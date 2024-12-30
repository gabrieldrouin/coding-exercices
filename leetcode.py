from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def t_to_i(tuple_list: List[tuple]) -> List[Interval]:
    return [Interval(start, end) for start, end in tuple_list]
    return [(interval.start, interval.end) for interval in interval_list]

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        

sol = Solution()
sf = t_to_i([(0,30),(5,10),(15,20)])
st = t_to_i([(5,8),(9,15)])
print(sol.canAttendMeetings(sf))
print(sol.canAttendMeetings(st))