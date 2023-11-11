class Solution:
    def hIndex(self, citations: List[int]) -> int:
        indices = [0]* (len(citations)+1)

        for citation in citations:
            for i in range(1,citation+1):
                if i==len(indices):
                    break
                else:
                    indices[i]+=1
        for i in range(len(indices)-1,-1,-1):
            if indices[i] >= i:
                return i