# brute force approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target- nums[i] == nums[j] and j!=i:
                    return i,j
                
# hash table approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in numsDict:
                return numsDict[comp],i
            numsDict[nums[i]]=i