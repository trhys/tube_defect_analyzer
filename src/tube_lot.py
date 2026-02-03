from split_log import split_log, get_start_index, get_end_index
from analyzer.analyze_time_diff import analyze_time_diff

class TubeLot:
    def __init__(self, heat, lot, raw):
        self._heat = heat
        self._lot = lot
        self._raw_data = raw

        self.defects = None
        self.groups = None

        self.avg_group_length = None
        self.group_rate = None
        
    def __repr__(self):
        return f"Heat#: {self._heat}\nLot#: {self._lot}\nDefects (timestamp, footage):\n===========\n{self.defects}\nGroups: ==========\n{self.groups}\nAvg Group Length: {self.avg_group_length}\nGroup Rate: {self.group_rate}"

    def parse_raw(self):
        start = get_start_index(self._raw_data)
        end = get_end_index(self._raw_data)
        self.defects = split_log(self._raw_data[start+1:end])
        self.groups = analyze_time_diff(self.defects)
