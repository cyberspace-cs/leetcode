# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 148
标题 : 排序链表
难度 : 中等
分类 : 链表
链接 : https://leetcode.cn/problems/sort-list/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数。

【输出格式】
一行，升序排序后的链表值（空格分隔）。

【样例输入】
2
4
4 2 1 3
5
-1 5 3 4 0

【样例输出】
1 2 3 4
-1 0 3 4 5

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
    head = build([int(next(it)) for _ in range(n)])

    def merge_sort(h):
        if not h or not h.next:
            return h
        slow, fast = h, h.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        l, r = merge_sort(h), merge_sort(mid)
        dummy = cur = ListNode()
        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next

    return dump(merge_sort(head))

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
