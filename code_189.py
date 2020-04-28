#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/rotate-array/

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
"""


def rotate1(nums, k):
    """
    第一种思路是利用数组拼接，向右移动N位其实就是将[-n:]位数组拼接到[:-n]数组的前面
    需要注意的是k可能会大于数组本身的长度，那么每移动len(nums)位，数组与原数组重合，
    所以只需要计算 k % len(nums)后需要移动的结果
    """

    length = len(nums)
    n = k % length
    if n == 0:
        return
    nums[:] = nums[-n:] + nums[:-n]


def rotate2(nums, k):
    """
    第二种思路是通过头部插入的方式，实现向右平移的效果
    即向右平移一位就是将数组尾部的数据插入到头部中去
    这里有两种实现思路，一种是使用list.insert(index, obj)方法插入头部
    另一种是将数组翻转，然后通过list.pop(0)和append()的效果实现平移，最后将数组再次reserve()
    关于python中数组方法的时间复杂度，可以参考一下这篇文章：https://blog.csdn.net/u011318721/article/details/79378280
    通过上篇文章可以知道，通过insert方法实现平移的思路的时间复杂度为 n * (n + 1) = O(n^2)
    通过翻转+pop+insert方法实现平移的思路的时间复杂度为 2n + n * (n + 1) = O(n^2)
    """
    length = len(nums)
    n = k % length
    if n == 0:
        return
    for i in range(n):
        nums.insert(0, nums.pop())

    # 因为这两种做法思路相近，只是调用的方法不同，所以写在一个方法中
    # length = len(nums)
    # n = k % length
    # if n == 0:
    #     return
    # # 2n指的是数组需要翻转两次
    # nums.reverse()
    # for i in range(n):
    #     nums.append(nums.pop(0))
    # nums.reverse()


"""
TODO: 暂时就想到这两种方法，题目说可以有3种以上的解，以后若是有想到，继续补充
"""
