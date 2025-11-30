from pathlib import Path

def read_file(path: str) -> str:
    p = Path(path).expanduser().resolve()

    if not p.exists():
        raise ValueError(f"File does not exist: {p}")

    if not p.is_file():
        raise ValueError(f"Not a file: {p}")

    return p.read_text(encoding="utf-8")
