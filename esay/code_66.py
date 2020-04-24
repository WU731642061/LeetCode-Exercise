#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/plus-one/

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

"""

def plusOne(digits):
    """
    前提是数组是非空非负
    第一种思路是这样的，
    先将数组中的每一个元素转化为str,
    其次拼接成一个字符串，将字符串再次转化成数字，进行+1操作，
    然后再次转化成str并进行list
    最后通过循环将list中的每个元素转换成int
    这是我一看到这道题的解决思路，虽然整体代码不多，但是用到了两次循环，多次转化，我相信是有优化空间的
    """
    def switchFormat(n):
      print(type(n))
      if type(n) == str:
        return int(n)
      else:
        return str(n)
    digits = map(switchFormat, digits)
    digits = ''.join(digits)
    digits = int(digits)
    digits += 1
    digits = list(str(digits))
    digits = list(map(switchFormat, digits))
    return digits


def plusOne2(digits):
  """
  第二种思路是这样的，
  我们从数组的最后一位开始，进行+1处理，判断结果是否是10，如果是10就换成0同时进一位
  这个思路就和我们平时做加法的原理很像了
  """
  n = len(digits) - 1
  while True:
    digits[n] += 1
    # 先从简单的开始判断，当不为10时，我们直接break就好了
    if digits[n] != 10:
      break
    if digits[n] == 10:
      # 当值为10，要考虑两种情况，一个是位于首位，另一个是位于其他位
      if n == 0:
        digits[n] = 0
        digits.insert(0,1)
        break
      else:
        digits[n] = 0
        n = n - 1
  return digits
