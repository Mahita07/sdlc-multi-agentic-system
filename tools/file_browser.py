from pathlib import Path

def list_files(base_path: str) -> list:
    p = Path(base_path).expanduser().resolve()

    if not p.exists() or not p.is_dir():
        return []

    return [str(f.relative_to(p)) for f in p.rglob("*") if f.is_file()]