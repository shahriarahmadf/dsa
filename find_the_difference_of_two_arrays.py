from collections import defaultdict
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output = [[],[]]

        nums_hashmap = defaultdict(list)
        
        for num in nums1:
            nums_hashmap[num].append(1)
        for num in nums2:
            nums_hashmap[num].append(2)
        for key,value in nums_hashmap.items():
            if not (1 in value and 2 in value):
                if value[0] == 1:
                    output[0].append(key)
                else:
                    output[1].append(key)
        return output
    
# more time efficient solution Time complexity: O(n+m), Space complexity: O(n+m)
# using HashSet
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        nums1Set, nums2Set = set(nums1), set(nums2)

        res1, res2 = set(), set()

        for num in nums1:
            if num not in nums2Set:
                res1.add(num)
        for num in nums2:
            if num not in nums1Set:
                res2.add(num)

        return [list(res1), list(res2)]