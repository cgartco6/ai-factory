import os
import json


class Storage:

    def save(self, data, filename="output.json"):

        os.makedirs("outputs", exist_ok=True)

        path = f"outputs/{filename}"

        with open(path, "w") as f:
            json.dump(data, f, indent=2)

        return path
