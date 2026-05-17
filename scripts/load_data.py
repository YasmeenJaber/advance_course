from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR.parent / "raw_data" / "sales.csv"

with open(
    
    file_path) as f:
    data = f.read()