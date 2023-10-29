from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        def find_min_difference(indices,k):
            current = indices[0]
            for i in range(1,len(indices)):
                diff = abs(indices[i]-current)
                if diff <= k:
                    return True
                current = indices[i]
            return False

        hashmap = defaultdict(list)

        for index,num in enumerate(nums):
            hashmap[num].append(index)

        for indices in hashmap.values():
            if len(indices)>0:
                ans = find_min_difference(indices,k)

                if ans == True:
                    return ans


            