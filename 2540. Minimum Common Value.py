class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[-1]<nums2[0]:
            return -1
        else:
            for num in nums1:
                if num in nums2:
                    return num
            return -1