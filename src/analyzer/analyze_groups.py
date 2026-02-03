from tube_lot import TubeLot

# takes tube lot and returns percentage of defects that occur in
# defect group window
def get_avg_group(lot):
    num_defects = len(lot.defects)
    num_groups = len(lot.groups)

    group_lengths = []
    num_grouped_defects = 0
    for group in lot.groups:
        group_size = len(group)
        group_lengths.append(group_size)
        num_grouped_defects += group_size
    
    if group_lengths:
        avg_group_length = sum(group_lengths) / len(group_lengths)    # average length of defect grouping 
    else:
        raise ValueError("cannot analyze group of zero!")

    if num_grouped_defects > 0:
        avg_group_rate = num_defects / num_grouped_defects            # rate of defects that are grouped
    else:
        raise ValueError("cannot analyze group of zero!")

    return avg_group_length, avg_group_rate

# takes list of lots and returns total number of defects and groups
def get_totals(lots):
    total_defects = 0
    total_groups = 0
    group_lengths = []
    total_grouped_defects = 0
    for lot in lots:
        total_defects += len(lot.defects)
        total_groups += len(lot.groups)
        for group in lot.groups:
            group_size = len(group)
            group_lengths.append(group_size)
            total_grouped_defects += group_size
    total_group_length = sum(group_lengths)
    return total_defects, total_groups, total_group_length, total_grouped_defects
