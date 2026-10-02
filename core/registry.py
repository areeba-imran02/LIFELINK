import json
from pathlib import Path
from .models import Resource

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "demo_resources.json"

def load_resources():
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    return [Resource(**item) for item in data]
