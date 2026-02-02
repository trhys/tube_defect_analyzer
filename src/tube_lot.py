from split_log import split_log
from analyzer.analyze_time_diff import analyze_time_diff

class TubeLot:
    def __init__(self, heat, lot, raw):
        self._heat = heat
        self._lot = lot
        self._raw_data = raw

        self._defects = None
        self._groups = None
        
    def __repr__(self):
        return f"Heat#: {self._heat}\nLot#: {self._lot}\nDefects (timestamp, footage):\n===========\n{self._defects}\nGroups: ==========\n{self._groups}"

    def parse_raw(self, index, end):
        self._defects = split_log(self._raw_data[index+1:end])
        self._groups = analyze_time_diff(self._defects)
