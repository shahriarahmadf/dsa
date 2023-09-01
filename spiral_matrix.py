class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        bottom = len(matrix)
        right = len(matrix[0]) if bottom > 0 else 0
        left = 0
        top = 0
        count = len(matrix)*len(matrix[0])
        while (count>0):
            print('running')
            # go left to right / col increase
            for i in range(left,right,1):
                output.append(matrix[top][i])
                count-=1
            top += 1
            if (count==0):
                break
            # go top to bottom / row increase
            for i in range(top,bottom,1):
                output.append(matrix[i][right-1])
                count-=1
            right -= 1
            if (count==0):
                break
            # go right to left / col decrease
            for i in range(right,left,-1):
                output.append(matrix[bottom-1][i-1])
                count-=1
            bottom -=1
            if (count==0):
                break
            # go bottom to top / row decrease
            for i in range(bottom,top,-1):
                output.append(matrix[i-1][left])
                count-=1
            left += 1
            if (count==0):
                break
        return output