import argparse
import json
from ocr_read import ocr_read
from analyzer.analyze_lots import analyze
from serialization import save_to_json, load_from_json

def main():
    parser = argparse.ArgumentParser(
                prog="tube-defect-analyzer",
                description="read file from ocr and analyze defect rates"
            )
    parser.add_argument('filepath')
    parser.add_argument('-j', '--j', '--json', dest="json", help='load tube lots from json. requires [filepath] to be json file', action='store_true')
    args = parser.parse_args()

    if args.filepath is None:
        raise Exception("ERROR: failed to parse argument: filepath")

    if args.json:
        with open(args.filepath, "r") as f:
            lots = load_from_json(json.load(f))
            for lot in lots:
                analyze(lot)
                print(lot._raw_data)
                print(lot)
    else:
        lots = ocr_read(args.filepath)
        for lot in lots:
            lot.parse_raw()
            analyze(lot) 
            print(lot._raw_data)
            print(lot)
        save_to_json(lots)
    
if __name__ == "__main__":
    main()
