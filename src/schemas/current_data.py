class CurrentDataSchema:

    valid_schema_current_data = {
        "type": "object",
        "properties": {
            "valid": {"type": "boolean"},
            "timestamp": {"type": "integer"},
            "watt": {"type": "integer"},
            "min": {"type": "integer"},
            "max": {"type": "integer"},
            "avg": {"type": "integer"}
        },
        "required": ["valid", "timestamp", "watt", "min", "max", "avg"]
    }
