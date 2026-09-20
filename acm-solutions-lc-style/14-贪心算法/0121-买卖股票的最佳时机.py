# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 121    标题: 买卖股票的最佳时机    难度: 简单    分类: 贪心算法
# 链接: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
# 运行: python3 "0121-买卖股票的最佳时机.py"   （按提示输入，或重定向样例输入）

def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # 在这里写你的代码
    low = prices[0]
    best = 0
    for p in prices[1:]:
        best = max(best, p - low)
        low = min(low, p)
    return best


def main():
    prices = eval(input())
    print(max_profit(prices))


if __name__ == "__main__":
    main()


# 121. 买卖股票的最佳时机  简单
#
# 【题目描述】
# 给定每日股价，只允许一次买入和一次卖出（先买后卖），求最大利润；不能获利则返回 0。
#
# 【示例】
# prices = [7,1,5,3,6,4]  →  5
#
# 【思路提示】
# 一次遍历，维护历史最低价，用当前价减最低价不断更新最大利润。
#
# 【输入格式】
# 一行：每日股价列表，如 [7,1,5,3,6,4]。
#
# 【样例输入】
# [7,1,5,3,6,4]
# 【样例输出】
# 5
