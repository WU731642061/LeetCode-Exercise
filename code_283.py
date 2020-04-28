#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/move-zeroes/

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


def moveZeroes(nums):
    """
    这道题本身没有难度，要求只有两个，移动0，保持其他元素相对顺序，优化点在于，如何尽可能的减少操作次数
    第一种思路就是循环，每一次遍历遇到0则删除，最后统一append
    """

    length = len(nums)
    count_zero = 0
    # 这里尽量只遍历一次，这样就不需要用到remove方法，remove的时间复杂度是O(n)，没调用一次就要遍历一次数组，因此最好使用pop(index)的方式
    for i in range(length-1, -1, -1):
        if nums[i] == 0:
            nums.pop(i)
            count_zero +=1
    for i in range(count_zero):
        nums.append(0)


def moveZeroes2(nums):
  """
  第二种思路其实在写的时候也有想到过，就是通过索引实现位置交换，看了答案的解读后，感觉他们的解读更好，因此这里用了网上的解法
  主要实现思路就是通过双下标，当遇到不是0的元素时，两个下标i，j一起移动，当遇到0时，其中一个下标j定位到0的位置，另一个下标i继续前进
  直到遇到不是0的数，将i位置的元素与j位置的元素互换，同时双双+1，这样就不会改变相对位置的同时，实现了移动
  """
  if not nums:
    return 0
  
  j = 0
  for i in range(len(nums)):
    if nums[i]:
      # 这一步有无其实都不会影响结果，因为开始遇到第一个不为0的数字时，两个下标都是同步增长的，但是这个判断就体现了优化的过程，省去了不必要的替换
      if i > j:
        nums[j],nums[i] = nums[i],nums[j]
      j += 1
      