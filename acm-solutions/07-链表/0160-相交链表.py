# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 160
标题 : 相交链表
难度 : 简单
分类 : 链表
链接 : https://leetcode.cn/problems/intersection-of-two-linked-lists/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：a 的 n 个整数；第三行：m；第四行：b 的 m 个整数；第五行：k。
k 为两表公共尾部的长度（公共尾部取两表各自的末 k 个元素），k=0 表示不相交。

【输出格式】
一行，相交起始节点的值；不相交输出 -1。

【样例输入】
2
5
4 1 8 4 5
6
5 6 1 8 4 5
3
2
1 2
1
3
0

【样例输出】
8
-1

"""

import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(vals):
    dummy = cur = ListNode()
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def dump(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return " ".join(map(str, out)) if out else "EMPTY"


def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    m = int(next(it))
    b = [int(next(it)) for _ in range(m)]
    k = int(next(it))

    ha, hb = build(a), build(b)
    if 0 < k <= n and k <= m:
        na = []
        cur = ha
        while cur:
            na.append(cur)
            cur = cur.next
        tail = na[n - k]
        nb = []
        cur = hb
        while cur:
            nb.append(cur)
            cur = cur.next
        if m - k - 1 >= 0:
            nb[m - k - 1].next = tail
        else:
            hb = tail

    p, q = ha, hb
    while p is not q:
        p = p.next if p else hb
        q = q.next if q else ha
    return p.val if p else -1

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
