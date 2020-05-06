#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/string-to-integer-atoi/

请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

提示：

本题中的空白字符只包括空格字符 ' ' 。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
"""

def myAtoi(str):
  """
  大致需要做的几步
  首先可以用strip方法去去掉收尾的空格，先处理前后的空格方便处理字符串
  主要是判断第一个非空字符是否是0-9或+—，否则就返回0，
  我的第一种思路就是用try去int转化后的结果
  """

  str = str.strip()
  for i in range(len(str)):
    if str[i] not in "1234567890+-":
      # 我们这里只要取到第一个非数字的字符串为止
      str = str[:i]
      break
    if i != 0 and str[i] not in "+-":
      # 我们这里需要做一个判断，就是当+-位于后面时，例如123+-，这样的字符串是无效的
      str = str[:i]
      break
  try:
    n = int(str)
  except:
    return 0
  # 这边为了防止编译器计算int最大值(这样我们可能会跑的更快一点2333)，我们直接存结果进去
  if n > 2147483647:
    return 2147483647
  if n < -2147483648:
    return -2147483648
  return n


def myAtoi2(str):
  """
  虽然上面的方法解决了问题，但是十分的不优美，使用int本身去处理str的结果，感觉就失去了算法本身的意义，我想换个方式再尝试下
  这里主要是不去使用python的内置方法，而是尽量的只依靠基础类型的方法去实现
  """

  # 第一步，实现一个strip，python中的strip是通过c语言实现的，我这里通过python实现一个简易的strip函数
  # 首先做一个遍历，就是从头和尾处理字符串，直到遇到第一个非空格字符串停止搜索
  def strip(s):
    length = len(s)
    # 先判断一下空字符串的情况
    if not length:
      return ''
    start = 0
    end = length - 1
    start_stop = False
    end_stop = False
    while True:
      # 设定终止条件
      if start_stop and end_stop:
        break
      # 处理字符串左边的空格
      if not start_stop:
        if s[start] == ' ':
          start += 1
          # 这里做一个判断，当左值>=右值的情况下，就是考虑到'    '这样的字符串，必须做一些处理
          if start >= end:
            break
        else: 
          start_stop = True
      if not end_stop:
        if s[end] == ' ':
          end -=1
        else:
          end_stop = True
    return s[start:end+1]
  
  s = strip(str)
  # 第二步，我们在得到一个去掉空格的字符串的情况下，
  # 判断第一位是否是+-或者0-9，同时第二位是否是个数字，如果不是，直接返回0
  for i in range(len(s)):
    if i == 0 and s[i] not in "1234567890+-":
      return 0
    elif i == 0:
      continue
    if s[i] not in "1234567890":
      s = s[:i]
      break

  # 这一步处理完后我们会得到只包含+，-，0-9的情况
  # 但还有一个问题是，字符串可能是'+'，'-', '' 做一下处理即可
  if s == '+' or s == '-' or not s:
    return 0
  
  # 我这里做的，就是确保最后这个int方法，只会处理到纯数字的结果，而不是交给try去处理
  n = int(s)
  if n > 2147483647:
    return 2147483647
  if n < -2147483648:
    return -2147483648
  return n


def myAtoi3(str):
  """
  第三种思路就是用正则，当然，目前我对正则不能说是精通掌握，我也是直接借鉴别的回答者的答案了
  """
  import re

  if str=='':
    return 0
  str1=str.strip()
  if str1=='':
    return 0
  p='^[-,+]{0,1}[0-9]+'
  # 主要是这一步，匹配这样的一个字符串
  r=re.findall(p,str1)
  if len(r)==0:
    return 0
  x=int(r[0])
  if x<-2**31:
    return -2**31
  elif x>2**31-1:
    return 2**31-1
  else:
    return x
