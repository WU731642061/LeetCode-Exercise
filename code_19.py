#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def removeNthFromEnd(head, n):
  """
  链表的特性就是你不知道它的结尾在哪里，每次遍历都是O(n)
  我的第一种思路是创建一个list，将每个node都存入list中，最后操作
  """
  count = 0
  cur = head
  l = []
  while cur:
    l.append(cur)
    count += 1
    cur = cur.next
  # 因为说明了说了n保证是有效的，因此不用考虑n
  index = len(l) - n
  # 接下来要考虑三种情况，就是节点只有1个，一般情况和删除尾部节点
  if len(l) == 1:
    return None
  if n == 1:
    l[index-1].next = None
  else:
    l[index].val = l[index].next.val
    l[index].next = l[index].next.next
  return head    


def removeNthFromEnd2(head, n):
  """
  在写第一种方法的时候，应该能感受到，这种写法不太优雅，
  因为你在使用链表的同时，使用了数组等于用到了额外的空间，并没有以链表结构的思维去思考这道题，而是转化成了数组来做
  要用链表打败链表2333
  有一种思路是把单向链表变成双向链表，到达尾部后，调用node.pre去实现一个倒数的删除
  但是后来想了想，可能这样改变了题目的初衷，所以思考了另一种解法
  我们可以设计两个“指针”a和b，以n个距离同时进行移动，当b到达链表的尾部时，a.next就是要被删除的元素
  但是会有一个问题，就是如果n为链表的长度，我们其实需要删除的是head，b会移动到None的位置，因为我们需要创建一个node，插入在head的前边
  """
  befo = ListNode(0)
  befo.next = head
  start = befo
  end = befo
  for i in range(n):
    end = end.next
  while end.next:
    start = start.next
    end = end.next
  start.next = start.next.next
  return befo.next
  # 我一开始的写法是判断了链表长度是否为1 ，后来参考到这个答案，发现这个答案更好，返回了befo.next
  # 本来befo.next指向head，但是当长度为1时，head就变成None了，这里直接就处理了，很巧妙
  