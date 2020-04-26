#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/two-sum/

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
"""


def twoSum(nums, target):
  """
  这道题是leetcode题库的第一题，本身也是没有难度的，因为已经明确答案是一一对应的了，主要思路在于找到一个数，并且查找数组中是否存在target-num1的数
  遍历是肯定需要的，问题在于，如何以最少的遍历次数锁定num1和num2
  例如[1，3，5，6]，目标值是8，不可能因为发现1没办法合成答案就以3为num1数再次遍历，如果一个数组足够长，这样最倒霉的情况下要遍历N^2次
  因为我们要逆转思路，就上面而言，我们不能以1为num1，去向后遍历查找是否存在8-1的元素，而是去找数组前面是否存在8-num[n]的元素
  为此，我们要借助字典，key存放数组的元素，value存放index
  """
  store = {}
  length = len(nums)
  for i in range(length):
    e = target - nums[i]
    if e in store:
      return [store[e], i]
    store[nums[i]] = i


# 暂时没有想到更好的思路，以后补


