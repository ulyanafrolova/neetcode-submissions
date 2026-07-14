class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target_sum = (1+len(nums))*(len(nums))//2
        current_sum = 0
        for i in nums:
            current_sum+=i
        return target_sum - current_sum