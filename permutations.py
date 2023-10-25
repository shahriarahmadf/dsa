class Solution:
    def __init__(self):
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums,[]) 
        return self.result
    
    def backtrack(self,nums,current_perm):
        if not nums: # when no element in nums remaining 
            self.result.append(current_perm) # append the current permutation to result
            return
        for x in range(len(nums)): # for every element in nums
            self.backtrack(nums[:x]+nums[x+1:], current_perm+[nums[x]])
            # (rest of elements in nums except x, add current element x in current permuation)
