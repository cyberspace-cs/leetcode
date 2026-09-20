# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 3
标题 : 无重复字符的最长子串
难度 : 中等
分类 : 滑动窗口
链接 : https://leetcode.cn/problems/longest-substring-without-repeating-characters/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
一行：字符串 s（不含空白字符）。

【输出格式】
一行，不含重复字符的最长子串长度。

【样例输入】
3
abcabcbb
bbbbb
pwwkew

【样例输出】
3
1
3

"""

import sys


def solve(it):
    s = next(it)
    last = {}
    left = best = 0
    for i, c in enumerate(s):
        if c in last and last[c] >= left:
            left = last[c] + 1
        last[c] = i
        if i - left + 1 > best:
            best = i - left + 1
    return best

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        out.append(str(solve(it)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
