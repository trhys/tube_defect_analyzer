import argparse
from ocr_read import ocr_read

def main():
    parser = argparse.ArgumentParser(
                prog="tube-defect-analyzer",
                description="read file from ocr and analyze defect rates"
            )
    parser.add_argument('filepath')
    args = parser.parse_args()
    if args.filepath is None:
        raise Exception("ERROR: failed to parse argument: filepath")

    ocr_read(args.filepath)

if __name__ == "__main__":
    main()
