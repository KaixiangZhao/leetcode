class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total, min, start = 0, float('inf'), 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < min:
                min = total
                start = i + 1
        return -1 if total < 0 else start % len(gas)
