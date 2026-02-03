from split_log import split_log, get_start_index, get_end_index
from analyzer.analyze_time_diff import analyze_time_diff

class TubeLot:
    def __init__(self, heat=None, lot=None, raw=None, json_lot=None):
        if json_lot:
            self._heat = json_lot["heat"]
            self._lot = json_lot["lot"]
            self._raw_data = json_lot["data"]

            self.defects = json_lot["defects"]
            self.groups = json_lot["groups"]

            self.avg_group_length = 0
            self.group_rate = 0
        else:
            self._heat = heat
            self._lot = lot
            self._raw_data = raw

            self.defects = None
            self.groups = None

            self.avg_group_length = 0
            self.group_rate = 0
        
    def __repr__(self):
        return f"Heat#: {self._heat}\nLot#: {self._lot}\nDefects (timestamp, footage):\n{self.defects}\nGroups: ==========\n{self.groups}\nAvg Group Length: {self.avg_group_length}\nGroup Rate: {self.group_rate}\n\n"

    def parse_raw(self, defect_window):
        start = get_start_index(self._raw_data)
        end = get_end_index(self._raw_data)
        self.defects = split_log(self._raw_data[start+1:end])
        self.groups = analyze_time_diff(self.defects, defect_window)

    def to_json(self):
        json_lot = {
            "heat": self._heat,
            "lot": self._lot,
            "data": self._raw_data,
            "defects": self.defects,
            "groups": self.groups
            }
        return json_lot

    def update(self, defect_window):
        self.groups = analyze_time_diff(self.defects, defect_window)
