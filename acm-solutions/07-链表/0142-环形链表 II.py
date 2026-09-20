# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 142
标题 : 环形链表 II
难度 : 中等
分类 : 链表
链接 : https://leetcode.cn/problems/linked-list-cycle-ii/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数；第三行：pos。pos 为入环位置（0-based），-1 表示无环。

【输出格式】
一行，入环第一个节点的值；无环输出 -1。

【样例输入】
2
4
3 2 0 -4
1
3
1 2 3
-1

【样例输出】
2
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
    vals = [int(next(it)) for _ in range(n)]
    pos = int(next(it))
    head = build(vals)
    if pos >= 0 and n:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        nodes[-1].next = nodes[pos]
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            p = head
            while p is not slow:
                p = p.next
                slow = slow.next
            return p.val
    return -1

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
