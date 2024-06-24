# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []

        if root:
            q.append(root)
        
        while len(q):
            rightView = None
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)                      
                if curr.right:
                    q.append(curr.right)
                rightView = curr.val
            res.append(rightView)
        return res