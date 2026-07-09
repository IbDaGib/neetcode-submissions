class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        n = len(nums3)
        m = n // 2
        if n % 2 == 1:
            return nums3[m]
        else:
            return (nums3[m - 1] + nums3[m]) / 2
