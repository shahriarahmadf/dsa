# 7 mins

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_candy_among_kids = 0
        
        extra_candies_given = []
        extra_candies_make_highest = []

        for kid in candies:
            max_candy_among_kids = max(max_candy_among_kids,kid)
            extra_candies_given.append(kid+extraCandies)
        
        for kid in extra_candies_given:
            if kid >= max_candy_among_kids:
                extra_candies_make_highest.append(True)
            else:
                extra_candies_make_highest.append(False)
        
        return extra_candies_make_highest
