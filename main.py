from paddleocr import PaddleOCR
import argparse
import os

from split_log import split_log

def ocr_read(filepath):
    ocr = PaddleOCR(text_rec_score_thresh=0.6, lang='en')
    result = ocr.predict(filepath)

    for line in result:
        data = line["rec_texts"]
        print("RAW OCR LINES:")
        print(data)
        print(f"SAVING TO JSON AT: {os.path.join('tests/', filepath)}")
        line.save_to_json(os.path.join('tests/', os.path.basename(filepath)))

        print("BEGINNING LOG SPLITTER")
        index_rf = "Roll Footage"
        index_rn = "R#"
        if index_rf in data:
            split_index = data.index(index_rf)
        elif index_rn in data:
            split_index = data.index(index_rn) + 1
        else:
            raise Exception("ERROR: could not find 'Roll Footage' or 'R#' index. other indices are not currently implemented")
        split_data = split_log(data[split_index+1:])
        print(split_data)

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
