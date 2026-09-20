# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 72    标题: 编辑距离    难度: 中等    分类: 多维动态规划
# 链接: https://leetcode.cn/problems/edit-distance/
# 运行: python3 "0072-编辑距离.py"   （按提示输入，或重定向样例输入）

def min_distance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    # 在这里写你的代码（一维滚动）
    n, m = len(word1), len(word2)
    dp = list(range(m + 1))
    for i in range(1, n + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, m + 1):
            tmp = dp[j]
            if word1[i - 1] == word2[j - 1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(prev, dp[j], dp[j - 1])
            prev = tmp
    return dp[m]


def main():
    word1 = input()
    word2 = input()
    print(min_distance(word1, word2))


if __name__ == "__main__":
    main()


# 72. 编辑距离  中等
#
# 【题目描述】
# 求把 word1 转换成 word2 所需的最少操作次数，允许插入、删除、替换一个字符。
#
# 【示例】
# word1 = "horse", word2 = "ros"  →  3
#
# 【思路提示】
# 二维 DP，注意边界初始化（dp[0][j] = j、dp[i][0] = i），字符不同时取三种操作的最小值 + 1。
#
# 【输入格式】
# 第一行：word1；第二行：word2。
#
# 【样例输入】
# horse
# ros
# 【样例输出】
# 3
