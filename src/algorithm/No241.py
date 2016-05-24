class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return self.helper(input, {})

    def helper(self, input, seen):
        if input in seen:
            return seen[input]
        if input.isnumeric():
            return [int(input)]
        res = []
        for i, c in enumerate(input):
            if c in "+-*":
                res += [l+r if c == "+" else l-r if c == "-" else l*r
                            for l in self.helper(input[:i], seen)
                            for r in self.helper(input[i+1:], seen)]
        seen[input] = res
        return res


if __name__ == "__main__":
    print(Solution().diffWaysToCompute("2*3-4*5"))