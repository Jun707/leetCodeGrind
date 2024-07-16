class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp = nums[:k]

        heapq.heapify(temp)

        for num in nums[k:]:
            heapq.heappush(temp, num)
            heapq.heappop(temp)
        return temp[0]