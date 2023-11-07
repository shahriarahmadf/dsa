# 12:28~40 = 12 mins

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_plants = 0

        if len(flowerbed) == 0:
            if n > 0:
                return False
            else:
                return True
        elif len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n <= 1
            else:
                return n == 0

        for i in range(0,len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            else:
                if i==0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        new_plants += 1

                elif i==len(flowerbed)-1:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        new_plants += 1

                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        new_plants += 1
        
        return new_plants >= n
                    
