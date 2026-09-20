# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 438    标题: 找到字符串中所有字母异位词    难度: 中等    分类: 滑动窗口
# 链接: https://leetcode.cn/problems/find-all-anagrams-in-a-string/
# 运行: python3 "0438-找到字符串中所有字母异位词.py"   （按提示输入，或重定向样例输入）

def find_anagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    # 在这里写你的代码
    need = [0] * 26
    for ch in p:
        need[ord(ch) - 97] += 1
    window = [0] * 26
    k = len(p)
    res = []
    for i, ch in enumerate(s):
        window[ord(ch) - 97] += 1
        if i >= k:
            window[ord(s[i - k]) - 97] -= 1
        if i >= k - 1 and window == need:
            res.append(i - k + 1)
    return res


def main():
    s = input()
    p = input()
    print(find_anagrams(s, p))


if __name__ == "__main__":
    main()


# 438. 找到字符串中所有字母异位词  中等
#
# 【题目描述】
# 给定字符串 s 和 p，找出 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#
# 【示例】
# s = "cbaebabacd", p = "abc"  →  [0,6]
#
# 【思路提示】
# 固定长度窗口滑动，比较窗口字符计数与 p 的字符计数。
#
# 【输入格式】
# 第一行：字符串 s；第二行：字符串 p。
#
# 【样例输入】
# cbaebabacd
# abc
# 【样例输出】
# [0, 6]
