import re

# takes a split list and cleans out irrelevant data using regex
# and returns a list of tuples (timestame, footage)
def split_log(data):
    cleaned_log = []
    times = []
    lengths = []
    timestamp_pattern = r"^(?:[0-1]?\d|2[0-3]):[0-5]\d$"
    for i in range(len(data) - 1):
        if re.match(timestamp_pattern, data[i]):
            timestamp = data[i]
            footage = data[i+1].strip("'")
            cleaned_log.append((timestamp, footage))
    return cleaned_log
