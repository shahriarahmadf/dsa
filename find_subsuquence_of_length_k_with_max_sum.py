
# my first solution but does not pass all test cases due to time limit exceed
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        indexed_nums = list(enumerate(nums))
 
        sorted_nums = sorted(indexed_nums, key=lambda x: x[1])

        output = []
        for i in range(len(sorted_nums)-k,len(sorted_nums)):
            output.append(sorted_nums[i])
        sorted_output = sorted(output, key=lambda x:x[0])

        final_output = []        
        for i in range(len(sorted_output)):
            final_output.append(sorted_output[i][1])
        return final_output