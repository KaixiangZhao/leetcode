from src.datastructure.Interval import Interval


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result, overlap, begin = [], 0, float('-inf')
        for x, y in sorted([(i.start, 1) for i in intervals] + [(i.end, -1) for i in intervals] +
                                   [(newInterval.start, 1), (newInterval.end, -1)], key=lambda x: (x[0], -x[1])):
            if y == 1 and not overlap:
                begin = x
            if y == -1 and overlap == 1:
                result += Interval(begin, x),
            overlap += y
        return result
