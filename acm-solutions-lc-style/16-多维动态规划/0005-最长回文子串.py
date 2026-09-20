# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 5    标题: 最长回文子串    难度: 中等    分类: 多维动态规划
# 链接: https://leetcode.cn/problems/longest-palindromic-substring/
# 运行: python3 "0005-最长回文子串.py"   （按提示输入，或重定向样例输入）

def longest_palindrome(s):
    """
    :type s: str
    :rtype: str
    """
    # 在这里写你的代码（中心扩展）
    n = len(s)
    if n == 0:
        return ""
    start, best = 0, 1
    for i in range(n):
        for l, r in ((i, i), (i, i + 1)):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            length = r - l - 1
            if length > best:
                best = length
                start = l + 1
    return s[start:start + best]


def main():
    s = input()
    print(longest_palindrome(s))


if __name__ == "__main__":
    main()


# 5. 最长回文子串  中等
#
# 【题目描述】
# 给定字符串 s，找出其中最长的回文子串。
#
# 【示例】
# s = "babad"  →  "bab"（"aba" 也正确）
#
# 【思路提示】
# 中心扩展法最直观（O(n²) 时间、O(1) 空间）；也可用区间 DP 或 Manacher。
#
# 【输入格式】
# 一行：字符串 s，如 babad。
#
# 【样例输入】
# babad
# 【样例输出】
# bab
