# Definition for a binary tree node.

# root = [3,9,20,None,None,15,7]
root = eval(input())

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.val = val
        self.right = right
        
import collections
from typing import Optional



class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # queue = collections.deque([root])
        queue = collections.deque(root)
        print(type(queue))
        depth = 0
        
        print(queue)
        
        while queue :
            depth += 1
            # insert child node of extracted node(queue)
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        # BFS repeated equals to depth
        return depth

tree = TreeNode([3,9,20,None,None,15,7])
print(tree)
a = Solution()
print(a.maxDepth((root)))
