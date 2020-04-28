#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/reverse-integer/

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""

def reverse(x):
  """
  这也是一道非常简单的题目
  先是用python的api，将int转换成str，然后从无符号位开始翻转，就可以得到结果
  唯一需要额外判断的就是注意里的东西
  """
  if x>=0:
    x= str(x)
    x= int(x[::-1])
  else:
    x = str(x)[1:]
    x = -int(x[::-1])
  if x not in range(-2**31, 2**31-1):
    return 0
  return x





