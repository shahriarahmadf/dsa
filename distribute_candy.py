class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        A_candies = [1]*len(A)
        for i in range(1,len(A)):
            if A[i-1] < A[i]:
                A_candies[i] = A_candies[i-1]+1
        
        for j in range(len(A)-2,-1,-1):
            if A[j] > A[j+1]:
                A_candies[j] = max(A_candies[j],A_candies[j+1]+1) 
        s = sum(A_candies)
        return s