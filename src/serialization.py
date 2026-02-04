import os
import json
from tube_lot import TubeLot
from tqdm import tqdm

def save_to_json(lots, filepath):
    dest = os.path.join("jobs/", os.path.basename(filepath))
    print(f"Saving JSON to {dest}...")
    json_lots = []
    for lot in tqdm(lots, desc="Converting to JSON", unit="lot"):
        json_lots.append(lot.to_json())
    os.makedirs("jobs/", exist_ok=True)
    with open(dest, "w") as f:
        f.write(json.dumps(json_lots, indent=4))
    f.close()

def load_from_json(json_object):
    print("Loading from JSON...")
    lots = []
    for obj in tqdm(json_object, desc="Converting from JSON", unit="obj"):
        tube_lot = TubeLot(json_lot=obj)
        lots.append(tube_lot)
    return lots
