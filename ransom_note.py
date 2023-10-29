from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters_map = defaultdict(int)

        for letter in magazine:
            magazine_letters_map[letter] += 1
        
        for letter in ransomNote:
            if magazine_letters_map[letter] > 0:
                magazine_letters_map[letter] -= 1
            else:
                return False
        return True