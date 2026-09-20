# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 76    标题: 最小覆盖子串    难度: 困难    分类: 子串
# 链接: https://leetcode.cn/problems/minimum-window-substring/
# 运行: python3 "0076-最小覆盖子串.py"   （按提示输入，或重定向样例输入）

def min_window(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    # 在这里写你的代码
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    missing = len(t)
    left = 0
    best = None
    for right, ch in enumerate(s):
        if need.get(ch, 0) > 0:
            missing -= 1
        need[ch] = need.get(ch, 0) - 1
        while missing == 0:
            if best is None or right - left + 1 < best[1] - best[0] + 1:
                best = (left, right)
            need[s[left]] = need.get(s[left], 0) + 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return s[best[0]:best[1] + 1] if best else ""


def main():
    s = input()
    t = input()
    print(min_window(s, t))


if __name__ == "__main__":
    main()


# 76. 最小覆盖子串  困难
#
# 【题目描述】
# 在 s 中找出涵盖 t 中所有字符（含重复计数）的最短子串，不存在则返回空串。
#
# 【示例】
# s = "ADOBECODEBANC", t = "ABC"  →  "BANC"
#
# 【思路提示】
# 滑动窗口 + need/window 计数，窗口满足条件后不断收缩左边界取最优。
#
# 【输入格式】
# 第一行：字符串 s；第二行：字符串 t。
#
# 【样例输入】
# ADOBECODEBANC
# ABC
# 【样例输出】
# BANC
