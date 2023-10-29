class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letter_map = {}

        for i in range(len(s)):
            if s[i] not in letter_map:
                if t[i] not in letter_map.values():
                    letter_map[s[i]] = t[i]
                else:
                    return False
            else:
                if letter_map[s[i]] == t[i]:
                    continue
                else:
                    return False
        return True
        