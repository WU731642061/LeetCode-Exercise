#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""


def removeDuplicates1(nums):
    """
    第一种思路是用 python原生的set() 函数创建集合，需要注意的是，set是无序的
    再将集合转换成list，最后调用sort()函数排序。
    """
    nums[:] = sorted(list(set(nums)))
    return len(nums)


def removeDuplicates2(nums):
    """
    第二种思路是通过创建dict，利用key的unique的性质去重，最后用list([iterable])方法将一个可迭代对象转换成list
    """
    r = dict()
    for i in nums:
        r[i] = 0
    nums[:] = list(r.keys())
    return len(nums)


def removeDuplicates3(nums):
    """
    第三种思路是通过range正序去重会抛出list index out of range的错误，可以尝试倒序去重
    range(start, stop[, step])
    """
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            nums.pop(i + 1)

