#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/merge-two-sorted-lists/

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
  """
  第一种思路就是创建两个指针，依次对应两个链表的每一位，然后生成一个新的升序链表
  注意点，你可以先创建一个ListNode，这样就不用去判断它的头是否存在，减少重复性的代码
  """
  head = ListNode(None)
  lnode = head
  while l1 and l2:
    if l1.val <= l2.val:
      lnode.next = l1
      l1 = l1.next
    else:
      lnode.next = l2
      l2 = l2.next
    lnode = lnode.next
  if l1:
    lnode.next = l1
  else:
    lnode.next = l2
  return head.next


def mergeTwoLists2(l1: ListNode, l2: ListNode) -> ListNode:
  """
  第二种思路是用递归，我确实没想到，广大群众的思考方式还是很多的，借鉴的同时，也强化一下自己对递归的理解吧
  递归的思维方式在没见过它时是比较难想到的，但是一见到，就有一种豁然开朗的感觉，因此还是要多用，多思考
  """
  if l1 and l2:
    # 这里每次都做一次判断，如果l1值大于l2值，就进行一次交换，最后能保证递归时的正确性
    if l1.val > l2.val:
      l1, l2 = l2, l1
    l1.next = mergeTwoLists2(l1.next, l2)
  return l1 or l2
