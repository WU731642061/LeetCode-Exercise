#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/count-and-say/

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221

1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。
"""

def countAndSay(n):
  """
  由于是对前一项的描述，所以对应的规则只有当数字大于3的时候，才会生效
  我们只需要依次遍历，然后根据规则得到相应的结果
  """

  if n <1 :
    return False
  if n == 1:
    return '1'
  if n == 2:
    return '11'
  start = '11'

  for i in range(3,n+1):
    tmp = '' # 暂时保存第n次的结果
    index = 0  # 从第一位开始遍历
    # 从字符串最后一位遍历到第二位
    for j in range(len(start)-1, 0, -1):
      if start[j] == start[j-1]:
        index += 1
      else:
        index += 1
        tmp = str(index) + start[j] + tmp
        index = 0
      # 特殊处理，当j==1时，我们需要处理字符串第一位
      if j == 1:
        index +=1
        tmp = str(index) + start[j-1] + tmp
    start = tmp
  return tmp 
  
# 我看最快的那种写法，是将tmp作为[]，这样处理的速度比拼接字符串更加快，这里我就不再写一种了，毕竟两者的主要思路是一样的
