class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        hashmap = {}

        for num in arr:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        frequency = []
        frequency_set = set()
        for value in hashmap.values():
            frequency.append(value)
            frequency_set.add(value)
        
        return len(frequency) == len(frequency_set)
