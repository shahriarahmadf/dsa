class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        print(frequency)

        i = 0
        for key,value in frequency.items():
            if value > 2:
                value = 2
            for times in range(value):
                nums[i] = key
                i+=1
        
        return i
            