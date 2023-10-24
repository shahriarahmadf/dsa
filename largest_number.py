class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(num1,num2):
            if num1 + num2 > num2 + num1:
                return -1
            else:
                return 1

        # converting each digit from int to str
        for i, n in enumerate(nums):
            nums[i] = str(n)

        # sort the str nums array using defined function compare in key
        nums = sorted(nums, key=cmp_to_key(compare), )

        return str(int("".join(nums)))