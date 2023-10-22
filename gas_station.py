class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return an integer
	def canCompleteCircuit(self, A, B):
		# B - gas cost
		# A - gas available
		if sum(B)>sum(A):
			return -1
		i = 0
		gas = 0
        start = i
		while 1:
			gas += A[i]
			if B[i] <= gas: # go to next station
				gas -= B[i]
                if i == len(A)-1:
                    i = 0
                else:
                    i += 1
                if start == i:
                    return 0 if (i-1)<0 else start
            else: # cannot go next station
                gas = 0
                i += 1
                start = i # initialize new start point
			
		
		