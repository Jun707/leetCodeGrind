class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)-1
        for i in s:
            if i !=s[n]:
                return
            n-=1
        return True