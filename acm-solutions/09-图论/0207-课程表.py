# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 207
标题 : 课程表
难度 : 中等
分类 : 图论
链接 : https://leetcode.cn/problems/course-schedule/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：numCourses E；随后 E 行，每行 a b，表示 b 是 a 的先修课（先修 b 才能修 a）。

【输出格式】
一行，true 或 false，表示能否修完所有课程。

【样例输入】
3
2 1
1 0
2 2
1 0
0 1
3 2
1 0
2 1

【样例输出】
true
false
true

"""

import sys


from collections import deque


def solve(it):
    nc = int(next(it))
    e = int(next(it))
    adj = [[] for _ in range(nc)]
    indeg = [0] * nc
    for _ in range(e):
        a = int(next(it))
        b = int(next(it))
        adj[b].append(a)
        indeg[a] += 1
    dq = deque(i for i in range(nc) if indeg[i] == 0)
    seen = 0
    while dq:
        u = dq.popleft()
        seen += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                dq.append(v)
    return "true" if seen == nc else "false"

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
