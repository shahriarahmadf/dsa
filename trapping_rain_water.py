# not good solution
class Solution:
    
    def trap(self, height: List[int]) -> int:
        if height is None:
            return 0

        maxLeft = [0]
        maxRight = [0]

        for i in range(1,len(height)-1):
            maxLeft = max(height[i-1],height[i])
            maxRight = max(height[len(height)-i],height[len(height)-i-1])
        print(maxLeft)
        print(maxRight)

# slightly better but still not good enough
class Solution:
    
    def trap(self, height: List[int]) -> int:
        if height is None:
            return 0

        leftMax = 0
        leftMaxArray = [0]

        for i in range(1,len(height)):
            leftMax = max(leftMax,height[i-1])
            leftMaxArray.append(leftMax)

        rightMax = 0
        rightMaxArray = [0]
        for i in range(len(height)-2,-1,-1):
            rightMax = max(rightMax,height[i+1])
            rightMaxArray.append(rightMax)
        rightMaxArray.reverse()
        water = 0
        for i in range(len(leftMaxArray)):
            water += max(0,min(leftMaxArray[i],rightMaxArray[i]) - height[i])
        
        return water
    
# best solution 
class Solution:
    
    def trap(self, height: List[int]) -> int:
        if height is None:
            return 0
        leftMax = 0
        leftMaxArray = [0]
        for i in range(1,len(height)):
            leftMax = max(leftMax,height[i-1])
            leftMaxArray.append(leftMax)
        rightMax = 0
        rightMaxArray = [0]
        for i in range(len(height)-2,-1,-1):
            rightMax = max(rightMax,height[i+1])
            rightMaxArray.append(rightMax)
        rightMaxArray.reverse()
        water = 0
        for i in range(len(leftMaxArray)):
            water += max(0,min(leftMaxArray[i],rightMaxArray[i]) - height[i])
        return water