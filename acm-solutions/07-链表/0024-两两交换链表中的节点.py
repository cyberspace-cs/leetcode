# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 24
标题 : 两两交换链表中的节点
难度 : 中等
分类 : 链表
链接 : https://leetcode.cn/problems/swap-nodes-in-pairs/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数。

【输出格式】
一行，两两交换后的链表值（空格分隔）。

【样例输入】
2
4
1 2 3 4
3
1 2 3

【样例输出】
2 1 4 3
2 1 3

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
    dummy = prev = ListNode(0, head)
    while prev.next and prev.next.next:
        a = prev.next
        b = a.next
        a.next = b.next
        b.next = a
        prev.next = b
        prev = a
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
