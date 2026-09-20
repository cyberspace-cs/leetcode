# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 279    标题: 完全平方数    难度: 中等    分类: 动态规划
# 链接: https://leetcode.cn/problems/perfect-squares/
# 运行: python3 "0279-完全平方数.py"   （按提示输入，或重定向样例输入）

def num_squares(n):
    """
    :type n: int
    :rtype: int
    """
    # 在这里写你的代码（完全背包）
    dp = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        sq = i * i
        for j in range(sq, n + 1):
            dp[j] = min(dp[j], dp[j - sq] + 1)
    return dp[n]


def main():
    n = int(input())
    print(num_squares(n))


if __name__ == "__main__":
    main()


# 279. 完全平方数  中等
#
# 【题目描述】
# 求把 n 表示为若干个完全平方数之和所需的最少个数。
#
# 【示例】
# n = 12  →  3   # 12 = 4 + 4 + 4
#
# 【思路提示】
# 完全背包 / BFS：dp[i] = min(dp[i - j*j] + 1)。
#
# 【输入格式】
# 一行：n。
#
# 【样例输入】
# 12
# 【样例输出】
# 3
