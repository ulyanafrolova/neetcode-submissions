class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_dict = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in number_dict:
                return [number_dict[x], i]
            else:
                number_dict[nums[i]]=i
        return False