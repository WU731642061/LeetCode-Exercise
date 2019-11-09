#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/contains-duplicate/

给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
"""


def containsDuplicate1(nums):
    """
    第一种思是通过python的set()方法，将list转换成set
    依据set元素不可重复的特性，判断set的长度和list的长度是否相等，得出是否有重复元素的结论
    """
    return len(nums) != len(set(nums))


def containsDuplicate2(nums):
    """
    第二种思路是创建一个新的set或者dict，依次判断原list的元素是否存在于新set/dict中，如果存在则返回True，否则返回false
    这里为什么不创建新的list，因为list的查询某个未知元素的时间复杂度是O(n), 而dict查询的时间复杂度是O(1)
    注意：python中set内部实现是dict的。在in操作上是O(1), 这一点比list要强。
    优化：可以从list的双端开始做搜索，这样可以减少一半的搜索的量
    """
    new_dict = {}
    start = 0
    end = len(nums) - 1
    while start <= end:
        if start == end:
            if nums[start] in new_dict:
                return True
            else:
                return False
        if nums[start] == nums[end]:
            return True
        elif nums[start] in new_dict or nums[end] in new_dict:
            return True
        else:
            new_dict[nums[start]] = 0
            new_dict[nums[end]] = 0
        start += 1
        end -= 1
    return False

