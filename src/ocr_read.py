from paddleocr import PaddleOCR
from split_log import get_lot
from tube_lot import TubeLot

def ocr_read(filepath):
    ocr = PaddleOCR(text_rec_score_thresh=0.6, lang='en')
    results = ocr.predict(filepath)

    tube_lots = []
    for line in results:    
        data = line["rec_texts"]

        heat, lot = get_lot(data)
        tube_lot = TubeLot(heat, lot, data)
        tube_lots.append(tube_lot)
    return tube_lots
