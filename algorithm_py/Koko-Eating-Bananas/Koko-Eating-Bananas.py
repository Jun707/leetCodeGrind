# Brute Force
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        for i in range(1, max(piles)):
            temp = 0
            for j in piles:
                temp += ceil(j/i)
            if temp <= h:
                res = min(i, res)
        return res

# Binary Search
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = max(piles)

        while l <= r:
            m = (l+r)//2
            temp = 0
            for i in piles:
                temp += ceil(i/m)
            if temp > h:
                l = m+1
            elif temp <= h:
                res = min(res, m)
                r = m-1
        return res

