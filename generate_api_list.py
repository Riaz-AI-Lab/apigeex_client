# generate_api_list.py

import yaml
from pathlib import Path

def load_spec_metadata(spec_path: Path):
    with open(spec_path, "r", encoding="utf-8") as f:
        spec = yaml.safe_load(f)

    name = spec_path.stem
    version = spec.get("info", {}).get("version", "unknown")
    servers = spec.get("servers", [])
    base_url = servers[0]["url"] if servers else "https://example.com"

    return {
        "name": name,
        "base_url": base_url,
        "version": version,
        "spec_path": str(spec_path),
    }

def generate_api_yaml(spec_dir="specs", output_yaml="apigeex_client/data/api_list.yaml"):
    spec_dir = Path(spec_dir)
    entries = []

    for spec_file in spec_dir.glob("*.yaml"):
        entry = load_spec_metadata(spec_file)
        entries.append(entry)

    with open(output_yaml, "w", encoding="utf-8") as f:
        yaml.dump(entries, f, sort_keys=False, default_flow_style=False)

    print(f"Wrote {len(entries)} APIs to {output_yaml}")

if __name__ == "__main__":
    generate_api_yaml("specs")