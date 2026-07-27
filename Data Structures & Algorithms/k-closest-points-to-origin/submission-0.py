import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []
        dist = []
        for i in range(len(points)):
            j = 0 
            d = math.sqrt((points[i][j])**2 + (points[i][j+1])**2)
            dist.append((d, points[i]))

            
        heapq.heapify(dist)

        for i in range(k):
            d, point = heapq.heappop(dist)
            res.append(point)

        return res
