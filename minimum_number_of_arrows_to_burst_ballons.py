class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        # first sort the given points according to starting of the points
        points_sorted = sorted(points, key = lambda x: x[0])
        
        # first we take the first point as common interval
        common = points_sorted[0]      

        # this is a function that will find common interval between two points
        def limit_finder(point1,point2):
            lower_limit = max(point1[0],point2[0])
            higher_limit = min(point1[1],point2[1])
            return [lower_limit,higher_limit]

        # first we initiate the first arrow
        arrow = 1

        # run a loop from second point
        for i in range(1,len(points_sorted)): 
            
            # if  current point lower limit is less than higher limit of common interval
            if points_sorted[i][0] <= common[1]:
                # we find the new common interval between them
                common = limit_finder(common,points_sorted[i])
            else:
                # when current point outside of common interval
                arrow += 1 # we need another arrow
                common = points_sorted[i] # new common interval considered
        return arrow