from paddleocr import PaddleOCR
import argparse

def ocr_read(filepath):
    ocr = PaddleOCR(lang='en')
    result = ocr.predict(filepath)

    for line in result:
        line.print()

def main():
    parser = argparse.Parser(
                prog="tube-defect-analyzer",
                description="read file from ocr and analyze defect rates"
            )
    parser.add_Argument(filepath, required=True)
    args = parser.parse_args()

    ocr_read(args.filepath)

if __name__ == "__main__":
    main()
