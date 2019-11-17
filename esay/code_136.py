#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/single-number/

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
"""


def singleNumber(nums):
    """
    第一种思路是运用到位运算，将数组中的数字转换成二进制进行响应的运算
    其中运用到python的按位异或运算符(^)，当且仅当两对应的二进位相异时，结果为1，例如：123 ^ 123 = 0; 123 ^ 124 =7
    因此，将数组中的多个数据进行异或运算，相同的数组会变成0，只出现一次的会保留
    """
    from functools import reduce
    return reduce(lambda x, y: x ^ y, nums)


def singleNumber2(nums):
    """
    第二种思路就是普通的遍历，但是需要将列表先排序，再将排序好的列表依次与前后元素对比，得到唯一的那个数
    相较于第一种方法，这种方法肯定还是慢了许多的，因为多了一道排序的过程
    """
    nums[:] = sorted(nums)
    for i in range(len(nums)):
        if i == len(nums) - 1:
            return nums[i]
        if nums[i] == nums[i + 1] or nums[i] == nums[i - 1] :
            continue
        return nums[i]
