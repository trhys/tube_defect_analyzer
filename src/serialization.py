import os
import json
from tube_lot import TubeLot

def save_to_json(lots, filepath):
    dest = os.path.join("jobs/", os.path.basename(filepath))
    json_lots = []
    for lot in lots:
        json_lots.append(lot.to_json())
    os.makedirs("jobs/", exist_ok=True)
    with open(dest, "w") as f:
        f.write(json.dumps(json_lots, indent=4))
    f.close()

def load_from_json(json_object):
    lots = []
    for obj in json_object:
        tube_lot = TubeLot(json_lot=obj)
        lots.append(tube_lot)
    return lots
