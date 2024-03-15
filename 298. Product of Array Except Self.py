def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1]*len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix = prefix * nums[i] #updating the prefix value for next iteration
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] = res[i] * postfix
        postfix = postfix*nums[i] #updating the postfix value for next iteration
    return res