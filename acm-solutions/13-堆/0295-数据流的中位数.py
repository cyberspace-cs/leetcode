# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 295
标题 : 数据流的中位数
难度 : 困难
分类 : 堆
链接 : https://leetcode.cn/problems/find-median-from-data-stream/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：q；随后 q 行，每行为 add num 或 findMedian。

【输出格式】
一行，按顺序输出所有 findMedian 的结果（整数原样输出，半整数保留 1 位小数，空格分隔）；
若无查询则输出 EMPTY。

【样例输入】
2
5
add 1
add 2
findMedian
add 3
findMedian
4
add 6
findMedian
add 10
findMedian

【样例输出】
1.5 2
6 8

"""

import sys


import heapq


def solve(it):
    q = int(next(it))
    small = []
    large = []
    out = []
    for _ in range(q):
        op = next(it)
        if op == "add":
            x = int(next(it))
            heapq.heappush(small, -x)
            heapq.heappush(large, -heapq.heappop(small))
            if len(large) > len(small):
                heapq.heappush(small, -heapq.heappop(large))
        else:
            if len(small) > len(large):
                out.append(str(-small[0]))
            else:
                v = (-small[0] + large[0]) / 2.0
                out.append(str(int(v)) if v == int(v) else "%.1f" % v)
    return " ".join(out) if out else "EMPTY"

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
