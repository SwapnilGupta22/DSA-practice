class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum, ans = 0, 0
        flag = True
        for i in range(0, len(nums)):
            if nums[i] >= 0:
                flag = False

        if(flag):
            return max(nums)
            
        for i in nums:

            currsum = currsum + i
            if currsum < 0:
                currsum = 0
                continue
            ans = max(ans,currsum)
        
        return ans