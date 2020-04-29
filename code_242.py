#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/valid-anagram/

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""


def isAnagram(s, t):
  """
  这道题感觉还是有点争议的，因为示例里面s=""，t=""，标准答案是true，那么"car"和"car"应该也算作异位词吧
  第一种思路是，将字符串转换成list
  然后对数组串进行排序，如果完全相等，则返回true，否则返回false
  """
  l = list(s)
  r = list(r)
  if sorted(l) == sorted(r):
    return True
  return False


# 这道题我看了其他解答，没有什么特别好的解题思路
# 时间最快的答案是将s和t转换成set，然后循环通过count比对，我感觉并不能快很多
# 以后如果想到了更好的思路再补充