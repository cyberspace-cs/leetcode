# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 32    标题: 最长有效括号    难度: 困难    分类: 动态规划
# 链接: https://leetcode.cn/problems/longest-valid-parentheses/
# 运行: python3 "0032-最长有效括号.py"   （按提示输入，或重定向样例输入）

def longest_valid_parentheses(s):
    """
    :type s: str
    :rtype: int
    """
    # 在这里写你的代码（DP：dp[i] 表示以 i 结尾的最长有效长度）
    n = len(s)
    dp = [0] * n
    best = 0
    for i in range(1, n):
        if s[i] != ")":
            continue
        if s[i - 1] == "(":
            dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
        else:
            j = i - dp[i - 1] - 1
            if j >= 0 and s[j] == "(":
                dp[i] = dp[i - 1] + 2 + (dp[j - 1] if j >= 1 else 0)
        best = max(best, dp[i])
    return best


def main():
    s = input()
    print(longest_valid_parentheses(s))


if __name__ == "__main__":
    main()


# 32. 最长有效括号  困难
#
# 【题目描述】
# 找出字符串中最长的有效（正确闭合）括号子串，返回其长度。
#
# 【示例】
# s = "(()"  →  2
#
# 【思路提示】
# 栈存下标（先压入哨兵 -1）；或用 DP：dp[i] 表示以 i 结尾的最长有效长度。
#
# 【输入格式】
# 一行：括号字符串，如 ()())。
#
# 【样例输入】
# )()())
# 【样例输出】
# 4
