import os
import json
from datetime import datetime
from tube_lot import TubeLot
from analyzer.analyze_groups import get_totals

def gen_report(lots, defect_window):
    if not lots:
        return None
    num_lots = len(lots)
    total_defects, total_groups, total_group_length, total_grouped_defects = get_totals(lots)
    avg_defects_per_lot = total_defects / num_lots
    avg_groups_per_lot = total_groups / num_lots
    avg_group_length = total_group_length / total_groups
    group_rate = total_grouped_defects / total_defects
    return {
            'total_lots': num_lots,
            'total_defects': total_defects,
            'total_groups': total_groups,
            'avg_defects_per_lot': avg_defects_per_lot,
            'avg_groups_per_lot': avg_groups_per_lot,
            'avg_group_length': avg_group_length,
            'group_rate': group_rate,
            'defect_window': defect_window
            }

def save_report(report):
    output = f"""
This report is an analysis of the provided defect logs regarding the defect rates, especially in relation to the proximity of defects with respect to time and footage.
============================================================================================================================
Total Lots: {report['total_lots']}
Total Number of Defects: {report['total_defects']}
Total Number of Groupings * : {report['total_groups']} 

Average Defects per Lot: {report['avg_defects_per_lot']}
Average Groupings per Lot: {report['avg_groups_per_lot']}

Average Group Length: {report['avg_group_length']}
Group Rate * *: {report['group_rate']}

* grouping is defined as a sequence of defects that occur within a specified defect window. Defect window for this report is: [[ {report['defect_window']} minutes ]]

* * group rate is defined as the number of grouped defects divided by the number of total defects. This gives a ratio describing the rate of defects that occur in immediate sequence, determined by defect window.
"""
    os.makedirs("reports/metadata", exist_ok=True)
    #timestamp = str(datetime.now().time()).replace(":", "-").replace(".", "-")
    filename = input("Enter save filename: ")
    dest = os.path.join("reports/", f"{filename}.md")
    print(f"Saving report to {dest}...")
    with open(dest, "w") as f:
        f.write(output)
        f.close()
    dest_json = os.path.join("reports/metadata", f"{filename}.json")
    print(f"Saving metadata to {dest_json}...")
    with open(dest_json, "w") as f:
        f.write(json.dumps(report, indent=4))
        f.close()
