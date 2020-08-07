#!/usr/bin/env python3

"""
link: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""


def maxProfit(prices):
    """
    思路；只要第二天的值(A2)大于当天的值(A1)，即可被视为有利可图，即使第三天的值(A3)大于第二天的值(A2)，其利润总和也是相等的
    即：A3 - A1 = (A3 - A2) + (A2 - A1)
    """
    profit = 0
    length = len(prices)
    for i in range(1, length):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit
 