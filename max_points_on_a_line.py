from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        slopes = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                if (points[j][0] - points[i][0]) == 0: # y parallel 
                    m = (float(inf),points[j][0])
                elif (points[j][1] - points[i][1]) == 0: # x parallel
                    m = (0,points[j][1])
                else:
                    m_1 = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    c = points[j][1] - m_1 * points[j][0]
                    m = (m_1, c)
                slopes[m].append(tuple(points[i]))
                slopes[m].append(tuple(points[j]))

        max_num_points = 0
        num_points = 0
        for key,value in slopes.items():
            num_points = len(set(value))
            max_num_points = max(max_num_points,num_points)
        return max_num_points            