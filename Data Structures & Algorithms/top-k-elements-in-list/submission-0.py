class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = {}
        for i in nums:
            if i in dict_nums:
                dict_nums[i]+=1
            else:
                dict_nums[i]=1
        result = dict(sorted(dict_nums.items(), key=lambda item: item[1], reverse=True))
        return list(result.keys())[:k]