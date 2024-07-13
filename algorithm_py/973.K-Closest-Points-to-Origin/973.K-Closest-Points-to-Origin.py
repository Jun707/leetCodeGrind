class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        new_list = []
        res = []
        for x,y in points:
            dis = x**2 + y **2
            new_list.append([dis,x , y])
        heapq.heapify(new_list)
        
        while k > 0:
            dis, x, y = heapq.heappop(new_list)
            res.append([x,y])
            k -= 1
        return res