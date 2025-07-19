# generate_clients.py

import subprocess
from pathlib import Path
import yaml
import json
import re
import shutil
from generate_api_list import generate_api_yaml


def snake_case(s: str) -> str:
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '_', s)
    s = s.strip('_')
    return s


def get_generated_package_name(spec_path: Path) -> str:
    import yaml
    with spec_path.open(encoding="utf-8") as f:
        spec = yaml.safe_load(f)
    title = spec["info"]["title"] + "_client"
    return snake_case(title)


def inject_spec_version(version: str, client_path: Path):
    client_file = client_path / "client.py"
    if not client_file.exists():
        raise FileNotFoundError(f"{client_file} not found.")

    lines = client_file.read_text(encoding="utf-8").splitlines()
    new_lines = []
    inserted = False
    for line in lines:
        new_lines.append(line)
        if not inserted and line.strip().startswith("class Client"):
            new_lines.append(f"    __spec_version__ = {version!r}")
            inserted = True
    client_file.write_text("\n".join(new_lines), encoding="utf-8")
    print(f"Injected __spec_version__ = '{version}' into {client_file}")


def write_config(package_name: str, output_dir: Path):
    config = {
        "package_name": package_name
    }
    config_path = output_dir / "config.json"
    with open(config_path, "w") as f:
        json.dump(config, f)
    return config_path


def generate_clients(api_list_path="api_list.yaml", output_dir="clients"):
    with open(api_list_path, "r") as f:
        api_list = yaml.safe_load(f)

    for api in api_list:
        name = api["name"]
        spec_path = Path(api["spec_path"])
        version = api.get("version", "0.0.0")

        output_path = Path(output_dir) / name
        output_path.mkdir(parents=True, exist_ok=True)

        config_path = write_config(name, output_path)

        subprocess.run([
            "openapi-python-client",
            "generate",
            "--overwrite",
            "--path", str(spec_path),
            "--output-path", str(output_path),
            "--config", str(config_path)
        ], check=True)

        generated_subfolder = output_path / get_generated_package_name(spec_path)

        inject_spec_version(version, generated_subfolder)

        # After openapi-python-client generates to the default folder (from title)
        generated_dirs = [d for d in output_path.iterdir() if d.is_dir() and d.name != '.ruff_cache']
        print(generated_dirs)
        if len(generated_dirs) != 1:
            # raise RuntimeError(f"Expected 1 generated subfolder in {output_path}, found: {generated_dirs}")
            print(f"Generating {api}...")
            print(f"Expected 1 generated subfolder in {output_path}, found: {generated_dirs}")
            print("Now proceed to next API")
            continue

        generated_dir = generated_dirs[0]  # e.g., clients/clinical_trials/ai-factory-product-build-azure-openai

        # Move all files from the generated subfolder up one level
        for item in generated_dir.iterdir():
            shutil.move(str(item), str(output_path))

        # Delete the now-empty subfolder
        generated_dir.rmdir()


if __name__ == "__main__":
    generate_api_yaml("specs")
    generate_clients()
