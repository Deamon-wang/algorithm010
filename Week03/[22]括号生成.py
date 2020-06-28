# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p,left,right,parens=[]):
            if left:
                generate(p + '(',left-1,right)
            if right > left:
                generate(p + ')',left,right - 1)
            if not right:
                parens += p,
            return parens
        return generate('',n,n)
# leetcode submit region end(Prohibit modification and deletion)
