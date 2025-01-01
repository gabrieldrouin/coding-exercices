from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def buildTree(nums):
    if not nums:
        return None
    root = TreeNode(nums[0])
    queue = [root]
    i = 1
    while queue and i < len(nums):
        node = queue.pop(0)
        if i < len(nums):
            node.left = TreeNode(nums[i])
            queue.append(node.left)
            i += 1
        if i < len(nums):
            node.right = TreeNode(nums[i])
            queue.append(node.right)
            i += 1
    return root
def treeToArray(root):
    if not root:
       return []
    result = []
    queue = [root]
    while queue:
       node = queue.pop(0)
       result.append(node.val)
       
       if node.left:
           queue.append(node.left)
       if node.right:
           queue.append(node.right)    
    return result

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue: List[TreeNode] = []
        q_queue: List[TreeNode] = []

        p_queue.append(p)
        q_queue.append(q)

        while p_queue and q_queue:
            p_node = p_queue.pop()
            q_node = q_queue.pop()

            if not p_node and not q_node:
                continue
            if not p_node or not q_node or p_node.val != q_node.val:
                return False
            
            p_queue.append(p_node.left)
            p_queue.append(p_node.right)
            q_queue.append(q_node.left)
            q_queue.append(q_node.right)

        return True
            




sol = Solution()
p1 = buildTree([1,2,3])
q1 = buildTree([1,2,3])
p2 = buildTree([1,2,1])
q2 = buildTree([1,1,2])
print(sol.isSameTree(p1,q1))
print(sol.isSameTree(p2,q2))