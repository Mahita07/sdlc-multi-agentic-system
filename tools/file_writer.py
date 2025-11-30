import json
from pathlib import Path
from typing import List, Dict


def create_project_from_json(base_dir: str, project_name: str, files_json: str) -> str:
    print("🚀 TOOL CALLED")
    print("BASE DIR:", base_dir)
    print("PROJECT NAME:", project_name)


    base_path = Path(base_dir).expanduser().resolve()

    if not base_path.exists():
        raise ValueError(f"❌ Invalid base directory: {base_path}")

    if not base_path.is_dir():
        raise ValueError(f"❌ Not a directory: {base_path}")

    project_path = base_path / project_name
    project_path.mkdir(parents=True, exist_ok=True)


    try:
        data = json.loads(files_json)
    except json.JSONDecodeError as e:
        raise ValueError(f"""
❌ INVALID JSON RECEIVED

ERROR:
{str(e)}

PAYLOAD (truncated):
{files_json[:500]}
""")



    files: List[Dict] = []

    if isinstance(data, dict) and "files" in data and isinstance(data["files"], list) and data["files"]:
        files = data["files"]

    elif isinstance(data, dict) and isinstance(data.get("single_file"), str) and data["single_file"].strip():
        files = [{
            "filename": "main.py",
            "code": data["single_file"]
        }]

    else:
        raise ValueError(f"""
❌ INVALID CODE GENERATION FORMAT

Expected one of:

1) {{
      "files": [{{"filename": "...", "code": "..."}}]
   }}

OR

2) {{
      "single_file": "..."
   }}

Received:
{data}
""")


    written_files = []

    for file in files:
        if not isinstance(file, dict):
            raise ValueError(f"Invalid file entry: {file}")

        filename = file.get("filename")
        content = file.get("code") or file.get("test_code")

        if not filename:
            raise ValueError("❌ Missing filename")

        if not content:
            raise ValueError(f"❌ Missing content for {filename}")

        relative = Path(filename)

        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError(f"❌ Illegal filename: {filename}")

        full_path = project_path / relative
        full_path.parent.mkdir(parents=True, exist_ok=True)

        full_path.write_text(content, encoding="utf-8")
        written_files.append(str(full_path))


    return (
        f"✅ Project created / updated at:\n{project_path}\n\n"
        f"✅ Files written:\n" + "\n".join(written_files)
    )
