class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        total = 0
        def dfs(subset, total, i):
            if target == total:
                res.append(subset.copy())
                return
            elif total > target or i >= len(candidates):
                return
            
            subset.append(candidates[i])
            dfs(subset, total+candidates[i], i)
            subset.pop()
            dfs(subset, total, i+1)
        dfs(subset, total, 0)
        return res
        