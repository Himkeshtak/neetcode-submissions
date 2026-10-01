"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
        intervals.sort(key = lambda i : i.start)
        res = 1
        prevend = [intervals[0].end]

        for i in range(1, len(intervals)):
            if intervals[i].start < prevend[0]:
                res += 1
                heapq.heappush(prevend, intervals[i].end)
            else:
               heapq.heapreplace(prevend, intervals[i].end)
        return res
