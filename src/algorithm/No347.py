class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        _dict={}
        for i in nums:
            if i not in _dict:
                _dict[i]=1
            else:
                _dict[i]+=1
        _dict=sorted(_dict.items(),key=lambda x: x[1],reverse=True)
        result=[]
        for i in range(k):
            result.append(_dict[i][0])
        return result
