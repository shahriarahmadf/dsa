class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        current_alt = 0
        highest_alt = 0

        for step in gain:
            current_alt += step
            highest_alt = current_alt if current_alt>highest_alt else highest_alt
        return highest_alt