# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 1143    标题: 最长公共子序列    难度: 中等    分类: 多维动态规划
# 链接: https://leetcode.cn/problems/longest-common-subsequence/
# 运行: python3 "1143-最长公共子序列.py"   （按提示输入，或重定向样例输入）

def longest_common_subsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    # 在这里写你的代码（一维滚动）
    n, m = len(text1), len(text2)
    dp = [0] * (m + 1)
    for i in range(1, n + 1):
        prev = 0
        for j in range(1, m + 1):
            tmp = dp[j]
            if text1[i - 1] == text2[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = tmp
    return dp[m]


def main():
    text1 = input()
    text2 = input()
    print(longest_common_subsequence(text1, text2))


if __name__ == "__main__":
    main()


# 1143. 最长公共子序列  中等
#
# 【题目描述】
# 给定两个字符串，求它们的最长公共子序列的长度（子序列不必连续）。
#
# 【示例】
# text1 = "abcde", text2 = "ace"  →  3   # "ace"
#
# 【思路提示】
# dp[i][j]：字符相等则 dp[i-1][j-1] + 1，否则取 max(dp[i-1][j], dp[i][j-1])。
#
# 【输入格式】
# 第一行：字符串 text1；第二行：字符串 text2。
#
# 【样例输入】
# abcde
# ace
# 【样例输出】
# 3
