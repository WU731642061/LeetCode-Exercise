#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/valid-palindrome/

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。
"""

def isPalindrome(s):
  """
  python本身已经提供了很好的api，那么就先从python自带的api开始
  思路一：我们需要做的是‘忽略’字符串中的符号，同时‘忽略’大小写
  然后通过判断str和str[::-1]是否相等即可
  """
  # 我们先创建一个空数组，用来存放字符串的有效元素
  r = []
  s = s.lower()
  for i in s:
    if i in "qwertyuiopasdfghjklzxcvbnm1234567890":
      r.append(i)
  return r == r[::-1]


def isPalindrome2(s):
  """
  第二种思路就是用正则去判断
  """
  tmp = re.sub(r"[^A-Za-z0-9]","", s).lower()
  return tmp == tmp[::-1]