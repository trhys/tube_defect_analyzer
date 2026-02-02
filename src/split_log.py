import re

# takes a split list and cleans out irrelevant data using regex
# and returns a list of tuples (timestame, footage)
def split_log(data):
    cleaned_log = []
    times = []
    lengths = []
    timestamp_pattern = r"(?i)\b(\d{1,2}[:;][0-5]\d)[a-z]*"
    for i in range(len(data) - 1):
        match = re.match(timestamp_pattern, data[i].replace(" ", ""))
        if match:
            timestamp = clean_timestamp(match.group(1))
            footage = data[i+1].strip("'")
            cleaned_log.append((timestamp, footage))
    return cleaned_log

# takes raw timestamp and cleans up any misreading from ocr
def clean_timestamp(time):
    time = time.replace(" ", "").replace(";", ":")
    hour, minute = time.split(":")
    if int(hour) > 23:
        hour = hour.replace("8", "0")
        hour = hour.replace("5", "1")
        hour = hour.replace("9", "1")
    if int(minute) > 59:
        minute = minute.replace("8", "0")
        minute = minute.replace("6", "0")
        minute = minute.replace("9", "1")
    return f"{hour.zfill(2)}:{minute.zfill(2)}"

# gets heat number and lot number from raw data
# returns HEAT, LOT
def get_lot(data):
    heat_pattern = r"(?i)(?:R#)?\s*(\d{6}-\d{3})"
    lot_pattern = r"(?i)Lot[-\#\s]\s*(\d+)"
    heat = None
    lot = None
    for line in data:
        heat_match = re.match(heat_pattern, line)
        lot_match = re.match(lot_pattern, line)
        if heat_match:
            heat = heat_match.group(1)
        if lot_match:
            lot = lot_match.group(1)
    return heat, lot

# gets the appropriate end index for data slicing
def get_end_index(data):
    for index, line in enumerate(data):
        match = re.match(r"(?i)Total[:=-]?\s*", line)
        if match:
            return index
    return len(data)

# get start index
def get_start_index(data):
    rf_pattern = r"Roll Footage"
    rn_pattern = r"R#"
    for index, line in enumerate(data):
        match_rf = re.match(rf_pattern, line)
        match_rn = re.match(rn_pattern, line)
        if match_rf or match_rn:
            return index
    return 0
