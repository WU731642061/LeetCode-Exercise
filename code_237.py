#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/delete-node-in-a-linked-list/

请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:

4 --> 5 --> 1 --> 9

说明:
链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def deleteNode(node):
  """
  这里只是需要我们实现一个删除的方法，只要理解最基本的链表知识，还是非常简单的
  思路就是判断node.next是否存在，确保删除某个节点后，整个链表的连贯性
  """
  # 当node是末尾节点时，直接删除当前节点即可
  # 虽然说明里给出是非末尾节点，我这里还是添油加醋了一番，做题时可以不加
  if not node.next:
    node = None
    return
  # 不是时，将值赋给next节点
  node.val = node.next.val
  node.next = node.next.next