import os
import json
from datetime import datetime
from tube_lot import TubeLot

def save_to_json(lots):
    timestamp = datetime.now().time()
    json_lots = []
    for lot in lots:
        json_lots.append(lot.to_json())
    os.makedirs("jobs/", exist_ok=True)
    with open(os.path.join("jobs/", str(timestamp)), "w") as f:
        f.write(json.dumps(json_lots, indent=4))
    f.close()
