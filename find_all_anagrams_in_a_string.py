class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import defaultdict
        
        # output array
        anagram_index = []

        # if p (small string) > s
        if (len(p)>len(s)):
            return anagram_index

        # finding small string map
        small_string_map = defaultdict(int)
        for x in p:
            small_string_map[x] += 1

        # window slider subarray map
        substring_map = defaultdict(int)

        # window slider base case
        for i in range(len(p)):
            substring_map[s[i]] += 1

        # check if anagram for base case
        if substring_map == small_string_map:
            anagram_index.append(0)

        # other cases: looping from 1
        for i in range( 1, len(s)-len(p)+1 ):

            # deleting left most character from substring map
            left_most_char = s[i-1]
            substring_map[left_most_char] -= 1
            # deleting if left most key is empty value = 0
            if substring_map[left_most_char] == 0:
                del substring_map[left_most_char]

            # adding right most character to substring map
            right_most_char = s[i+len(p)-1]
            substring_map[right_most_char] += 1       

            # check if anagram
            if (substring_map == small_string_map):
                anagram_index.append(i)
        return anagram_index

