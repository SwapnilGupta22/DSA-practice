class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1) - 1, -1, -1):
            if nums1[i] == 0 and n > 0:
                nums1[i] = nums2[n-1]
                n = n - 1
        nums1.sort()