class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        current_max=1
        max_len = 0
        nums_seen = sorted(set(nums))
        print(nums_seen)
        for i in nums_seen:
            if max_len<current_max:
                max_len=current_max
            if i+1 in nums_seen:
                current_max+=1
            else:
                current_max=1
        return max_len