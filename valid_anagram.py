class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        if len(s) != len(t):
            return False

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in range(0,len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1

        if s_dict == t_dict:
            return True
        else:
            return False        