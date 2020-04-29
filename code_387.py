#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/first-unique-character-in-a-string/

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

注意事项：您可以假定该字符串只包含小写字母。
"""


def firstUniqChar(s):
  """
  这道题的解法有很多种，可以用普通的遍历去重，也可以用dict，我尽量多写几种，包括自己想的，和答案里看到的
  第一种就是去遍历，然后建立dict，最后查找dict中，value为1的那个key值
  """
  count = {}
  for i in s:
    if count.get(i):
      count[i] += 1
    else:
      count[i] = 1
  
  for n in count:
    if count[n] == 1:
      return s.index(n)
  return -1


def firstUniqChar2(s):
  """
  第二种方法，是答案里的一个写法，用到了collection这个库，我认为虽然这个答案可以通过验证，但是做算法题还是尽量少用库，虽然这些库运行起来确实很快
  更重要的是去了解实现一种算法的本质，优化点。如果用了库，可能就会忽略这些。毕竟快只是其次。
  """
  from collections import Counter
  c = Counter(s)

  for i in range(len(s)):
    if c[s[i]]==1:
        return i
  return -1


def firstUniqChar3(s):
  """
  第三中方法，也是答案里的方法，主要是用到了str.find和str.rfind两个方法，不得不说，原生的find的方法确实比使用dict更快，可能是底层的优化吧
  """
  char = "abcdefghijklmnopqrstuvwxyz"
  res = len(s)
  # 遍历小写的26个字母
  for ch in char:
    # 查到s中第一个出现的这个字母的位置
    left = s.find(ch)
    # 如果这个字母存在，并使rfind也是它，即是唯一的值，将这个字母的位置赋给res
    if left != -1 and left == s.rfind(ch):
        # 如果存在多个唯一值，取最小值
        res = min(res, left)
  return res if res != len(s) else -1