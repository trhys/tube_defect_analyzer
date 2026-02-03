import argparse
from ocr_read import ocr_read
from analyzer.analyze_lots import analyze

def main():
    parser = argparse.ArgumentParser(
                prog="tube-defect-analyzer",
                description="read file from ocr and analyze defect rates"
            )
    parser.add_argument('filepath')
    args = parser.parse_args()
    if args.filepath is None:
        raise Exception("ERROR: failed to parse argument: filepath")

    lots = ocr_read(args.filepath)

    for lot in lots:
        lot.parse_raw()
        analyze(lot) 
        print(lot)
    
if __name__ == "__main__":
    main()
