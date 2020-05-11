#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/reverse-linked-list/

反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def reverseList(head):
  """
  最简单的思路就是，拆成数组去处理，但是这样失去了链表本身的意义
  这里还是写一个这种写法，抛砖引玉的作用
  """
  tmp = head
  arr = []
  # 得到一个包含所有节点的数组
  while tmp:
    arr.append(tmp)
    tmp = tmp.next
  arr = arr[::-1]  # 翻转数组
  head = arr[0] if arr else None
  for i in range(len(arr)):
    if i == len(arr)-1:
      arr[i].next = None
      break
    else:
      arr[i].next = arr[i+1]
  return head


def reverseList2(head):
  """
  为什么要写第一种写法，就是希望去了解翻转中的每一步，我们应该做什么
  接下来用迭代的思路，用链表本身去实现翻转
  主要实现思路如下：
  以1-2-3-4-5-NULL为例
  我们将2取出，插入到1(指的是上面示例1，后同)的位置，并将2指向1，再将3取出，插入到1的位置，将3指向2，类似于头插,以此类推
  """
  if not head:
    return None
  tmp = head.next
  head.next = None
  while tmp:
    # 要保存两个值，当前的node和node.next
    cur = head
    head = tmp
    tmp = tmp.next
    head.next = cur
  return head


def reverseList3(head):
  """
  经过测试，上面那种写法确实生效了，但是还是太啰嗦，还要判断head，继续优化一下代码
  """
  pre = None
  cur = head
  while cur:
    tmp = cur.next
    cur.next = pre
    pre = cur
    cur = tmp
  # 我们创造一个变量，让他代替head的作用，作为返回值
  return pre


def reverseList4(head):
  """
  最后一种思路，就是进阶里的，用递归解决他
  讲道理，适应了迭代的思考方式后，一下子用递归来处理，我还真没想出来，毕竟菜
  思考了一会后，看了一下大佬的答案，终于豁然开朗
  """
  if not head or not head.next:
    return head
  pre = reverseList4(head.next)
  # 以1-2-3-4-5为例，递归的结果是先取到5，然后是4
  # head.next指向5，然后将5.next指向自己，达到了翻转的目的，以此类推，4.next指向3，直到最后1.next指向None，最后返回一整个链表
  # 这个某种意义上，是以5为起点，向后延长的同时，改变前面的节点的指向
  head.next.next = head
  head.next = None
  return pre


# 这道题还是非常有意思的，迭代和递归展现出了两种不同的思考方式
# 先来看看迭代：我们翻转的思路类似于这种：
# 1-2-3-4-5；2-1-3-4-5；3-2-1-4-5；4-3-2-1-5；5-4-3-2-1；
# 而递归则是反过来，先取到尾部，再依次处理：
# 1-2-3-4-5；1-2-3-5-4；1-2-5-4-3；1-5-4-3-2；5-4-3-2-1；
# 当然，实际代码中，并不是完全像上面这样指向的，这里只是表达一种思维方式
