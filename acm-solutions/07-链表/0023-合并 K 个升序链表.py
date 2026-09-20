# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 23
标题 : 合并 K 个升序链表
难度 : 困难
分类 : 链表
链接 : https://leetcode.cn/problems/merge-k-sorted-lists/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：k；随后 k 组，每组第一行为该链表长度 len，第二行为 len 个升序整数。

【输出格式】
一行，合并后的升序链表值（空格分隔）；全空输出 EMPTY。

【样例输入】
1
3
3
1 4 5
3
1 3 4
2
2 6

【样例输出】
1 1 2 3 4 4 5 6

"""

import sys


import heapq


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


def solve(it):
    k = int(next(it))
    heap = []
    for i in range(k):
        L = int(next(it))
        head = build([int(next(it)) for _ in range(L)])
        if head:
            heapq.heappush(heap, (head.val, i, head))
    dummy = cur = ListNode()
    while heap:
        v, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    out = []
    head = dummy.next
    while head:
        out.append(head.val)
        head = head.next
    return " ".join(map(str, out)) if out else "EMPTY"

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
