# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 2
标题 : 两数相加
难度 : 中等
分类 : 链表
链接 : https://leetcode.cn/problems/add-two-numbers/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数（逆序存放的低位在前）；第三行：m；第四行：m 个整数。

【输出格式】
一行，和的链表值（同样低位在前，空格分隔）。

【样例输入】
2
3
2 4 3
3
5 6 4
1
0
1
0

【样例输出】
7 0 8
0

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
    h1, h2 = build(a), build(b)
    dummy = cur = ListNode()
    carry = 0
    while h1 or h2 or carry:
        s = carry
        if h1:
            s += h1.val
            h1 = h1.next
        if h2:
            s += h2.val
            h2 = h2.next
        carry, d = divmod(s, 10)
        cur.next = ListNode(d)
        cur = cur.next
    return dump(dummy.next)

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
