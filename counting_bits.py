# O(n) solution
class Solution:       
    def countBits(self, n: int) -> List[int]:

        dp = [0] * (n+1)
        offset = 1

        for i in range(1,n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp

# O(nlogn)
class Solution:
    def countBits(self, n: int) -> List[int]:

        hammingWeights = [0]
        if n == 0:
            return hammingWeights

        for i in range(1,n+1):
            count = 0
            while i > 0:
                count += i % 2
                i = i // 2
            hammingWeights.append(count)
        
        return hammingWeights