class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.s1 = sorted(s)
        self.t1 = sorted(t)
        if self.s1 == self.t1:
            return True
        else:
            return False


handle = Solution()
s = "racecar"
t = "carrace"
print(handle.isAnagram(s,t))