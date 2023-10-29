class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        hashmap = {}

        s_words = s.split()
        if len(s_words) != len(pattern):
            return False
            
        for i in range(len(s_words)):
            if pattern[i] not in hashmap:
                if s_words[i] not in hashmap.values():
                    hashmap[pattern[i]] = s_words[i]
                else:
                    return False
            
            else:
                if hashmap[pattern[i]] == s_words[i]:
                    continue
                else:
                    return False
        return True