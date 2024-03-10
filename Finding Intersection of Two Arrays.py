class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        if len(nums1)<len(nums2):
            for num in nums1:
                if num in nums2 and num not in result:
                    result.append(num)
            return result
        else:
            for num in nums2:
                if num in nums1 and num not in result:
                    result.append(num)
            return result
        return result