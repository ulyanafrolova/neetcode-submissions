class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = set(nums)
        if len(unique_numbers) == len(nums):
            return False
        return True