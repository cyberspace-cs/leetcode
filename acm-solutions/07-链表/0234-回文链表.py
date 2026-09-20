# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 234
标题 : 回文链表
难度 : 简单
分类 : 链表
链接 : https://leetcode.cn/problems/palindrome-linked-list/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数。

【输出格式】
一行，true 或 false。

【样例输入】
3
4
1 2 2 1
2
1 2
1
1

【样例输出】
true
false
true

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
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    p, q = head, prev
    while q:
        if p.val != q.val:
            return "false"
        p = p.next
        q = q.next
    return "true"

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
