#!/usr/bin/env python3
"""
validate_json.py
- usage: python validate_json.py schema.json data.json
"""
import json, sys
try:
    import jsonschema
except ImportError:
    print("jsonschema not installed. pip install jsonschema", file=sys.stderr)
    sys.exit(2)

schema_path, data_path = sys.argv[1], sys.argv[2]
schema = json.load(open(schema_path, "r", encoding="utf-8"))
data = json.load(open(data_path, "r", encoding="utf-8"))
jsonschema.validate(data, schema)
print("OK")
