from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        freq = defaultdict(int)
        for edge in edges:
            freq[edge[0]] += 1
            freq[edge[1]] += 1
        most_common = max(freq, key = lambda k: freq[k])

        return most_common