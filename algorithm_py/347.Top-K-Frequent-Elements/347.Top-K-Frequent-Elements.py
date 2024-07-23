class Solution:
    # brute force
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        res = []
        for num in nums:
            if num in nums_dict:
                nums_dict[num] +=1
            else:
                nums_dict[num] = 1
        while k > 0:
            count = float("-inf")
            freq = None
            for key in nums_dict:
                if nums_dict[key] > count and key not in res:
                    freq = key
                    count = nums_dict[key]
            res.append(freq)
            k-=1
        return res
        