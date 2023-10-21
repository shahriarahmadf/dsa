class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        import math
        A_list = sorted(A) # converting tuple to array because tuple is immutable
        size = math.floor(len(A_list)/2)
        count = 0
        current = None

        for x in A_list:
            if current != x:
                current = x
                count = 1
            else:
                count += 1
            if count > size:
                return current
            