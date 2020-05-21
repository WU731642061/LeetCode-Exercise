#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/linked-list-cycle/

给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

进阶：
你能用 O(1)（即，常量）内存解决此问题吗？
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def hasCycle(head: ListNode) -> bool:
  """
  还是从最简单的思路开始吧，用数组，这种解法思路code_234(回文链表)有相同的地方
  同样的，缺点也是一样的，不满足O(1)的空间复杂度
  """
  l = []
  while head:
    if head in l:
      return True
    l.append(head)
    head = head.next
  return False
  # 查一句嘴，因为用了in查找，速度之慢，可想而知，没超时只能说官方的测试用例还是挺宽容的，233333


def hasCycle2(head: ListNode) -> bool:
  """
  第二种解法我思考了挺久的，因为这是一个薛定谔的环，也就是说，你不知道他是否是一个环
  如果不是一个环，那么last.next一定为None，得到这个结果就比较好写
  如果是一个环，你不知道它的末尾在哪里，你也不知道环的起点是哪里
  但是有一点可以证明的是，如果存在一个环，在环上的两个点，以不同速度前进，迟早会重合
  我们可以设置两个变量，以不同的速度得到next和next.next值，如果重合了，说明是一个环
  """
  if not head:
    return False
  before, after = head, head.next
  while True:
    if before == after:
      return True
    try:
      before = before.next
      after = after.next.next
    except:
      return False




