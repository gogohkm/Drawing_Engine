#!/usr/bin/env python3
"""
Image Vectorizer - vtracer 알고리즘 기반 Python 구현

이미지를 벡터(선)로 변환하는 엔진.
의존성 최소화: PNG/JPEG 디코더 내장, OpenCV 없이 순수 Python 구현

핵심 알고리즘:
1. 이미지 → 이진화 (Binarization)
2. 연결 요소 분석 (Connected Component Labeling)
3. 윤곽선 추출 (Contour Tracing - Moore-Neighbor)
4. 경로 단순화 (Douglas-Peucker Algorithm)
5. DXF MCP 도구 시퀀스 생성

지원 형식 (의존성 없이):
- PNG (zlib 압축 사용)
- JPEG (baseline format)
- PPM/PGM/PBM
"""

import json
import math
import struct
import sys
import zlib
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional, Set
from collections import deque


# ============ PNG 디코더 (순수 Python, zlib 사용) ============

class PNGDecoder:
    """
    PNG 디코더 - 순수 Python 구현

    표준 라이브러리만 사용: struct, zlib

    지원:
    - Color types: 0 (Grayscale), 2 (RGB), 3 (Indexed), 4 (Grayscale+Alpha), 6 (RGBA)
    - Bit depths: 1, 2, 4, 8 (16-bit은 8-bit으로 변환)
    - Interlacing: Non-interlaced (Adam7은 지원하지 않음)
    """

    PNG_SIGNATURE = b'\x89PNG\r\n\x1a\n'

    def __init__(self):
        self.width = 0
        self.height = 0
        self.bit_depth = 8
        self.color_type = 0
        self.compression = 0
        self.filter_method = 0
        self.interlace = 0
        self.palette: List[Tuple[int, int, int]] = []
        self.pixels: List[List[Tuple[int, ...]]] = []

    def decode(self, filepath: str) -> 'PNGDecoder':
        """PNG 파일 디코드"""
        with open(filepath, 'rb') as f:
            return self.decode_bytes(f.read())

    def decode_bytes(self, data: bytes) -> 'PNGDecoder':
        """바이트 데이터에서 PNG 디코드"""
        if data[:8] != self.PNG_SIGNATURE:
            raise ValueError("Invalid PNG signature")

        pos = 8
        idat_data = b''

        while pos < len(data):
            # 청크 읽기: length (4) + type (4) + data + crc (4)
            length = struct.unpack('>I', data[pos:pos+4])[0]
            chunk_type = data[pos+4:pos+8].decode('ascii')
            chunk_data = data[pos+8:pos+8+length]
            pos += 12 + length

            if chunk_type == 'IHDR':
                self._parse_ihdr(chunk_data)
            elif chunk_type == 'PLTE':
                self._parse_plte(chunk_data)
            elif chunk_type == 'IDAT':
                idat_data += chunk_data
            elif chunk_type == 'IEND':
                break

        # IDAT 압축 해제 및 필터 해제
        self._decode_image_data(idat_data)
        return self

    def _parse_ihdr(self, data: bytes):
        """IHDR 청크 파싱"""
        (self.width, self.height, self.bit_depth, self.color_type,
         self.compression, self.filter_method, self.interlace) = struct.unpack('>IIBBBBB', data)

        if self.interlace != 0:
            raise NotImplementedError("Adam7 interlacing not supported")

    def _parse_plte(self, data: bytes):
        """PLTE 청크 파싱 (팔레트)"""
        self.palette = []
        for i in range(0, len(data), 3):
            self.palette.append((data[i], data[i+1], data[i+2]))

    def _decode_image_data(self, compressed_data: bytes):
        """이미지 데이터 디코드"""
        # zlib 압축 해제
        raw_data = zlib.decompress(compressed_data)

        # 채널 수 결정
        channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}.get(self.color_type, 1)
        bytes_per_pixel = max(1, (self.bit_depth * channels + 7) // 8)
        scanline_width = self.width * bytes_per_pixel

        self.pixels = []
        pos = 0
        prev_row = [0] * scanline_width

        for y in range(self.height):
            filter_type = raw_data[pos]
            pos += 1

            row_data = list(raw_data[pos:pos+scanline_width])
            pos += scanline_width

            # 필터 해제
            row_data = self._unfilter_row(filter_type, row_data, prev_row, bytes_per_pixel)
            prev_row = row_data

            # 픽셀로 변환
            row_pixels = self._bytes_to_pixels(row_data, channels)
            self.pixels.append(row_pixels)

    def _unfilter_row(self, filter_type: int, row: List[int], prev_row: List[int], bpp: int) -> List[int]:
        """PNG 필터 해제"""
        result = row[:]

        if filter_type == 0:  # None
            pass
        elif filter_type == 1:  # Sub
            for i in range(bpp, len(result)):
                result[i] = (result[i] + result[i - bpp]) & 0xFF
        elif filter_type == 2:  # Up
            for i in range(len(result)):
                result[i] = (result[i] + prev_row[i]) & 0xFF
        elif filter_type == 3:  # Average
            for i in range(len(result)):
                left = result[i - bpp] if i >= bpp else 0
                up = prev_row[i]
                result[i] = (result[i] + (left + up) // 2) & 0xFF
        elif filter_type == 4:  # Paeth
            for i in range(len(result)):
                left = result[i - bpp] if i >= bpp else 0
                up = prev_row[i]
                up_left = prev_row[i - bpp] if i >= bpp else 0
                result[i] = (result[i] + self._paeth_predictor(left, up, up_left)) & 0xFF

        return result

    def _paeth_predictor(self, a: int, b: int, c: int) -> int:
        """Paeth predictor"""
        p = a + b - c
        pa = abs(p - a)
        pb = abs(p - b)
        pc = abs(p - c)
        if pa <= pb and pa <= pc:
            return a
        elif pb <= pc:
            return b
        return c

    def _bytes_to_pixels(self, row_data: List[int], channels: int) -> List[Tuple[int, ...]]:
        """바이트 데이터를 픽셀로 변환"""
        pixels = []

        if self.bit_depth == 8:
            for i in range(0, len(row_data), channels):
                if self.color_type == 0:  # Grayscale
                    pixels.append((row_data[i],))
                elif self.color_type == 2:  # RGB
                    pixels.append((row_data[i], row_data[i+1], row_data[i+2]))
                elif self.color_type == 3:  # Indexed
                    idx = row_data[i]
                    if idx < len(self.palette):
                        pixels.append(self.palette[idx])
                    else:
                        pixels.append((0, 0, 0))
                elif self.color_type == 4:  # Grayscale + Alpha
                    pixels.append((row_data[i], row_data[i+1]))
                elif self.color_type == 6:  # RGBA
                    pixels.append((row_data[i], row_data[i+1], row_data[i+2], row_data[i+3]))
        elif self.bit_depth < 8:
            # 1, 2, 4 bit depths (palette 또는 grayscale)
            bits_per_pixel = self.bit_depth
            mask = (1 << bits_per_pixel) - 1
            pixel_count = 0

            for byte_val in row_data:
                for bit_offset in range(8 - bits_per_pixel, -1, -bits_per_pixel):
                    if pixel_count >= self.width:
                        break
                    idx = (byte_val >> bit_offset) & mask

                    if self.color_type == 3 and idx < len(self.palette):  # Indexed
                        pixels.append(self.palette[idx])
                    else:  # Grayscale
                        # Scale to 0-255
                        val = idx * 255 // mask
                        pixels.append((val,))
                    pixel_count += 1
        elif self.bit_depth == 16:
            # 16-bit -> 8-bit 변환
            step = channels * 2
            for i in range(0, len(row_data), step):
                pixel = []
                for c in range(channels):
                    high = row_data[i + c*2]
                    # 16-bit을 8-bit으로 변환 (상위 바이트만 사용)
                    pixel.append(high)
                pixels.append(tuple(pixel))

        return pixels

    def to_grayscale_array(self) -> List[List[int]]:
        """그레이스케일 2D 배열로 변환"""
        result = []
        for row in self.pixels:
            gray_row = []
            for pixel in row:
                if len(pixel) == 1:  # Grayscale
                    gray_row.append(pixel[0])
                elif len(pixel) == 2:  # Grayscale + Alpha
                    gray_row.append(pixel[0])
                elif len(pixel) >= 3:  # RGB or RGBA
                    r, g, b = pixel[0], pixel[1], pixel[2]
                    gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                    gray_row.append(gray)
            result.append(gray_row)
        return result

    def to_rgb_array(self) -> List[List[Tuple[int, int, int]]]:
        """RGB 2D 배열로 변환"""
        result = []
        for row in self.pixels:
            rgb_row = []
            for pixel in row:
                if len(pixel) == 1:  # Grayscale
                    val = pixel[0]
                    rgb_row.append((val, val, val))
                elif len(pixel) == 2:  # Grayscale + Alpha
                    val = pixel[0]
                    rgb_row.append((val, val, val))
                elif len(pixel) >= 3:  # RGB or RGBA
                    rgb_row.append((pixel[0], pixel[1], pixel[2]))
            result.append(rgb_row)
        return result


# ============ JPEG 디코더 (순수 Python, Baseline DCT) ============

class JPEGDecoder:
    """
    JPEG 디코더 - 순수 Python 구현 (Baseline DCT)

    표준 라이브러리만 사용: struct

    지원:
    - Baseline DCT (SOF0)
    - Huffman coding
    - YCbCr -> RGB 변환

    미지원:
    - Progressive JPEG
    - Arithmetic coding
    - CMYK
    """

    # Zigzag 순서
    ZIGZAG = [
        0,  1,  8, 16,  9,  2,  3, 10,
        17, 24, 32, 25, 18, 11,  4,  5,
        12, 19, 26, 33, 40, 48, 41, 34,
        27, 20, 13,  6,  7, 14, 21, 28,
        35, 42, 49, 56, 57, 50, 43, 36,
        29, 22, 15, 23, 30, 37, 44, 51,
        58, 59, 52, 45, 38, 31, 39, 46,
        53, 60, 61, 54, 47, 55, 62, 63
    ]

    def __init__(self):
        self.width = 0
        self.height = 0
        self.components = []
        self.quant_tables = {}
        self.huffman_dc = {}
        self.huffman_ac = {}
        self.pixels: List[List[Tuple[int, int, int]]] = []
        self._bit_buffer = 0
        self._bits_left = 0

    def decode(self, filepath: str) -> 'JPEGDecoder':
        """JPEG 파일 디코드"""
        with open(filepath, 'rb') as f:
            return self.decode_bytes(f.read())

    def decode_bytes(self, data: bytes) -> 'JPEGDecoder':
        """바이트 데이터에서 JPEG 디코드"""
        if data[:2] != b'\xFF\xD8':
            raise ValueError("Invalid JPEG signature")

        pos = 2
        while pos < len(data) - 1:
            if data[pos] != 0xFF:
                pos += 1
                continue

            marker = data[pos + 1]
            pos += 2

            if marker == 0xD8:  # SOI
                continue
            elif marker == 0xD9:  # EOI
                break
            elif marker == 0x00:  # Stuffed byte
                continue
            elif 0xD0 <= marker <= 0xD7:  # RST markers
                continue

            # 마커 길이
            length = struct.unpack('>H', data[pos:pos+2])[0]
            segment = data[pos+2:pos+length]
            pos += length

            if marker == 0xDB:  # DQT
                self._parse_dqt(segment)
            elif marker == 0xC0:  # SOF0 (Baseline DCT)
                self._parse_sof0(segment)
            elif marker == 0xC4:  # DHT
                self._parse_dht(segment)
            elif marker == 0xDA:  # SOS
                # SOS 후 이미지 데이터
                scan_data = self._extract_scan_data(data[pos:])
                self._decode_scan(segment, scan_data)
                break

        return self

    def _parse_dqt(self, data: bytes):
        """양자화 테이블 파싱"""
        pos = 0
        while pos < len(data):
            info = data[pos]
            precision = (info >> 4) & 0x0F  # 0 = 8-bit, 1 = 16-bit
            table_id = info & 0x0F
            pos += 1

            if precision == 0:
                table = list(data[pos:pos+64])
                pos += 64
            else:
                table = []
                for i in range(64):
                    table.append(struct.unpack('>H', data[pos:pos+2])[0])
                    pos += 2

            # Zigzag 역순
            self.quant_tables[table_id] = [0] * 64
            for i in range(64):
                self.quant_tables[table_id][self.ZIGZAG[i]] = table[i]

    def _parse_sof0(self, data: bytes):
        """프레임 헤더 파싱 (Baseline DCT)"""
        precision = data[0]
        self.height = struct.unpack('>H', data[1:3])[0]
        self.width = struct.unpack('>H', data[3:5])[0]
        num_components = data[5]

        self.components = []
        for i in range(num_components):
            comp_id = data[6 + i*3]
            sampling = data[7 + i*3]
            h_sampling = (sampling >> 4) & 0x0F
            v_sampling = sampling & 0x0F
            quant_table = data[8 + i*3]
            self.components.append({
                'id': comp_id,
                'h_sampling': h_sampling,
                'v_sampling': v_sampling,
                'quant_table': quant_table
            })

    def _parse_dht(self, data: bytes):
        """Huffman 테이블 파싱"""
        pos = 0
        while pos < len(data):
            info = data[pos]
            table_class = (info >> 4) & 0x0F  # 0 = DC, 1 = AC
            table_id = info & 0x0F
            pos += 1

            # 코드 길이별 개수 (16개)
            counts = list(data[pos:pos+16])
            pos += 16

            # 심볼 읽기
            symbols = []
            for count in counts:
                for _ in range(count):
                    symbols.append(data[pos])
                    pos += 1

            # Huffman 테이블 생성
            table = self._build_huffman_table(counts, symbols)

            if table_class == 0:
                self.huffman_dc[table_id] = table
            else:
                self.huffman_ac[table_id] = table

    def _build_huffman_table(self, counts: List[int], symbols: List[int]) -> Dict:
        """Huffman 테이블 생성"""
        table = {}
        code = 0
        symbol_idx = 0

        for length in range(1, 17):
            for _ in range(counts[length - 1]):
                # (코드, 길이) -> 심볼
                table[(code, length)] = symbols[symbol_idx]
                symbol_idx += 1
                code += 1
            code <<= 1

        return table

    def _extract_scan_data(self, data: bytes) -> bytes:
        """스캔 데이터 추출 (바이트 스터핑 제거)"""
        result = bytearray()
        i = 0
        while i < len(data):
            if data[i] == 0xFF:
                if i + 1 < len(data):
                    if data[i + 1] == 0x00:
                        result.append(0xFF)
                        i += 2
                        continue
                    elif data[i + 1] == 0xD9:  # EOI
                        break
                    elif 0xD0 <= data[i + 1] <= 0xD7:  # RST
                        i += 2
                        continue
            result.append(data[i])
            i += 1
        return bytes(result)

    def _decode_scan(self, sos_data: bytes, scan_data: bytes):
        """스캔 데이터 디코드"""
        # SOS 헤더 파싱
        num_components = sos_data[0]
        comp_info = []
        for i in range(num_components):
            comp_id = sos_data[1 + i*2]
            tables = sos_data[2 + i*2]
            dc_table = (tables >> 4) & 0x0F
            ac_table = tables & 0x0F
            comp_info.append({'id': comp_id, 'dc': dc_table, 'ac': ac_table})

        # 간단한 구현: 4:4:4 서브샘플링만 지원
        # 복잡한 서브샘플링은 단순화
        self._bit_buffer = 0
        self._bits_left = 0
        self._scan_data = scan_data
        self._scan_pos = 0

        # MCU 크기 계산
        max_h = max(c['h_sampling'] for c in self.components)
        max_v = max(c['v_sampling'] for c in self.components)
        mcu_width = 8 * max_h
        mcu_height = 8 * max_v

        mcus_x = (self.width + mcu_width - 1) // mcu_width
        mcus_y = (self.height + mcu_height - 1) // mcu_height

        # 이미지 버퍼 초기화
        self.pixels = [[(0, 0, 0) for _ in range(self.width)] for _ in range(self.height)]

        # DC 예측 값
        dc_pred = [0] * len(self.components)

        try:
            for mcu_y in range(mcus_y):
                for mcu_x in range(mcus_x):
                    # 각 컴포넌트의 블록 디코드
                    blocks = []
                    for ci, comp in enumerate(self.components):
                        comp_blocks = []
                        for v in range(comp['v_sampling']):
                            for h in range(comp['h_sampling']):
                                block, dc_pred[ci] = self._decode_block(
                                    ci, comp_info[ci], dc_pred[ci]
                                )
                                comp_blocks.append(block)
                        blocks.append(comp_blocks)

                    # 블록을 픽셀로 변환
                    self._blocks_to_pixels(blocks, mcu_x, mcu_y, mcu_width, mcu_height)
        except (IndexError, KeyError):
            # 디코딩 오류 시 지금까지 디코드된 부분 유지
            pass

    def _decode_block(self, comp_idx: int, comp_info: Dict, dc_pred: int) -> Tuple[List[int], int]:
        """8x8 블록 디코드"""
        block = [0] * 64

        # DC 계수
        dc_table = self.huffman_dc.get(comp_info['dc'], {})
        category = self._decode_huffman(dc_table)
        if category > 0:
            diff = self._read_bits(category)
            if diff < (1 << (category - 1)):
                diff -= (1 << category) - 1
            dc_pred += diff
        block[0] = dc_pred

        # AC 계수
        ac_table = self.huffman_ac.get(comp_info['ac'], {})
        i = 1
        while i < 64:
            symbol = self._decode_huffman(ac_table)
            if symbol == 0:  # EOB
                break

            run_length = (symbol >> 4) & 0x0F
            category = symbol & 0x0F

            if symbol == 0xF0:  # ZRL
                i += 16
                continue

            i += run_length
            if i >= 64:
                break

            if category > 0:
                value = self._read_bits(category)
                if value < (1 << (category - 1)):
                    value -= (1 << category) - 1
                block[self.ZIGZAG[i]] = value
            i += 1

        # 역양자화
        quant_table = self.quant_tables.get(self.components[comp_idx]['quant_table'], [1]*64)
        for i in range(64):
            block[i] *= quant_table[i]

        # IDCT
        block = self._idct(block)

        return block, dc_pred

    def _decode_huffman(self, table: Dict) -> int:
        """Huffman 심볼 디코드"""
        code = 0
        for length in range(1, 17):
            code = (code << 1) | self._read_bit()
            if (code, length) in table:
                return table[(code, length)]
        return 0

    def _read_bit(self) -> int:
        """비트 읽기"""
        if self._bits_left == 0:
            if self._scan_pos >= len(self._scan_data):
                return 0
            self._bit_buffer = self._scan_data[self._scan_pos]
            self._scan_pos += 1
            self._bits_left = 8

        self._bits_left -= 1
        return (self._bit_buffer >> self._bits_left) & 1

    def _read_bits(self, n: int) -> int:
        """n비트 읽기"""
        value = 0
        for _ in range(n):
            value = (value << 1) | self._read_bit()
        return value

    def _idct(self, block: List[int]) -> List[int]:
        """역 이산 코사인 변환 (간소화 버전)"""
        result = [0] * 64

        # 간단한 IDCT 구현 (정확도보다 속도 우선)
        for y in range(8):
            for x in range(8):
                sum_val = 0.0
                for v in range(8):
                    for u in range(8):
                        cu = 0.7071067811865476 if u == 0 else 1.0
                        cv = 0.7071067811865476 if v == 0 else 1.0
                        cos_u = math.cos((2*x + 1) * u * math.pi / 16)
                        cos_v = math.cos((2*y + 1) * v * math.pi / 16)
                        sum_val += cu * cv * block[v * 8 + u] * cos_u * cos_v
                result[y * 8 + x] = int(sum_val / 4 + 128)

        # 클리핑
        for i in range(64):
            result[i] = max(0, min(255, result[i]))

        return result

    def _blocks_to_pixels(self, blocks: List[List[List[int]]], mcu_x: int, mcu_y: int,
                          mcu_width: int, mcu_height: int):
        """블록을 픽셀로 변환"""
        for by in range(mcu_height):
            for bx in range(mcu_width):
                px = mcu_x * mcu_width + bx
                py = mcu_y * mcu_height + by

                if px >= self.width or py >= self.height:
                    continue

                # 각 컴포넌트에서 값 가져오기
                values = []
                for ci, comp in enumerate(self.components):
                    h_sampling = comp['h_sampling']
                    v_sampling = comp['v_sampling']

                    # 블록 인덱스
                    block_x = (bx // 8) % h_sampling
                    block_y = (by // 8) % v_sampling
                    block_idx = block_y * h_sampling + block_x

                    # 블록 내 위치
                    in_x = bx % 8
                    in_y = by % 8

                    if block_idx < len(blocks[ci]):
                        values.append(blocks[ci][block_idx][in_y * 8 + in_x])
                    else:
                        values.append(128)

                # YCbCr -> RGB 변환
                if len(values) >= 3:
                    y, cb, cr = values[0], values[1], values[2]
                    r = int(y + 1.402 * (cr - 128))
                    g = int(y - 0.344136 * (cb - 128) - 0.714136 * (cr - 128))
                    b = int(y + 1.772 * (cb - 128))
                    r = max(0, min(255, r))
                    g = max(0, min(255, g))
                    b = max(0, min(255, b))
                    self.pixels[py][px] = (r, g, b)
                elif len(values) == 1:
                    # Grayscale
                    val = values[0]
                    self.pixels[py][px] = (val, val, val)

    def to_grayscale_array(self) -> List[List[int]]:
        """그레이스케일 2D 배열로 변환"""
        result = []
        for row in self.pixels:
            gray_row = []
            for r, g, b in row:
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                gray_row.append(gray)
            result.append(gray_row)
        return result

    def to_rgb_array(self) -> List[List[Tuple[int, int, int]]]:
        """RGB 2D 배열로 변환"""
        return self.pixels


# ============ 이미지 로더 (통합) ============

def load_image_native(filepath: str) -> Tuple[int, int, List[List[int]]]:
    """
    이미지 파일 로드 (의존성 없이)

    Args:
        filepath: 이미지 파일 경로

    Returns:
        (width, height, grayscale_pixels)
    """
    ext = filepath.lower().split('.')[-1]

    if ext == 'png':
        decoder = PNGDecoder().decode(filepath)
        pixels = decoder.to_grayscale_array()
        return decoder.width, decoder.height, pixels

    elif ext in ('jpg', 'jpeg'):
        decoder = JPEGDecoder().decode(filepath)
        pixels = decoder.to_grayscale_array()
        return decoder.width, decoder.height, pixels

    elif ext in ('ppm', 'pgm', 'pbm'):
        # 기존 PPM 로더 사용 (BinaryImage.from_ppm에서 가져옴)
        with open(filepath, 'rb') as f:
            magic = f.readline().decode('ascii').strip()

            line = f.readline()
            while line.startswith(b'#'):
                line = f.readline()

            parts = line.decode('ascii').split()
            width, height = int(parts[0]), int(parts[1])
            max_val = int(f.readline().decode('ascii').strip())

            pixels = []

            if magic == 'P5':  # Binary grayscale
                for y in range(height):
                    row = []
                    for x in range(width):
                        pixel = f.read(1)[0]
                        row.append(pixel * 255 // max_val)
                    pixels.append(row)

            elif magic == 'P6':  # Binary RGB
                for y in range(height):
                    row = []
                    for x in range(width):
                        r, g, b = f.read(3)
                        gray = int(0.299 * r + 0.587 * g + 0.114 * b) * 255 // max_val
                        row.append(gray)
                    pixels.append(row)

            elif magic == 'P2':  # ASCII grayscale
                data = f.read().decode('ascii').split()
                idx = 0
                for y in range(height):
                    row = []
                    for x in range(width):
                        row.append(int(data[idx]) * 255 // max_val)
                        idx += 1
                    pixels.append(row)

            elif magic == 'P3':  # ASCII RGB
                data = f.read().decode('ascii').split()
                idx = 0
                for y in range(height):
                    row = []
                    for x in range(width):
                        r, g, b = int(data[idx]), int(data[idx+1]), int(data[idx+2])
                        gray = int(0.299 * r + 0.587 * g + 0.114 * b) * 255 // max_val
                        row.append(gray)
                        idx += 3
                    pixels.append(row)

            return width, height, pixels

    else:
        raise ValueError(f"Unsupported image format: {ext}. Supported: png, jpg, jpeg, ppm, pgm, pbm")


@dataclass
class Point:
    x: float
    y: float

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance_to(self, other: 'Point') -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


@dataclass
class Line:
    start: Point
    end: Point
    layer: str = "OUTLINE"

    def length(self) -> float:
        return self.start.distance_to(self.end)


@dataclass
class Contour:
    """윤곽선 - 점들의 순서 리스트"""
    points: List[Point] = field(default_factory=list)
    is_closed: bool = True

    def length(self) -> float:
        total = 0.0
        for i in range(len(self.points) - 1):
            total += self.points[i].distance_to(self.points[i+1])
        if self.is_closed and len(self.points) > 1:
            total += self.points[-1].distance_to(self.points[0])
        return total


class BinaryImage:
    """이진 이미지 클래스"""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        # 1 = foreground (black in original), 0 = background
        self.pixels: List[List[int]] = [[0] * width for _ in range(height)]

    def set_pixel(self, x: int, y: int, value: int):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = value

    def get_pixel(self, x: int, y: int) -> int:
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.pixels[y][x]
        return 0  # 경계 밖은 배경

    @classmethod
    def from_pil_image(cls, pil_image, threshold: int = 128) -> 'BinaryImage':
        """PIL 이미지에서 이진 이미지 생성"""
        # 그레이스케일로 변환
        gray = pil_image.convert('L')
        width, height = gray.size

        binary = cls(width, height)
        for y in range(height):
            for x in range(width):
                pixel = gray.getpixel((x, y))
                # threshold 이하면 전경 (1), 아니면 배경 (0)
                binary.set_pixel(x, y, 1 if pixel < threshold else 0)

        return binary

    @classmethod
    def from_grayscale_array(cls, pixels: List[List[int]], threshold: int = 128) -> 'BinaryImage':
        """
        그레이스케일 2D 배열에서 이진 이미지 생성

        Args:
            pixels: 2D 배열 [height][width], 값 0-255
            threshold: 이진화 임계값
        """
        height = len(pixels)
        width = len(pixels[0]) if height > 0 else 0

        binary = cls(width, height)
        for y in range(height):
            for x in range(width):
                # threshold 이하면 전경 (1), 아니면 배경 (0)
                binary.set_pixel(x, y, 1 if pixels[y][x] < threshold else 0)

        return binary

    @classmethod
    def from_rgb_array(cls, pixels: List[List[Tuple[int, int, int]]], threshold: int = 128) -> 'BinaryImage':
        """
        RGB 2D 배열에서 이진 이미지 생성

        Args:
            pixels: 2D 배열 [height][width], 각 값은 (r, g, b) 튜플
            threshold: 이진화 임계값
        """
        height = len(pixels)
        width = len(pixels[0]) if height > 0 else 0

        binary = cls(width, height)
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[y][x]
                # 그레이스케일 변환: Y = 0.299*R + 0.587*G + 0.114*B
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                binary.set_pixel(x, y, 1 if gray < threshold else 0)

        return binary

    @classmethod
    def from_ppm(cls, filepath: str, threshold: int = 128) -> 'BinaryImage':
        """
        PPM/PGM 파일에서 이진 이미지 로드 (순수 Python, 의존성 없음)

        지원 형식: P2 (ASCII grayscale), P3 (ASCII RGB), P5 (binary grayscale), P6 (binary RGB)
        """
        with open(filepath, 'rb') as f:
            # 매직 넘버 읽기
            magic = f.readline().decode('ascii').strip()

            # 주석 건너뛰기
            line = f.readline()
            while line.startswith(b'#'):
                line = f.readline()

            # 크기 읽기
            parts = line.decode('ascii').split()
            width, height = int(parts[0]), int(parts[1])

            # 최대값 읽기
            max_val = int(f.readline().decode('ascii').strip())

            binary = cls(width, height)

            if magic == 'P5':  # Binary grayscale
                for y in range(height):
                    for x in range(width):
                        pixel = f.read(1)[0]
                        gray = pixel * 255 // max_val
                        binary.set_pixel(x, y, 1 if gray < threshold else 0)

            elif magic == 'P6':  # Binary RGB
                for y in range(height):
                    for x in range(width):
                        r, g, b = f.read(3)
                        gray = int(0.299 * r + 0.587 * g + 0.114 * b) * 255 // max_val
                        binary.set_pixel(x, y, 1 if gray < threshold else 0)

            elif magic == 'P2':  # ASCII grayscale
                data = f.read().decode('ascii').split()
                idx = 0
                for y in range(height):
                    for x in range(width):
                        pixel = int(data[idx])
                        gray = pixel * 255 // max_val
                        binary.set_pixel(x, y, 1 if gray < threshold else 0)
                        idx += 1

            elif magic == 'P3':  # ASCII RGB
                data = f.read().decode('ascii').split()
                idx = 0
                for y in range(height):
                    for x in range(width):
                        r, g, b = int(data[idx]), int(data[idx+1]), int(data[idx+2])
                        gray = int(0.299 * r + 0.587 * g + 0.114 * b) * 255 // max_val
                        binary.set_pixel(x, y, 1 if gray < threshold else 0)
                        idx += 3

            else:
                raise ValueError(f"Unsupported PPM format: {magic}")

        return binary

    @classmethod
    def from_file(cls, filepath: str, threshold: int = 128) -> 'BinaryImage':
        """
        파일에서 이진 이미지 로드

        지원 형식 (의존성 없이):
        - PNG: 내장 PNGDecoder 사용
        - JPEG: 내장 JPEGDecoder 사용
        - PPM/PGM/PBM: 직접 파싱
        """
        ext = filepath.lower().split('.')[-1]

        if ext in ('ppm', 'pgm', 'pbm'):
            return cls.from_ppm(filepath, threshold)

        # PNG 네이티브 디코더 사용
        if ext == 'png':
            try:
                width, height, gray_pixels = load_image_native(filepath)
                return cls.from_grayscale_array(gray_pixels, threshold)
            except Exception as e:
                raise ValueError(f"Failed to decode PNG: {e}")

        # JPEG 네이티브 디코더 사용
        if ext in ('jpg', 'jpeg'):
            try:
                width, height, gray_pixels = load_image_native(filepath)
                return cls.from_grayscale_array(gray_pixels, threshold)
            except Exception as e:
                raise ValueError(f"Failed to decode JPEG: {e}")

        # 그 외 형식: PIL 사용 시도
        try:
            from PIL import Image
            img = Image.open(filepath)
            return cls.from_pil_image(img, threshold)
        except ImportError:
            raise ImportError(
                f"Unsupported format: {ext}. Supported: png, jpg, jpeg, ppm, pgm, pbm\n"
                f"Or install Pillow for additional formats."
            )


class GrayscaleImage:
    """그레이스케일 이미지 클래스 (엣지 감지용)"""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pixels: List[List[int]] = [[0] * width for _ in range(height)]

    def set_pixel(self, x: int, y: int, value: int):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = max(0, min(255, value))

    def get_pixel(self, x: int, y: int) -> int:
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.pixels[y][x]
        return 0

    @classmethod
    def from_ppm(cls, filepath: str) -> 'GrayscaleImage':
        """PPM/PGM 파일에서 그레이스케일 이미지 로드"""
        with open(filepath, 'rb') as f:
            magic = f.readline().decode('ascii').strip()

            line = f.readline()
            while line.startswith(b'#'):
                line = f.readline()

            parts = line.decode('ascii').split()
            width, height = int(parts[0]), int(parts[1])
            max_val = int(f.readline().decode('ascii').strip())

            gray = cls(width, height)

            if magic == 'P5':
                for y in range(height):
                    for x in range(width):
                        pixel = f.read(1)[0]
                        gray.set_pixel(x, y, pixel * 255 // max_val)

            elif magic == 'P6':
                for y in range(height):
                    for x in range(width):
                        r, g, b = f.read(3)
                        val = int(0.299 * r + 0.587 * g + 0.114 * b)
                        gray.set_pixel(x, y, val * 255 // max_val)

            elif magic == 'P2':
                data = f.read().decode('ascii').split()
                idx = 0
                for y in range(height):
                    for x in range(width):
                        gray.set_pixel(x, y, int(data[idx]) * 255 // max_val)
                        idx += 1

            elif magic == 'P3':
                data = f.read().decode('ascii').split()
                idx = 0
                for y in range(height):
                    for x in range(width):
                        r, g, b = int(data[idx]), int(data[idx+1]), int(data[idx+2])
                        val = int(0.299 * r + 0.587 * g + 0.114 * b)
                        gray.set_pixel(x, y, val * 255 // max_val)
                        idx += 3

        return gray

    @classmethod
    def from_file(cls, filepath: str) -> 'GrayscaleImage':
        """
        파일에서 그레이스케일 이미지 로드

        지원 형식 (의존성 없이):
        - PNG: 내장 PNGDecoder 사용
        - JPEG: 내장 JPEGDecoder 사용
        - PPM/PGM/PBM: 직접 파싱
        """
        ext = filepath.lower().split('.')[-1]

        if ext in ('ppm', 'pgm', 'pbm'):
            return cls.from_ppm(filepath)

        # PNG/JPEG 네이티브 디코더 사용
        if ext in ('png', 'jpg', 'jpeg'):
            try:
                width, height, gray_pixels = load_image_native(filepath)
                gray = cls(width, height)
                for y in range(height):
                    for x in range(width):
                        gray.set_pixel(x, y, gray_pixels[y][x])
                return gray
            except Exception as e:
                raise ValueError(f"Failed to decode image: {e}")

        raise ValueError(f"Unsupported format: {ext}. Supported: png, jpg, jpeg, ppm, pgm, pbm")


class EdgeDetector:
    """
    엣지 감지 - Sobel 연산자 기반

    사진에서 선(엣지)을 추출하기 위한 전처리
    """

    # Sobel 커널
    SOBEL_X = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]

    SOBEL_Y = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ]

    @staticmethod
    def detect_edges(gray_image: GrayscaleImage, threshold: int = 50) -> BinaryImage:
        """
        Sobel 엣지 감지

        Args:
            gray_image: 그레이스케일 이미지
            threshold: 엣지 감지 임계값 (낮을수록 더 많은 엣지)

        Returns:
            엣지가 1인 이진 이미지
        """
        width = gray_image.width
        height = gray_image.height
        binary = BinaryImage(width, height)

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                # Sobel X 방향
                gx = 0
                for ky in range(3):
                    for kx in range(3):
                        gx += gray_image.get_pixel(x + kx - 1, y + ky - 1) * EdgeDetector.SOBEL_X[ky][kx]

                # Sobel Y 방향
                gy = 0
                for ky in range(3):
                    for kx in range(3):
                        gy += gray_image.get_pixel(x + kx - 1, y + ky - 1) * EdgeDetector.SOBEL_Y[ky][kx]

                # 기울기 크기
                magnitude = int(math.sqrt(gx * gx + gy * gy))

                # 임계값 적용
                if magnitude > threshold:
                    binary.set_pixel(x, y, 1)

        return binary

    @staticmethod
    def detect_edges_simple(gray_image: GrayscaleImage, threshold: int = 30) -> BinaryImage:
        """
        단순 엣지 감지 (빠른 버전)

        인접 픽셀과의 차이만으로 엣지 감지
        """
        width = gray_image.width
        height = gray_image.height
        binary = BinaryImage(width, height)

        for y in range(height - 1):
            for x in range(width - 1):
                current = gray_image.get_pixel(x, y)
                right = gray_image.get_pixel(x + 1, y)
                down = gray_image.get_pixel(x, y + 1)

                diff = max(abs(current - right), abs(current - down))

                if diff > threshold:
                    binary.set_pixel(x, y, 1)

        return binary


class ConnectedComponentLabeler:
    """연결 요소 레이블링 (Flood Fill 기반)"""

    def __init__(self, binary_image: BinaryImage):
        self.image = binary_image
        self.labels: List[List[int]] = [
            [0] * binary_image.width for _ in range(binary_image.height)
        ]
        self.num_labels = 0
        self.label_pixels: Dict[int, List[Tuple[int, int]]] = {}

    def label(self, min_area: int = 4) -> int:
        """
        연결 요소 레이블링 수행

        Args:
            min_area: 최소 픽셀 수 (이보다 작은 영역은 무시)

        Returns:
            레이블 수
        """
        current_label = 0

        for y in range(self.image.height):
            for x in range(self.image.width):
                if self.image.get_pixel(x, y) == 1 and self.labels[y][x] == 0:
                    current_label += 1
                    pixels = self._flood_fill(x, y, current_label)

                    if len(pixels) >= min_area:
                        self.label_pixels[current_label] = pixels
                    else:
                        # 작은 영역은 레이블 제거
                        for px, py in pixels:
                            self.labels[py][px] = 0
                        current_label -= 1

        self.num_labels = current_label
        return current_label

    def _flood_fill(self, start_x: int, start_y: int, label: int) -> List[Tuple[int, int]]:
        """BFS 기반 Flood Fill"""
        pixels = []
        queue = deque([(start_x, start_y)])

        while queue:
            x, y = queue.popleft()

            if not (0 <= x < self.image.width and 0 <= y < self.image.height):
                continue
            if self.image.get_pixel(x, y) != 1 or self.labels[y][x] != 0:
                continue

            self.labels[y][x] = label
            pixels.append((x, y))

            # 4-연결 (상하좌우)
            queue.append((x + 1, y))
            queue.append((x - 1, y))
            queue.append((x, y + 1))
            queue.append((x, y - 1))

        return pixels

    def get_component_pixels(self, label: int) -> List[Tuple[int, int]]:
        """특정 레이블의 픽셀들 반환"""
        return self.label_pixels.get(label, [])


class ContourTracer:
    """
    윤곽선 추적 - Moore-Neighbor Tracing Algorithm

    참고: https://www.imageprocessingplace.com/downloads_V3/root_downloads/tutorials/contour_tracing_Abeer_George_Ghuneim/moore.html
    """

    # Moore 이웃: 시계방향 (오른쪽부터)
    DIRECTIONS = [
        (1, 0),   # 0: 오른쪽
        (1, 1),   # 1: 오른쪽 아래
        (0, 1),   # 2: 아래
        (-1, 1),  # 3: 왼쪽 아래
        (-1, 0),  # 4: 왼쪽
        (-1, -1), # 5: 왼쪽 위
        (0, -1),  # 6: 위
        (1, -1),  # 7: 오른쪽 위
    ]

    def __init__(self, binary_image: BinaryImage):
        self.image = binary_image
        self.visited: Set[Tuple[int, int]] = set()

    def trace_all_contours(self, min_length: int = 10) -> List[Contour]:
        """모든 윤곽선 추출"""
        contours = []

        for y in range(self.image.height):
            for x in range(self.image.width):
                # 전경 픽셀이고 왼쪽이 배경이면 외곽선 시작점
                if self.image.get_pixel(x, y) == 1:
                    if self.image.get_pixel(x - 1, y) == 0:
                        if (x, y) not in self.visited:
                            contour = self._trace_contour(x, y)
                            if contour and len(contour.points) >= min_length:
                                contours.append(contour)

        return contours

    def _trace_contour(self, start_x: int, start_y: int) -> Optional[Contour]:
        """단일 윤곽선 추적 (Moore-Neighbor)"""
        contour = Contour()

        x, y = start_x, start_y
        # 시작 방향: 왼쪽에서 들어옴 (방향 4의 반대 = 0)
        direction = 0

        first = True
        while True:
            contour.points.append(Point(x, y))
            self.visited.add((x, y))

            # 다음 경계 픽셀 찾기
            found = False
            # 이전 방향의 반대 + 1부터 시계방향으로 검색
            start_dir = (direction + 5) % 8  # 반대 방향 + 1

            for i in range(8):
                check_dir = (start_dir + i) % 8
                dx, dy = self.DIRECTIONS[check_dir]
                nx, ny = x + dx, y + dy

                if self.image.get_pixel(nx, ny) == 1:
                    x, y = nx, ny
                    direction = check_dir
                    found = True
                    break

            if not found:
                break

            # 시작점으로 돌아오면 종료
            if not first and x == start_x and y == start_y:
                break

            first = False

            # 무한 루프 방지
            if len(contour.points) > self.image.width * self.image.height:
                break

        return contour if len(contour.points) >= 3 else None


class PathSimplifier:
    """
    경로 단순화 - Douglas-Peucker Algorithm

    곡선을 적은 수의 점으로 근사화
    """

    @staticmethod
    def simplify(points: List[Point], epsilon: float = 2.0) -> List[Point]:
        """
        Douglas-Peucker 알고리즘으로 경로 단순화

        Args:
            points: 원본 점들
            epsilon: 허용 오차 (클수록 더 단순화)

        Returns:
            단순화된 점들
        """
        if len(points) < 3:
            return points

        # 시작점과 끝점
        start = points[0]
        end = points[-1]

        # 가장 먼 점 찾기
        max_dist = 0
        max_idx = 0

        for i in range(1, len(points) - 1):
            dist = PathSimplifier._perpendicular_distance(points[i], start, end)
            if dist > max_dist:
                max_dist = dist
                max_idx = i

        # 최대 거리가 epsilon보다 크면 재귀 분할
        if max_dist > epsilon:
            left = PathSimplifier.simplify(points[:max_idx + 1], epsilon)
            right = PathSimplifier.simplify(points[max_idx:], epsilon)
            return left[:-1] + right
        else:
            return [start, end]

    @staticmethod
    def _perpendicular_distance(point: Point, line_start: Point, line_end: Point) -> float:
        """점에서 직선까지의 수직 거리"""
        dx = line_end.x - line_start.x
        dy = line_end.y - line_start.y

        if dx == 0 and dy == 0:
            return point.distance_to(line_start)

        # 직선의 길이 제곱
        line_len_sq = dx * dx + dy * dy

        # 점에서 직선에 내린 수선의 발까지의 파라미터 t
        t = ((point.x - line_start.x) * dx + (point.y - line_start.y) * dy) / line_len_sq
        t = max(0, min(1, t))

        # 수선의 발 좌표
        proj_x = line_start.x + t * dx
        proj_y = line_start.y + t * dy

        return math.sqrt((point.x - proj_x)**2 + (point.y - proj_y)**2)


class ImageVectorizer:
    """
    이미지 벡터화 메인 클래스

    사진 → 선(벡터) 변환

    모드:
    - 'binary': 단순 이진화 (기본, 도면/스케치용)
    - 'edge': Sobel 엣지 감지 (사진용)
    - 'edge_simple': 단순 엣지 감지 (빠른 버전)
    """

    def __init__(self):
        self.binary_image: Optional[BinaryImage] = None
        self.gray_image: Optional[GrayscaleImage] = None
        self.contours: List[Contour] = []
        self.simplified_contours: List[Contour] = []
        self.lines: List[Line] = []

        # 설정
        self.mode = 'binary'          # 'binary', 'edge', 'edge_simple'
        self.threshold = 128          # 이진화 임계값
        self.edge_threshold = 50      # 엣지 감지 임계값
        self.min_component_area = 16  # 최소 연결 요소 크기
        self.min_contour_length = 10  # 최소 윤곽선 길이
        self.simplify_epsilon = 2.0   # 단순화 오차 허용치

        # 출력 설정
        self.output_scale = 1.0       # 출력 스케일
        self.output_offset = Point(0, 0)  # 출력 오프셋
        self.flip_y = True            # Y축 반전 (이미지는 위가 0, DXF는 아래가 0)

    def load_image(self, filepath: str) -> bool:
        """이미지 파일 로드 (PNG, JPEG, PPM 지원 - 의존성 없음)"""
        try:
            if self.mode in ('edge', 'edge_simple'):
                # 엣지 감지 모드: 그레이스케일로 로드 후 엣지 감지
                self.gray_image = GrayscaleImage.from_file(filepath)

                # 엣지 감지 실행
                if self.mode == 'edge':
                    self.binary_image = EdgeDetector.detect_edges(self.gray_image, self.edge_threshold)
                else:
                    self.binary_image = EdgeDetector.detect_edges_simple(self.gray_image, self.edge_threshold)
            else:
                # 이진화 모드
                self.binary_image = BinaryImage.from_file(filepath, self.threshold)
            return True
        except Exception as e:
            print(f"Error loading image: {e}")
            return False

    def load_from_base64(self, base64_data: str) -> bool:
        """Base64 이미지 데이터 로드"""
        try:
            import base64
            from PIL import Image
            import io

            # data:image/png;base64, 접두어 제거
            if ',' in base64_data:
                base64_data = base64_data.split(',')[1]

            image_data = base64.b64decode(base64_data)
            img = Image.open(io.BytesIO(image_data))
            self.binary_image = BinaryImage.from_pil_image(img, self.threshold)
            return True
        except Exception as e:
            print(f"Error loading base64 image: {e}")
            return False

    def vectorize(self) -> List[Line]:
        """
        벡터화 실행

        Returns:
            추출된 선 리스트
        """
        if not self.binary_image:
            raise ValueError("No image loaded")

        # 1. 연결 요소 레이블링
        labeler = ConnectedComponentLabeler(self.binary_image)
        num_labels = labeler.label(self.min_component_area)
        print(f"Found {num_labels} connected components")

        # 2. 윤곽선 추출
        tracer = ContourTracer(self.binary_image)
        self.contours = tracer.trace_all_contours(self.min_contour_length)
        print(f"Traced {len(self.contours)} contours")

        # 3. 경로 단순화
        self.simplified_contours = []
        for contour in self.contours:
            simplified_points = PathSimplifier.simplify(
                contour.points,
                self.simplify_epsilon
            )
            self.simplified_contours.append(Contour(
                points=simplified_points,
                is_closed=contour.is_closed
            ))

        # 4. 선 생성
        self.lines = []
        for contour in self.simplified_contours:
            self._contour_to_lines(contour)

        print(f"Generated {len(self.lines)} lines")
        return self.lines

    def _contour_to_lines(self, contour: Contour):
        """윤곽선을 선 리스트로 변환"""
        points = contour.points
        if len(points) < 2:
            return

        for i in range(len(points) - 1):
            start = self._transform_point(points[i])
            end = self._transform_point(points[i + 1])
            self.lines.append(Line(start=start, end=end))

        # 닫힌 윤곽선이면 마지막 점과 첫 점 연결
        if contour.is_closed and len(points) > 2:
            start = self._transform_point(points[-1])
            end = self._transform_point(points[0])
            self.lines.append(Line(start=start, end=end))

    def _transform_point(self, point: Point) -> Point:
        """좌표 변환 (스케일, 오프셋, Y반전)"""
        x = point.x * self.output_scale + self.output_offset.x
        y = point.y * self.output_scale

        if self.flip_y and self.binary_image:
            y = (self.binary_image.height - point.y) * self.output_scale

        y += self.output_offset.y

        return Point(x, y)

    def set_output_bounds(self, x: float, y: float, width: float, height: float):
        """
        출력 영역 설정 (DXF 배경 이미지 좌표에 맞춤)

        Args:
            x, y: 좌하단 좌표
            width, height: 영역 크기
        """
        if not self.binary_image:
            raise ValueError("Load image first")

        # 스케일 계산
        scale_x = width / self.binary_image.width
        scale_y = height / self.binary_image.height
        self.output_scale = min(scale_x, scale_y)

        # 오프셋 설정
        self.output_offset = Point(x, y)

    def generate_mcp_sequence(self, layer: str = "TRACE") -> Dict:
        """
        MCP 도구 시퀀스 생성

        Returns:
            실행 가능한 MCP 시퀀스
        """
        if not self.lines:
            return {"error": "No lines generated. Run vectorize() first."}

        sequence = []

        # 1. 레이어 생성
        sequence.append({
            "step": 1,
            "name": "레이어 생성",
            "tools": [{
                "tool": "create_layer",
                "args": {"name": layer, "color": 7}
            }]
        })

        # 2. 선 그리기 (배치로 나눔)
        BATCH_SIZE = 50
        line_tools = []

        for i, line in enumerate(self.lines):
            line_tools.append({
                "tool": "create_line",
                "args": {
                    "start": {"x": round(line.start.x, 2), "y": round(line.start.y, 2)},
                    "end": {"x": round(line.end.x, 2), "y": round(line.end.y, 2)},
                    "layer": layer
                },
                "id": f"line_{i}"
            })

        # 배치로 분할
        for batch_idx in range(0, len(line_tools), BATCH_SIZE):
            batch = line_tools[batch_idx:batch_idx + BATCH_SIZE]
            sequence.append({
                "step": len(sequence) + 1,
                "name": f"선 그리기 ({batch_idx+1}~{batch_idx+len(batch)})",
                "parallel": True,
                "tools": batch
            })

        return {
            "success": True,
            "total_lines": len(self.lines),
            "total_steps": len(sequence),
            "sequence": sequence
        }


# ============ CLI 함수들 ============

def cli_vectorize(image_path: str, bg_json: str, options_json: str = "{}") -> str:
    """
    이미지 벡터화 CLI

    Args:
        image_path: 이미지 파일 경로
        bg_json: 배경 영역 {"x":..., "y":..., "width":..., "height":...}
        options_json: 옵션
            - mode: 'binary' (이진화), 'edge' (Sobel 엣지), 'edge_simple' (단순 엣지)
            - threshold: 이진화 임계값 (기본: 128)
            - edge_threshold: 엣지 감지 임계값 (기본: 50)
            - epsilon: 단순화 허용 오차 (기본: 2.0)
            - min_length: 최소 윤곽선 길이 (기본: 10)
            - min_area: 최소 연결 요소 크기 (기본: 16)
            - layer: 출력 레이어 이름 (기본: TRACE)
    """
    try:
        bg = json.loads(bg_json)
        options = json.loads(options_json)

        vectorizer = ImageVectorizer()

        # 옵션 설정
        vectorizer.mode = options.get("mode", "binary")  # 'binary', 'edge', 'edge_simple'
        vectorizer.threshold = options.get("threshold", 128)
        vectorizer.edge_threshold = options.get("edge_threshold", 50)
        vectorizer.simplify_epsilon = options.get("epsilon", 2.0)
        vectorizer.min_contour_length = options.get("min_length", 10)
        vectorizer.min_component_area = options.get("min_area", 16)

        # 이미지 로드
        if not vectorizer.load_image(image_path):
            return json.dumps({"error": f"Failed to load image: {image_path}"})

        # 출력 영역 설정
        vectorizer.set_output_bounds(
            bg["x"], bg["y"],
            bg["width"], bg["height"]
        )

        # 벡터화
        vectorizer.vectorize()

        # MCP 시퀀스 생성
        layer = options.get("layer", "TRACE")
        result = vectorizer.generate_mcp_sequence(layer)

        return json.dumps(result, ensure_ascii=False, indent=2)

    except Exception as e:
        return json.dumps({"error": str(e)})


def cli_vectorize_base64(base64_data: str, bg_json: str, options_json: str = "{}") -> str:
    """
    Base64 이미지 벡터화
    """
    try:
        bg = json.loads(bg_json)
        options = json.loads(options_json)

        vectorizer = ImageVectorizer()

        # 옵션 설정
        vectorizer.threshold = options.get("threshold", 128)
        vectorizer.simplify_epsilon = options.get("epsilon", 2.0)
        vectorizer.min_contour_length = options.get("min_length", 10)
        vectorizer.min_component_area = options.get("min_area", 16)

        # Base64 이미지 로드
        if not vectorizer.load_from_base64(base64_data):
            return json.dumps({"error": "Failed to load base64 image"})

        # 출력 영역 설정
        vectorizer.set_output_bounds(
            bg["x"], bg["y"],
            bg["width"], bg["height"]
        )

        # 벡터화
        vectorizer.vectorize()

        # MCP 시퀀스 생성
        layer = options.get("layer", "TRACE")
        result = vectorizer.generate_mcp_sequence(layer)

        return json.dumps(result, ensure_ascii=False, indent=2)

    except Exception as e:
        return json.dumps({"error": str(e)})


def cli_info() -> str:
    """벡터화 엔진 정보"""
    return json.dumps({
        "name": "Image Vectorizer",
        "version": "2.0.0",
        "description": "vtracer 알고리즘 기반 이미지 벡터화 엔진 - 의존성 없이 PNG/JPEG 지원",
        "algorithm": [
            "1. 이미지 디코딩: PNG (zlib), JPEG (Baseline DCT), PPM/PGM 네이티브 지원",
            "2. 전처리: Binarization (이진화) 또는 Sobel Edge Detection (엣지 감지)",
            "3. Connected Component Labeling (연결 요소 분석)",
            "4. Moore-Neighbor Contour Tracing (윤곽선 추출)",
            "5. Douglas-Peucker Simplification (경로 단순화)",
            "6. MCP Sequence Generation (DXF 선 생성)"
        ],
        "modes": {
            "binary": "단순 이진화 - 도면, 스케치에 적합",
            "edge": "Sobel 엣지 감지 - 사진에서 선 추출에 적합",
            "edge_simple": "단순 엣지 감지 - 빠른 버전"
        },
        "options": {
            "mode": "처리 모드 ('binary', 'edge', 'edge_simple', 기본: 'binary')",
            "threshold": "이진화 임계값 (0-255, 기본: 128)",
            "edge_threshold": "엣지 감지 임계값 (기본: 50, 낮을수록 더 많은 엣지)",
            "epsilon": "단순화 허용 오차 (기본: 2.0, 클수록 더 단순)",
            "min_length": "최소 윤곽선 길이 (기본: 10)",
            "min_area": "최소 연결 요소 크기 (기본: 16)",
            "layer": "출력 레이어 이름 (기본: TRACE)"
        },
        "usage": {
            "basic": "vectorize '<이미지경로>' '<bg_json>'",
            "with_options": "vectorize '<이미지경로>' '<bg_json>' '<options_json>'",
            "edge_mode": "vectorize 'photo.jpg' '{...}' '{\"mode\":\"edge\",\"edge_threshold\":30}'"
        },
        "supported_formats": {
            "no_dependency": ["png", "jpg", "jpeg", "ppm", "pgm", "pbm"],
            "png_support": "완전 지원 - Non-interlaced, 모든 color type, bit depth 1~16",
            "jpeg_support": "Baseline DCT 지원 - Progressive JPEG 미지원",
            "requires_pillow": ["gif", "bmp", "tiff", "webp"]
        },
        "decoders": {
            "PNGDecoder": "순수 Python PNG 디코더 (zlib 압축 해제)",
            "JPEGDecoder": "순수 Python JPEG 디코더 (Baseline DCT, Huffman)"
        }
    }, ensure_ascii=False, indent=2)


# ============ Main ============

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Image Vectorizer - vtracer 기반 이미지→벡터 변환")
        print("")
        print("Usage:")
        print("  python image_vectorizer.py info")
        print("  python image_vectorizer.py vectorize '<image_path>' '<bg_json>' '[options]'")
        print("  python image_vectorizer.py vectorize_base64 '<base64>' '<bg_json>' '[options]'")
        print("")
        print("Examples:")
        print('  python image_vectorizer.py vectorize "photo.jpg" \'{"x":-73,"y":-77,"width":178,"height":100}\'')
        print('  python image_vectorizer.py vectorize "photo.jpg" \'{"x":0,"y":0,"width":100,"height":100}\' \'{"threshold":100,"epsilon":3.0}\'')
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "info":
        print(cli_info())

    elif cmd == "vectorize" and len(sys.argv) >= 4:
        image_path = sys.argv[2]
        bg_json = sys.argv[3]
        options_json = sys.argv[4] if len(sys.argv) > 4 else "{}"
        print(cli_vectorize(image_path, bg_json, options_json))

    elif cmd == "vectorize_base64" and len(sys.argv) >= 4:
        base64_data = sys.argv[2]
        bg_json = sys.argv[3]
        options_json = sys.argv[4] if len(sys.argv) > 4 else "{}"
        print(cli_vectorize_base64(base64_data, bg_json, options_json))

    else:
        print(json.dumps({"error": f"Unknown command: {cmd}"}))
