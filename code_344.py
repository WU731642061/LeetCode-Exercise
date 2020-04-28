#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/reverse-string/

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
"""


def reverseString(s):
    """
    这道题本身没什么难度，python给了我们很多api去实现
    """
    return s[::-1]


def reverseString2(s):
    """
    在C语言中，字符串的本质其实是数组，那么我们也可以把这里的字符串当作数组来看待，因为python本身也是支持相关操作的
    """
    length = len(s)
    mid = length // 2
    for i in range(mid):
        s[i], s[length-1-i] = s[length-1-i], s[i]