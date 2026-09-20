# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 56
标题 : 合并区间
难度 : 中等
分类 : 普通数组
链接 : https://leetcode.cn/problems/merge-intervals/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；随后 n 行，每行两个整数 l r 表示闭区间 [l, r]。

【输出格式】
第一行：合并后的区间数 g；随后 g 行，每行 l r（按左端点升序）。

【样例输入】
2
4
1 3
2 6
8 10
15 18
2
1 4
4 5

【样例输出】
3
1 6
8 10
15 18
1
1 5

"""

import sys


def solve(it):
    n = int(next(it))
    iv = []
    for _ in range(n):
        iv.append((int(next(it)), int(next(it))))
    iv.sort()
    res = []
    for l, r in iv:
        if res and l <= res[-1][1]:
            if r > res[-1][1]:
                res[-1][1] = r
        else:
            res.append([l, r])
    rows = ["%d %d" % (l, r) for l, r in res]
    return "\n".join([str(len(rows))] + rows)

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
