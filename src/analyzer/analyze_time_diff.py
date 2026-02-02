
DEFECT_WINDOW = 2 #minutes

# takes data (a list of tuples (timestamp, footage)) and compares the
# timestamps to group together defects occuring within a specified 
# time window TODO: make configurable for time window :

def analyze_time_diff(data):
    if data is None:
        return None
    if len(data) == 0:
        raise ValueError("data should not be empty!")
    groups = []
    current = []
    for i in range(len(data) -1):
        stamp1, stamp2 = data[i], data[i+1]
        hour1, minute1 = map(int, stamp1[0].split(":"))
        hour2, minute2 = map(int, stamp2[0].split(":"))
        time1 = hour1 * 60 + minute1
        time2 = hour2 * 60 + minute2
        delta_time = (time2 - time1) % 1440
        if delta_time <= DEFECT_WINDOW or delta_time >= 1440 - DEFECT_WINDOW:
            if current:
                current.append(stamp2)
            else:
                current = [stamp1, stamp2]
        else:
            if len(current) > 1:
                groups.append(current)
            current = []
    if len(current) > 1:
        groups.append(current)
    return groups
    
