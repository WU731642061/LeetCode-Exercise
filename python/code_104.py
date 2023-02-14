#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7

返回它的最大深度3

思考：
一开始做树的算法题总是蒙蔽的，因为要摆脱常规的逻辑思维，也有一部分原因是，平时很少去用到深度优先、广度优先的算法思想。
这道题的解法有点类似于快排，不过我一开始还是没有想到解法，看来还是不够融会贯通啊，23333
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def maxDepth(root: TreeNode) -> int:
  """
  第一种思路就是递归，通过比较左子树和右子树的最大值，来找到二叉树中最长的那条链
  唯一的缺陷是，python的默认配置下，最大递归层数是1000，这个会在下一种思路下改进
  """
  if not root:
    return 0
  else:
    left = maxDepth(root.left)
    right = maxDepth(root.right)
  # 加1是因为当前节点确认存在 
  return max(left, right) + 1


def maxDepth2(root: TreeNode) -> int:
  """
  第二种思想思迭代，本质上的思想是和递归一致的，但是可以解决栈溢出的问题
  """
  stack = []
  if root:
    stack.append((1, root))
  
  depth = 0
  while stack != []:
    current_depth, root = stack.pop()
    if root is not None:
      depth = max(depth, current_depth)
      stack.append((current_depth + 1, root.left))
      stack.append((current_depth + 1, root.right))
  
  return depth
