# 给定一个 N 叉树，返回其节点值的后序遍历。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其后序遍历: [5,6,3,2,4,1]. 
# 
#  
# 
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root :
            return None
        stack_run = [root]
        result = []
        while stack_run:
            node = stack_run.pop()
            result.append(node.val)
            children = node.children
            for child in children:
                if child:
                    stack_run.append(child)
        result.reverse()
        return result
        
# leetcode submit region end(Prohibit modification and deletion)
