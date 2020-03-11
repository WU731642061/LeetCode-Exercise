#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/

给定两个数组，编写一个函数来计算它们的交集。

说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。

我们可以不考虑输出结果的顺序。

进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
思考：我看到其他答案里有的写法用到了sort()方法，而且用的时间很短，
     但是不确定在无序未知长度的数组中，sort()依然能保持高效性，并比普通的遍历更快
     这个等以后了解了python的sort原理后再来补充

如果 nums1 的大小比 nums2 小很多，哪种方法更优？

如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？(这个目前不会，以后会了回来处理)
"""


def intersect(nums1, nums2):
    """
    第一种思考思路是先比对两个数组的长度，只需要遍历长度较短的数组即可
    遍历较短的数组的每一个元素，如果该元素同时也存在于另一个数组中，即为两者的交集，在较长的数组中删除该元素，并继续遍历
    优化：可以和之前code_217的方法一样，从双端开始遍历，能够减少一般的循环事件，但测试出来使用的内存大小和时间差不多，不知道问题出在哪里
    """
    nums = []
    l1 = len(nums1)
    l2 = len(nums2)
    start = 0
    end = None

    if l1 == 0 or l2 == 0:
        return nums
    if l1 <= l2:
        end = l1 - 1
        while start <= end:
            if nums1[start] in nums2:
                nums.append(nums1[start])
                nums2.remove(nums1[start])
            if start == end:
                start += 1
                end -= 1
                continue
            if nums1[end] in nums2:
                nums.append(nums1[end])
                nums2.remove(nums1[end])
            start += 1
            end -= 1
    else:
        end = l2 - 1
        while start <= end:
            if nums2[start] in nums1:
                nums.append(nums2[start])
                nums1.remove(nums2[start])
            if start == end:
                start += 1
                end -= 1
                continue
            if nums2[end] in nums1:
                nums.append(nums2[end])
                nums1.remove(nums2[end])
            start += 1
            end -= 1
    return nums

    # 没有用双端遍历的代码
    # nums = []
    # l1 = len(nums1)
    # l2 = len(nums2)
    # if l1 == 0 or l2 == 0:
    #     return nums
    # if l1 <= l2:
    #     for i in range(0, l1):
    #         if nums1[i] in nums2:
    #             nums.append(nums1[i])
    #             nums2.remove(nums1[i])
    # else:
    #     for i in range(0, l2):
    #         if nums2[i] in nums1:
    #             nums.append(nums2[i])
    #             nums1.remove(nums2[i])
    # return nums

def intersect2(nums1, nums2):
    """
    第二种思考方式就是建立dict，得到一个类似于{列表元素:出现次数, ...}的字典，因为用到了字典，所以搜索元素是否存在的速度快了很多
    """
    my_dict = {}
    nums = []
    for i in nums1:
        # 获取这个元素的字典之并+1，如果不存在就赋予默认值0并+1
        my_dict[i] = my_dict.get(i, 0) + 1
    for j in nums2:
        if j in my_dict and my_dict[j] > 0:
            my_dict[j] -= 1
            nums.append(j)
    return nums