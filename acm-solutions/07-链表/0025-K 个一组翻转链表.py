# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 25
标题 : K 个一组翻转链表
难度 : 困难
分类 : 链表
链接 : https://leetcode.cn/problems/reverse-nodes-in-k-group/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n k；第二行：n 个整数。每 k 个一组翻转，不足 k 个保持原样。

【输出格式】
一行，翻转后的链表值（空格分隔）。

【样例输入】
2
5 2
1 2 3 4 5
5 3
1 2 3 4 5

【样例输出】
2 1 4 3 5
3 2 1 4 5

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
    k = int(next(it))
    head = build([int(next(it)) for _ in range(n)])
    if k <= 1:
        return dump(head)
    dummy = ListNode(0, head)
    group_prev = dummy
    while True:
        kth = group_prev
        ok = True
        for _ in range(k):
            kth = kth.next
            if not kth:
                ok = False
                break
        if not ok:
            break
        group_next = kth.next
        prev, cur = group_next, group_prev.next
        while cur is not group_next:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        start = group_prev.next
        group_prev.next = kth
        group_prev = start
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
