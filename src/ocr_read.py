from paddleocr import PaddleOCR
from split_log import get_lot
from tube_lot import TubeLot
from tqdm import tqdm
from yaspin import yaspin
import time

def ocr_read(filepath):
    ocr = PaddleOCR(
            text_detection_model_name="PP-OCRv5_server_det",
            #text_recognition_model_name="PP-OCRv5_server_rec",
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False,
            text_rec_score_thresh=0.6,
            lang='en'
        )

    with yaspin(text="Running OCR prediction...", color="cyan") as spinner:
        start_time = time.time()
        results = ocr.predict(filepath)
        elapsed_time = time.time() - start_time
        spinner.ok("✓")

    tube_lots = []
    for line in tqdm(results, desc="Generating Lots", unit="line"):    
        data = line["rec_texts"]

        heat, lot = get_lot(data)
        tube_lot = TubeLot(heat, lot, data)
        tube_lots.append(tube_lot)
    return tube_lots
