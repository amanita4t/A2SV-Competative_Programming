class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        xy = []
        yx = []
        for i in range(len(points)):
          dist = math.sqrt((points[i][0]) **2 + (points[i][1]) **2 )
          xy.append([dist,points[i]])
        xy.sort()
        for i in range(k):
            yx.append(xy[i][1])
        return yx
