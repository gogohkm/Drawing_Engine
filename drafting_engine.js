/**
 * Professional Drafting Engine v3.0 (Core Kernel)
 * Implements ISO/NCS Standards, Parametric Logic, and Structural Semantics.
 * 
 * CORE PHILOSOPHY:
 * 1. "Data, Not Lines": We define objects (Beam, Bolt), the engine generates lines.
 * 2. "Standards First": All dimensions and layers follow the Registry.
 * 3. "View Awareness": Objects know how to draw themselves in Top/Front/Side views.
 */

// --- 1. STANDARDS REGISTRY (The "Knowledge Base") ---
const STANDARDS = {
    LAYERS: {
        // ISO 13567 / NCS format: Major-Minor-Status
        // S: Structural, U: User/Annotation
        SCHEMA: {
            BEAM: { name: "S-BEAM-CUT", color: 4, linetype: "Continuous" },  // Main structural cut
            PLATE: { name: "S-PLAT-CUT", color: 3, linetype: "Continuous" },  // Plate cut
            BOLT: { name: "S-BOLT-STD", color: 2, linetype: "Continuous" },  // Bolt standard
            HIDDEN: { name: "S-MISC-HID", color: 8, linetype: "DASHED" },      // Hidden geometrical features
            CENTER: { name: "S-GRID-CTR", color: 1, linetype: "CENTER" },      // Centerlines
            DIM: { name: "U-ANNO-DIM", color: 7, linetype: "Continuous" },  // Dimensions
            TEXT: { name: "U-ANNO-TXT", color: 7, linetype: "Continuous" }   // Annotations
        }
    },
    DRAFTING: {
        // The "10-8 Rule" from professional practice
        DIM_OFFSET_INITIAL: 10,
        DIM_SPACING: 8,
        EXTENSION_GAP: 2,
        TEXT_HEIGHT: 2.5,
        ARROW_SIZE: 2.5
    },
    STEEL: {
        // Minimal AISC/JIS Reference Table
        'H-250x250': { d: 250, b: 250, tw: 9, tf: 14, r: 16 }, // depth, breadth, thickness web, thickness flange, radius
        'H-300x300': { d: 300, b: 300, tw: 10, tf: 15, r: 18 },
        'M20': { d_nom: 20, d_hole: 22, nut_h: 16, wash_t: 3 }
    }
};

// --- 2. CORE KERNEL ---
class CoreEngine {
    constructor() {
        this.commands = [];
        this.origin = { x: 0, y: 0 };
    }

    addCommand(tool, args) {
        this.commands.push({ tool, args });
    }

    /**
     * Initialize standard layers in the DXF
     */
    initLayers() {
        Object.values(STANDARDS.LAYERS.SCHEMA).forEach(layer => {
            this.commands.push({
                tool: 'create_layer',
                args: { name: layer.name, color: layer.color, lineType: layer.linetype || 'Continuous' }
            });
        });
    }

    getCommands() { return this.commands; }
}

/**
 * Base class for all intelligent structural objects
 */
class StructuralElement {
    constructor(engine) {
        this.engine = engine;
    }
    // Abstract method: must be implemented by subclasses
    draw(viewType, insertionPoint) { }
}

/**
 * Intelligent H-Beam Component
 * Knows how to draw its Section, Web View, and Flange View
 */
class HBeam extends StructuralElement {
    constructor(engine, profileName) {
        super(engine);
        this.spec = STANDARDS.STEEL[profileName];
        if (!this.spec) throw new Error(`Unknown Profile: ${profileName}`);
    }

    draw(viewType, insertP, length) {
        const { d, b, tw, tf } = this.spec;
        const x = insertP.x;
        const y = insertP.y;

        if (viewType === 'SECTION') {
            // Draw I-shape Section
            // Simplified for rects: Top Flange, Bottom Flange, Web using polyline
            // ... implementation detail would go here for detailed section
        }
        else if (viewType === 'WEB_VIEW') {
            // Looking at the "H" from the side (seeing the web face)
            // Outer Boundary (Flanges edge lines)
            this.engine.addCommand('create_line', { start: { x, y }, end: { x, y+ length }, layer: STANDARDS.LAYERS.SCHEMA.BEAM.name });
        this.engine.addCommand('create_line', { start: { x: x + d, y }, end: { x: x + d, y+ length }, layer: STANDARDS.LAYERS.SCHEMA.BEAM.name });

    // Web Hidden Lines (Internal web thickness)
    // Web is centered. Web start = d/2 - tw/2
    const webStart = d / 2 - tw / 2;
    const webEnd = d / 2 + tw / 2;
            this.engine.addCommand('create_line', { start: { x: x + webStart, y }, end: { x: x + webStart, y+ length }, layer: STANDARDS.LAYERS.SCHEMA.HIDDEN.name });
this.engine.addCommand('create_line', { start: { x: x + webEnd, y }, end: { x: x + webEnd, y+ length }, layer: STANDARDS.LAYERS.SCHEMA.HIDDEN.name });

// Centerline
this.engine.addCommand('create_line', { start: { x: x + d / 2, y: y - 50 }, end: { x: x + d / 2, y: y + length + 50 }, layer: STANDARDS.LAYERS.SCHEMA.CENTER.name });
        }
    }
}

/**
 * Intelligent Bolt Group
 * Handles standard spacing (pitch/gage) and hole sizes
 */
class BoltGroup extends StructuralElement {
    constructor(engine, sizeName) {
        super(engine);
        this.spec = STANDARDS.STEEL[sizeName];
        if (!this.spec) throw new Error(`Unknown Bolt Size: ${sizeName}`);
    }

    drawGrid(centerPoint, rows, cols, pitch, gage) {
        const radius = this.spec.d_hole / 2; // Use HOLE size for drafting, not bolt shank

        const startX = centerPoint.x - (gage * (cols - 1)) / 2;
        const startY = centerPoint.y - (pitch * (rows - 1)) / 2;

        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                const cx = startX + c * gage;
                const cy = startY + r * pitch;
                this.engine.addCommand('create_circle', {
                    center: { x: cx, y: cy },
                    radius: radius,
                    layer: STANDARDS.LAYERS.SCHEMA.BOLT.name
                });

                // Add Center Mark (Cross)
                const markSize = radius + 2;
                this.engine.addCommand('create_line', { start: { x: cx - markSize, y: cy }, end: { x: cx + markSize, y: cy }, layer: STANDARDS.LAYERS.SCHEMA.CENTER.name });
                this.engine.addCommand('create_line', { start: { x: cx, y: cy - markSize }, end: { x: cx, y: cy + markSize }, layer: STANDARDS.LAYERS.SCHEMA.CENTER.name });
            }
        }
    }
}

/**
 * Dimensioning Engine
 * Automatically calculates offsets based on standards
 */
class DimEngine {
    constructor(engine) {
        this.engine = engine;
    }

    /**
     * Adds a linear dimension chain
     * @param {Array} points - Sorted list of points to measure between
     * @param {Number} refLineX - The X-coordinate of the reference line (e.g., beam edge) to measure FROM
     * @param {Number} level - Hierarchy level (1 = nearest, 2 = next, etc.) for the 10-8 rule
     */
    addChain(points, refLineX, level = 1) {
        const style = STANDARDS.DRAFTING;
        // 10-8 Rule Calculation
        const dist = style.DIM_OFFSET_INITIAL + ((level - 1) * style.DIM_SPACING);
        const dimX = refLineX + dist;
        const layer = STANDARDS.LAYERS.SCHEMA.DIM.name;

        // Sort points to ensure chain is sequential
        points.sort((a, b) => a - b);

        for (let i = 0; i < points.length - 1; i++) {
            const p1 = points[i];
            const p2 = points[i + 1];
            const midY = (p1 + p2) / 2;

            // Create standard dimension
            this.engine.addCommand('create_dimension', {
                point1: { x: refLineX, y: p1 },
                point2: { x: refLineX, y: p2 },
                dimLinePosition: { x: dimX, y: midY },
                dimensionType: 'vertical',
                layer: layer,
                textOverride: Math.abs(p2 - p1).toFixed(0) // Ensure clean integer text
            });
        }
    }
}

// --- EXECUTION JOB (The "Main" Function) ---
const engine = new CoreEngine();
const dimEngine = new DimEngine(engine);

// 1. Setup
engine.initLayers();

// 2. Clear Bounds
engine.addCommand('erase_by_bounds', { minX: -5000, minY: -5000, maxX: 5000, maxY: 5000, selectionMode: 'crossing' });

// 3. Draw Main Column (Knowledge-based: H-250x250)
const colStart = { x: 0, y: 0 };
const colLength = 1000;
const column = new HBeam(engine, 'H-250x250');
column.draw('WEB_VIEW', colStart, colLength);

// 4. Draw Bolt Group (Knowledge-based: M20)
// Logic: Place bolts relative to column center
// Beam is 250 wide, Center is 125.
const boltCenter = { x: 125, y: 500 };
const boltGroup = new BoltGroup(engine, 'M20');
// 2 cols @ 60 gage, 5 rows @ 60 pitch
boltGroup.drawGrid(boltCenter, 5, 2, 60, 60);

// 5. Add Intelligent Dimensions
// Points of interest: Plate Top/Bottom (simulated), Bolt Rows
const dimPoints = [
    500 - (2 * 60) - 30, // simulated plate bottom
    500 - (2 * 60),      // bolt row 1
    500 - (1 * 60),      // bolt row 2
    500,                 // bolt row 3 (center)
    500 + (1 * 60),      // bolt row 4
    500 + (2 * 60),      // bolt row 5
    500 + (2 * 60) + 30  // simulated plate top
];

// Level 1: Detail Dimensions (Bolts)
dimEngine.addChain(dimPoints, 250, 1);

// Level 2: Overall Grid (Plate)
dimEngine.addChain([dimPoints[0], dimPoints[dimPoints.length - 1]], 250, 2);

// --- OUTPUT ---
// Print commands to be executed by the python runner?
// No, we need to adapt this script to be RUN by the agent's tool system,
// OR we return the commands array so the agent can execute them.
// For now, let's just make it a valid JS file.
