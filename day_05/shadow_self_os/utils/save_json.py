import json
def save_json(data, path):
    import os
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as file:
        json.dump(data, file, indent=4)