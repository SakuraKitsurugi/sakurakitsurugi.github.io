import requests
import json
from pathlib import Path

# Path to your mods data folder
mods_folder = Path(__file__).parent

# Loop over all JSON files in the folder
for mod_file in mods_folder.glob("*.json"):
    mod_id = mod_file.stem.split("_")[0]  # filename without extension, used as mod ID
    api_url = f"https://mods.vintagestory.at/api/mod/{mod_id}"

    try:
        r = requests.get(api_url, timeout=10)
        r.raise_for_status()
        data = r.json()

        # Extract fields you care about
        mod_info = {
            "id": mod_id,
            "mod_url": "https://mods.vintagestory.at/show/mod/"
            + str(data["mod"]["assetid"]),
            "name": data["mod"]["name"],
            "version": data["mod"]["releases"][0]["modversion"],
        }

        # Write back to the same JSON file
        with open(mod_file, "w", encoding="utf-8") as f:
            json.dump(mod_info, f, indent=2, ensure_ascii=False)

        print(f"Updated mod {mod_id}: {mod_info['version']}")

    except Exception as e:
        print(f"Failed to update mod {mod_id}: {e}")
