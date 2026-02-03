from paddleocr import PaddleOCR
from split_log import get_lot#split_log, get_lot, get_end_index, get_start_index
#from analyzer.analyze_time_diff import analyze_time_diff
from tube_lot import TubeLot

def ocr_read(filepath):
    ocr = PaddleOCR(text_rec_score_thresh=0.6, lang='en')
    results = ocr.predict(filepath)

    tube_lots = []
    for line in results:    
        data = line["rec_texts"]
        #print("RAW OCR LINES:")
        #print(data)
        #print(f"SAVING TO JSON AT: {os.path.join('tests/', filepath)}")
        #line.save_to_json(os.path.join('tests/', os.path.basename(filepath)))

        heat, lot = get_lot(data)
        tube_lot = TubeLot(heat, lot, data)
        tube_lots.append(tube_lot)
    return tube_lots
        #index_start = get_start_index(data)
        #index_end = get_end_index(data)

        #tube_lot.parse_raw(index_start, index_end)
        #print(tube_lot)
