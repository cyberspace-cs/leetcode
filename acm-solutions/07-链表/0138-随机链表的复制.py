# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 138
标题 : 随机链表的复制
难度 : 中等
分类 : 链表
链接 : https://leetcode.cn/problems/copy-list-with-random-pointer/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；随后 n 行，每行 val randIdx。randIdx 为 0-based 下标，-1 表示 null。

【输出格式】
第一行：n；随后 n 行，每行 val randIdx，为深拷贝后的链表。

【样例输入】
1
5
7 -1
13 0
11 4
10 2
1 0

【样例输出】
5
7 -1
13 0
11 4
10 2
1 0

"""

import sys


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def solve(it):
    n = int(next(it))
    vals = []
    rnd = []
    for _ in range(n):
        vals.append(int(next(it)))
        rnd.append(int(next(it)))

    nodes = [Node(v) for v in vals]
    for i in range(n - 1):
        nodes[i].next = nodes[i + 1]
    for i in range(n):
        nodes[i].random = nodes[rnd[i]] if rnd[i] >= 0 else None

    mp = {nd: Node(nd.val) for nd in nodes}
    for nd in nodes:
        cp = mp[nd]
        cp.next = mp[nd.next] if nd.next else None
        cp.random = mp[nd.random] if nd.random else None

    idx = {mp[nodes[i]]: i for i in range(n)}
    rows = []
    cur = mp[nodes[0]] if n else None
    while cur:
        rows.append("%d %d" % (cur.val, idx[cur.random] if cur.random else -1))
        cur = cur.next
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
