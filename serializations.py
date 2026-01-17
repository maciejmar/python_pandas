def to_json(value):
    # None
    if value is None:
        return "null"

    # Bool
    if isinstance(value, bool):
        return "true" if value else "false"

    # Int / Float
    if isinstance(value, (int, float)):
        return str(value)

    # String
    if isinstance(value, str):
        escaped = (
            value
            .replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("\n", "\\n")
            .replace("\t", "\\t")
        )
        return f'"{escaped}"'

    # List / Tuple
    if isinstance(value, (list, tuple)):
        items = [to_json(item) for item in value]
        return "[" + ", ".join(items) + "]"

    # Dictionary
    if isinstance(value, dict):
        items = []
        for key, val in value.items():
            if not isinstance(key, str):
                raise TypeError("JSON object keys must be strings")
            items.append(f'{to_json(key)}: {to_json(val)}')
        return "{" + ", ".join(items) + "}"

    # Unsupported type
    raise TypeError(f"Type {type(value)} is not JSON serializable")

data_a = {
    "id": 1,
    "name": "Maciej",
    "active": True,
    "scores": [10, 20, 30],
    "profile": {
        "city": "Warsaw",
        "age": None
    }
}
print(to_json(data_a))