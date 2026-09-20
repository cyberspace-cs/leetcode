# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 438
标题 : 找到字符串中所有字母异位词
难度 : 中等
分类 : 滑动窗口
链接 : https://leetcode.cn/problems/find-all-anagrams-in-a-string/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：字符串 s；第二行：字符串 p（均不含空白字符）。

【输出格式】
第一行：个数 g；随后 g 行，每行一个升序排列的起始下标；无解时仅输出 0。

【样例输入】
2
cbaebabacd
abc
abab
ab

【样例输出】
2
0
6
3
0
1
2

"""

import sys


def solve(it):
    s = next(it)
    p = next(it)
    need = [0] * 26
    for c in p:
        need[ord(c) - 97] += 1
    win = [0] * 26
    k = len(p)
    res = []
    for i, c in enumerate(s):
        win[ord(c) - 97] += 1
        if i >= k:
            win[ord(s[i - k]) - 97] -= 1
        if i >= k - 1 and win == need:
            res.append(i - k + 1)
    return "\n".join([str(len(res))] + [str(x) for x in res])

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
