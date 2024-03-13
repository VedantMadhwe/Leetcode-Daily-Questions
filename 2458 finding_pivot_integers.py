class Solution:
    def pivotInteger(self, n: int) -> int:
        leftvalue, rightvalue = 1, n 
        if n==1: return n
        leftsum , rightsum = leftvalue , rightvalue
        while leftvalue<rightvalue:
            if leftsum< rightsum:
                leftvalue+=1
                leftsum += leftvalue
            else:
                rightvalue -= 1
                rightsum += rightvalue
            if leftsum == rightsum and leftvalue+1 == rightvalue-1:
                return leftvalue+1
        return -1
