class Solution:
    def __init__(self):
        self.result = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(1,n,k,[])
        return self.result
    
    def backtrack(self,start,n,k,combination):
        if len(combination) == k:
            self.result.append(combination[:])
            return

        for i in range(start,n+1):
            self.backtrack( i+1 ,n, k , combination + [i])
