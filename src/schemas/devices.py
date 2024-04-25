class DevicesSchema:

    valid_schema_devices = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "deviceId": {"type": "string"},
                "mainDevice": {"type": "boolean"},
                "name": {"type": "string"},
                "registeredAt": {"type": "integer"},
                "devision": {"type": "integer"},
                "prosumer": {"type": "boolean"},
                "manufacturer": {"type": "string"},
                "devisionClass": {"type": "integer"},
                "deprecated": {"type": "boolean"},
                "converterFaktor": {"type": "integer"},
                "rates": {"type": "array"}
            },
        },
        "required": ["deviceId",
                     "mainDevice",
                     "registeredAt",
                     "devision",
                     "prosumer",
                     "manufacturer",
                     "devisionClass",
                     "deprecated",
                     "converterFaktor"]
    }
