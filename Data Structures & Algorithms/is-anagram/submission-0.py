class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0

        if len(s) != len(t):
            return False
        else:
            s= sorted(s)
            t = sorted(t)

            if s == t:
                return True
            else: 
                return False


        