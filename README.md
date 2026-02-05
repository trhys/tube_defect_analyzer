# Overview

This is simple defect analysis tool designed for our in house defect logging. I've set up PaddleOCR to handle text detection and recognition, which is used to populate the tubing lots for analysis.

Key Metrics:
- Total Defects
- Total Groups
- Average defects/lot
- Average groups/lot
- Average group length
- Group Rate (percent of defects that occur in a grouping)


For the purposes of this defect study, a grouping is defined as a sequence of defects whose timestamp is within the defect window. The defect window is a number of minutes defined at the command line by the --rate flag (default: 2 minutes)

I've also included a meta analysis script that is used to track confidence ratings on reported metrics. This compares first pass reports to final pass and subtracts the delta from the confidence percentage.

# Usage

Assuming you are using uv for the virtual env :

```uv run src/main.py [FILEPATH]``` - where filepath is the path to an image file containing defect logs

The output will generate 3 files:
- jobs/FILEPATH.json
- reports/USERINPUT
- reports/metadata/USERINPUT.json

where USERINPUT is prompted at the command line when the program saves it's output.

The JSON files contain the lot data (jobs) and the report data (reports/metadata). The jobs file can be edited manually and then re-analyzed with the command:

```uv run src/main.py [FILEPATH] -jd``` - where [FILEPATH] is the path to the jobs/.json file

The -j flag (-j, --j, --json) is used to load data from a JSON file at FILEPATH.
The -d flag (-d, --d, --hard) forces lots to reparse raw data. This is used after editing the jobs/.json file in order to repopulate the defects and groups. Alternatively, you can edit the defects and groups themselves (as opposed to the "data" key) and use the
(-u, --u, --update) flag to re-run analysis without reparsing the data.

The --rate flat (-r, --r, --rate) is used as: --rate 10 

This specifies a defect window of 10 minutes (default 2)

# Reporting

Reports are saved at reports/USERINPUT. This will give you all the key metrics listed at the top of the page. For meta analysis including confidence scores, use the meta analysis script at the root of the project.

## Example

```
This report is an analysis of the provided defect logs regarding the defect rates,
especially in relation to the proximity of defects with respect to time and footage.
============================================================================================================================
Total Lots: 20
Total Number of Defects: 77
Total Number of Groupings*: 9 

Average Defects per Lot: 3.85
Average Groupings per Lot: 0.45

Average Group Length: 3.0
Group Rate**: 0.35064935064935066

* grouping is defined as a sequence of defects that occur within a specified defect window. Defect window for this report is: 2 minutes

** group rate is defined as the number of grouped defects divided by the number of total defects. This gives a ratio describing the rate of defects that occur in immediate sequence, determined by defect window.
```

# Meta Analysis

From the project root:

```python3 meta_analysis.py [PATH TO FIRST REPORT] [PATH TO SECOND REPORT]``` - where the paths are to the reports/metadata/.json files for your job.

This will compare the results of each analysis and take the delta for each metric and convert to a confidence rating. The confidence score is a percentage of drift from real values for each metric.

## Example

```
FIRST RUN (UNEDITED) :
    {'total_lots': 1, 'total_defects': 3, 'total_groups': 1, 'avg_defects_per_lot': 3.0, 'avg_groups_per_lot': 1.0, 'avg_group_length': 2.0, 'group_rate': 0.6666666666666666, 'defect_window': 2}

=========================================
=========================================

SECOND RUN (EDITED) :
    {'total_lots': 1, 'total_defects': 5, 'total_groups': 1, 'avg_defects_per_lot': 5.0, 'avg_groups_per_lot': 1.0, 'avg_group_length': 2.0, 'group_rate': 0.4, 'defect_window': 2}

=========================================

COMPARISON:                                      PERCENT DROP    CONFIDENCE
dt_total_num_defects: 2    | 40.00% | 60.00%
dt_total_num_groups: 0      | 0.00% | 100.00%
dt_avg_defects: 2.0                | 40.00% | 60.00%
dt_avg_groups: 0.0                  | 0.00% | 100.00%
dt_avg_group_len: 0.0            | 0.00% | 100.00%
dt_group_rate: -0.2666666666666666                  | 66.67% | 33.33%

AVG CONFIDENCE = [[ 26.67% ]]
```
