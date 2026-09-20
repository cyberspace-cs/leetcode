# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 70    标题: 爬楼梯    难度: 简单    分类: 动态规划
# 链接: https://leetcode.cn/problems/climbing-stairs/
# 运行: python3 "0070-爬楼梯.py"   （按提示输入，或重定向样例输入）

def climb_stairs(n):
    """
    :type n: int
    :rtype: int
    """
    # 在这里写你的代码
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    n = int(input())
    print(climb_stairs(n))


if __name__ == "__main__":
    main()


# 70. 爬楼梯  简单
#
# 【题目描述】
# 每次可以爬 1 或 2 个台阶，求爬到第 n 阶有多少种不同的方法。
#
# 【示例】
# n = 3  →  3   # 1+1+1 / 1+2 / 2+1
#
# 【思路提示】
# dp[i] = dp[i-1] + dp[i-2]，可用两个滚动变量把空间优化到 O(1)。
#
# 【输入格式】
# 一行：n（台阶数）。
#
# 【样例输入】
# 3
# 【样例输出】
# 3
