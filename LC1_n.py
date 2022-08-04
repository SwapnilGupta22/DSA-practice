class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        temp = 0
        for i in range(0, len(nums)):
            temp = target - nums[i]
            if temp in sum_dict.keys():
                return sum_dict[temp], i
            sum_dict[nums[i]] = i