#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/longest-common-prefix/

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

说明:

所有输入只包含小写字母 a-z 。
"""


def longestCommonPrefix(strs):
  """
  第一种思路先用普遍的遍历去做，
  取数组第一个元素作为默认的公共前缀，往后每一个依次和第一个比对，然后缩小公共前缀的范围
  """
  if len(strs) == 0:
    return ""
  if len(strs) == 1:
    return strs[0]
  prefix = strs[0]
  for i in range(1, len(strs)):
    index = 0
    cur = strs[i]  # 当前的字符串值
    # 这里处理一步，没有公共前缀的情况
    if not prefix:
      return ""
    # 两者取公共前缀的话，只要比较更短的那个就行
    length = len(cur) if len(cur) < len(prefix) else len(prefix)
    for j in range(length):
      if cur[j] == prefix[j]:
        index +=1
      else:
        break
    prefix = prefix[:index]
  return prefix


def longestCommonPrefix2(strs):
  """
  第二种方法，就是使用pythhon的find方法
  首先定义一个prefix，然后通过循环依次缩小prefix范围
  """
  if len(strs) == 0:
    return ""
  prefix = strs[0]
  for s in strs:
    while s.find(prefix) != 0:
      prefix = prefix[:len(prefix) - 1]
      if prefix == "":
        return prefix
  return prefix


def longestCommonPrefix3(strs):
  """
  上面那种思路一开始我也想到用find了，但是while那段循环是某个答案里写的
  确实比直接for循环更加的好，因此我想优化一下第一种思路
  """
  if len(strs) == 0:
    return ""
  if len(strs) == 1:
    return strs[0]
  prefix = strs[0]
  for s in strs[1:]:
    while prefix != s[:len(prefix)]:
      prefix = prefix[:len(prefix) - 1]
      if prefix == "":
        return prefix
  return prefix

def longestCommonPrefix4(strs):
  """
  最后一种思路是大佬的解答，这种思路是非常巧妙的，将每个字符串的每个字母丢进一个set中进行比较，从而得到结果
  """
  res = ""
  if len(strs) == 0:
    return ""
  for each in zip(*strs):  # zip()函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
    if len(set(each)) == 1:  # 利用集合创建一个无序不重复元素集
      res += each[0]
    else:
      return res
  return res
  