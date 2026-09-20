# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 763
标题 : 划分字母区间
难度 : 中等
分类 : 贪心算法
链接 : https://leetcode.cn/problems/partition-labels/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
一行：字符串 s（仅含小写字母）。

【输出格式】
一行，各片段长度（按出现顺序，空格分隔）。

【样例输入】
2
ababcbacadefegdehijhklij
abc

【样例输出】
9 7 8
1 1 1

"""

import sys


def solve(it):
    s = next(it)
    last = {}
    for i, c in enumerate(s):
        last[c] = i
    res = []
    start = 0
    end = 0
    for i, c in enumerate(s):
        if last[c] > end:
            end = last[c]
        if i == end:
            res.append(end - start + 1)
            start = i + 1
    return " ".join(map(str, res))

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
