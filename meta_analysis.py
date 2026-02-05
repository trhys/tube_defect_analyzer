import os
import json
import argparse

parser = argparse.ArgumentParser(
        prog="defect-report-meta-analzyer",
        description="provides analysis of result deltas from tube defect analyses"
    )
parser.add_argument('path1', help='path to unedited report')
parser.add_argument('path2', help='path to final/edited report')
args = parser.parse_args()

def analyze(raw_report, edited_report):
    with open(raw_report, "r") as r:
        results_raw = json.load(r)
        r.close()
    with open(edited_report, "r") as e:
        results_edited = json.load(e)
        e.close()

    dt_total_num_defects = results_edited["total_defects"] - results_raw["total_defects"]
    dt_total_num_groups = results_edited["total_groups"] - results_raw["total_groups"]
    dt_avg_defects = results_edited["avg_defects_per_lot"] - results_raw["avg_defects_per_lot"]
    dt_avg_groups = results_edited["avg_groups_per_lot"] - results_raw["avg_groups_per_lot"]
    dt_avg_group_len = results_edited["avg_group_length"] - results_raw["avg_group_length"]
    dt_group_rate = results_edited["group_rate"] - results_raw["group_rate"]

    pcnt_1 = abs(dt_total_num_defects / results_edited["total_defects"]) * 100
    pcnt_2 = abs(dt_total_num_groups /results_edited["total_groups"]) * 100
    pcnt_3 = abs(dt_avg_defects / results_edited["avg_defects_per_lot"]) * 100
    pcnt_4 = abs(dt_avg_groups / results_edited["avg_groups_per_lot"]) * 100
    pcnt_5 = abs(dt_avg_group_len / results_edited["avg_group_length"]) * 100
    pcnt_6 = abs(dt_group_rate / results_edited["group_rate"]) * 100

    scores = [pcnt_1, pcnt_2, pcnt_5, pcnt_6]
    confidence = sum(scores) / len(scores)

    output = f"""
FIRST RUN (UNEDITED) :
    {results_raw}

=========================================
=========================================

SECOND RUN (EDITED) :
    {results_edited}

=========================================

COMPARISON:                                      PERCENT DROP    CONFIDENCE
dt_total_num_defects: {dt_total_num_defects}    | {pcnt_1:.2f}% | {(100.00 - pcnt_1):.2f}%
dt_total_num_groups: {dt_total_num_groups}      | {pcnt_2:.2f}% | {(100.00 - pcnt_2):.2f}%
dt_avg_defects: {dt_avg_defects}                | {pcnt_3:.2f}% | {(100.00 - pcnt_3):.2f}%
dt_avg_groups: {dt_avg_groups}                  | {pcnt_4:.2f}% | {(100.00 - pcnt_4):.2f}%
dt_avg_group_len: {dt_avg_group_len}            | {pcnt_5:.2f}% | {(100.00 - pcnt_5):.2f}%
dt_group_rate: {dt_group_rate}                  | {pcnt_6:.2f}% | {(100.00 - pcnt_6):.2f}%

AVG CONFIDENCE = [[ {((pcnt_1 + pcnt_2 + pcnt_5 + pcnt_6) / 4):.2f}% ]]
"""
    filename = input("Enter new file name: ")
    os.makedirs("reports/metadata/", exist_ok=True)
    dest = os.path.join("reports/metadata", filename)
    print(f"Saving metadata analysis to {dest}...")
    with open(dest, "w") as f:
        f.write(output)
        f.close()
    print("Job complete. Results:\n\n")
    print(output)


analyze(args.path1, args.path2)
