# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
class Solution:

    def guessNumber(self, n: int) -> int:
        lower_limit = 1
        upper_limit = n
        while True:
            mid = (upper_limit+lower_limit)//2
            result = guess(mid)
            if result == 0:
                break
            elif result == -1:
                upper_limit = mid - 1
            else:
                lower_limit = mid + 1
        return mid