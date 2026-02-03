from analyzer.analyze_groups import get_avg_group
from tube_lot import TubeLot

def analyze(lot):
    avg_group_length = 0
    group_rate = 0
    if lot.groups:
        avg_group_length, group_rate = get_avg_group(lot)
    lot.avg_group_length = avg_group_length
    lot.group_rate = group_rate
