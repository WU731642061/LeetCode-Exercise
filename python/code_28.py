#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/implement-strstr/

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""

def strStr(haystack, needle):
  """
  python提供了原生的find方法
  第一种思路就使用python的find方法去实现
  主要是帮助温习一下api的使用
  """
  if needle == '':
    return 0
  if needle not in haystack:
    return -1
  return haystack.find(needle)


def strStr2(haystack, needle):
  """
  当我们不使用find方法时，
  需要通过遍历去查找needle是否和haystack中有重复的部分
  """
  if needle == '':
    return 0
  # 遍历从0到单词长度的最后一个字符串位置
  for i in range(len(haystack)-len(needle)+1):
    if haystack[i:i+len(needle)]==needle:
      return i
  return -1