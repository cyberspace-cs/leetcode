# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 62    标题: 不同路径    难度: 中等    分类: 多维动态规划
# 链接: https://leetcode.cn/problems/unique-paths/
# 运行: python3 "0062-不同路径.py"   （按提示输入，或重定向样例输入）

def unique_paths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    # 在这里写你的代码（一维滚动）
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[n - 1]


def main():
    m = int(input())
    n = int(input())
    print(unique_paths(m, n))


if __name__ == "__main__":
    main()


# 62. 不同路径  中等
#
# 【题目描述】
# 机器人位于 m×n 网格左上角，每次只能向右或向下移动一步，求到达右下角的不同路径数。
#
# 【示例】
# m = 3, n = 7  →  28
#
# 【思路提示】
# dp[i][j] = dp[i-1][j] + dp[i][j-1]，可压缩为一维数组。
#
# 【输入格式】
# 第一行：m；第二行：n。
#
# 【样例输入】
# 3
# 7
# 【样例输出】
# 28
