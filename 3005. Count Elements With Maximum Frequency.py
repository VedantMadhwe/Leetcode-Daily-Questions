class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        #making a freq array as array will take less time here(bcoz of limited constraints) than dictionary/hashmaps.
        freq_arr = [0]*101
        currf,maxf,sumf = 0,0,0
        for element in nums:
            freq_arr[element]+=1
            currf = freq_arr[element]
            # a new answer
            if currf>maxf:
                maxf = currf
                sumf = currf
            elif currf == maxf:
                sumf+=currf

        return sumf

