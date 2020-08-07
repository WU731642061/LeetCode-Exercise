#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/palindrome-linked-list/

请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def isPalindrome(head: ListNode) -> bool:
  """
  还是先最简单的思路吧，通过list来处理，取出所有的value，然后翻转，就可以检查是否是回文了
  但是这里不满足O(1)的空间复杂度
  """
  value = []
  while head:
    value.append(head.val)
    head = head.next
  return value == value[::-1]


def isPalindrome2(head: ListNode) -> bool:
  """
  还是那句话，这样就失去了链表题目考察我们本身的意义了，要用链表打败链表
  我们先不考虑进阶的要求，每种思路都去尝试一下，只有在不断优化的过程中，才能体会到算法的美妙
  思路：加入我们不考虑时间复杂度，我们该怎么做
  1. 拿到链表的长度
  2. 从head开始依次比较
  3. 每一项比较，我们就去遍历一次链表，0对应len-1,1对应len-2....
  4. 返回结果
  """
  def getNode(head, n):
    node = head
    for i in range(n-1):
      node = node.next
    return node

  length = 0
  cur = head
  
  while cur:
    length += 1
    cur = cur.next
  
  cur = head
  for i in range(length//2):
    # 1,2,3,4,5,4,3,2,1
    r = getNode(head, length-i)
    if cur.val != r.val:
      return False
    cur = cur.next
  return True
  # 结果就是妥妥的超时了，但是不考虑时间情况下的话，这种方法应该是可行的


def isPalindrome3(head: ListNode) -> bool:
  """
  这种思路是把链表变成双向链表
  先遍历一遍，创建pre属性
  然后拿head和last进行一一比较
  """
  pre = None
  cur = head

  last = None
  while cur:
    cur.pre = pre
    pre = cur
    cur = cur.next
    if cur == None:
      last = pre
  
  while True:
    if head == last:
      break
    if head.val != last.val:
      return False
    else:
      head = head.next
      last = last.pre
  return True


# 我在答案里看到还有一种思路也很有趣，先遍历一遍，获得整个链表的长度，然后翻转其中的一半(length//2)，同时取到一半时(length//2+1)的链表节点，同时开始遍历
# 这里我就不写出解法了，如果有缘人看到这，可是尝试着自己写一下
