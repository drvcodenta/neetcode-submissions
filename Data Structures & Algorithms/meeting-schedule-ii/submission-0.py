"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        i = j = 0
        max_day = count = 0
        while (i < len(start)):
            if start[i] < end[j]:
                count = count + 1
                i = i + 1
            else:
                count = count - 1
                j = j + 1
            max_day = max(max_day, count)
        return max_day