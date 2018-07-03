#!/usr/bin/python3
#coding=utf-8


def removeDuplicates(nums):
    index = 0
    long = len(nums)
    if long == 0:
        return 0

    for i in range(1, long):
        if nums[i] != nums[index]:
            index += 1
            nums[index] = nums[i]
    print(nums[:index+1])
    return index + 1


if __name__ == '__main__':
    testList = [1, 1, 2, 2, 3]
    removeDuplicates(testList)