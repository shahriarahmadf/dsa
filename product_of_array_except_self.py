#1:55\
# 10 mins
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [0]*len(nums)
        total_product = 1
        zero_indices = []

        for index,num in enumerate(nums):
            if num == 0:
                zero_indices.append(index)
            else:
                total_product *= num

        if len(zero_indices) > 1:
            return answer
        elif len(zero_indices) == 1:
            for index,num in enumerate(nums):
                if index == zero_indices[0]:
                    answer[index] = int(total_product)
        else:
            for index,num in enumerate(nums):
                    answer[index] = int(total_product/num)

        return answer