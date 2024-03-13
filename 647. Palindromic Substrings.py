def grow(s,left,right,count):
    while left>=0 and right<len(s):
        if s[left] == s[right]:
            count+=1
            left-=1
            right+=1
        else:
            break
    return count
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        left, right = 0,0
        ans = 0
        for i in range(len(s)):
            ans += grow(s,i,i,0)
            ans += grow(s,i,i+1,0)
        return ans
