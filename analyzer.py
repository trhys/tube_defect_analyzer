
DEFECT_WINDOW = 2 #minutes

# takes data (a list of tuples (timestamp, footage)) and compares the
# timestamps to group together defects occuring within a specified 
# time window TODO: make configurable for time window :

def cat_time_groups(groups):
    if groups:
        for j in range(len(groups) -1):
            if groups[j]:
                if groups[j][1] == groups[j+1][0]:
                    groups[j].extend(groups[j+1])
                    groups[j+1] = None
        if None in groups:
            while None in groups:
                groups.remove(None)
            groups = cat_time_groups(groups)
        cleaned_groups = []
        seen = []
        for group in groups:
            new_group = []
            for pair in group:
                if pair not in seen:
                    new_group.append(pair)
                    seen.append(pair)
            cleaned_groups.append(new_group)
    return cleaned_groups

def analyze_time_diff(data):
    if len(data) == 0:
        raise ValueError("data should not be empty!")
    groups = []
    for i in range(len(data) -1):
        stamp1, stamp2 = data[i], data[i+1]
        hour1, minute1 = map(int, stamp1[0].split(":"))
        hour2, minute2 = map(int, stamp2[0].split(":"))
        time1 = hour1 * 60 + minute1
        time2 = hour2 * 60 + minute2
        delta_time = time2 - time1 % 1440
        if delta_time <= DEFECT_WINDOW or delta_time >= 1438 - DEFECT_WINDOW:
            groups.append([stamp1, stamp2])
    groups = cat_time_groups(groups)
    return groups
    
