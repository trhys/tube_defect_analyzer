import argparse
import json
from ocr_read import ocr_read
from analyzer.analyze_lots import analyze
from analyzer.gen_report import gen_report, save_report
from serialization import save_to_json, load_from_json

def main():
    parser = argparse.ArgumentParser(
                prog="tube-defect-analyzer",
                description="read file from ocr and analyze defect rates"
            )
    parser.add_argument('filepath')
    parser.add_argument('-j', '--j', '--json', dest="json", help='load tube lots from json. requires [filepath] to be json file', action='store_true')
    parser.add_argument('-r', '--r', '--rate', dest="rate", help='set the defect window used by the analyzer. default is 2 minutes', type=int, default=2)
    parser.add_argument('-u', '--u', '--update', dest="update", help='update lot groups when loading from json. this catches edits made on the serialized data, as well as adjusted defect window.', action='store_true')
    args = parser.parse_args()

    if args.filepath is None:
        raise Exception("ERROR: failed to parse argument: filepath")

    if args.json:
        with open(args.filepath, "r") as f:
            lots = load_from_json(json.load(f))
            for lot in lots:
                if args.update:
                    lot.update(args.rate)
                analyze(lot)
            f.close()
    else:
        lots = ocr_read(args.filepath)
        for lot in lots:
            lot.parse_raw(args.rate)
            analyze(lot)

    save_to_json(lots, args.filepath)
    save_report(gen_report(lots, args.rate))
    
if __name__ == "__main__":
    main()
