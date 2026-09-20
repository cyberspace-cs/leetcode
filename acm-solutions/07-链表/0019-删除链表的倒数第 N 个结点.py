# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 19
标题 : 删除链表的倒数第 N 个结点
难度 : 中等
分类 : 链表
链接 : https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n k；第二行：n 个整数。删除倒数第 k 个节点。

【输出格式】
一行，删除后的链表值（空格分隔）；空链表输出 EMPTY。

【样例输入】
2
5 2
1 2 3 4 5
1 1
1

【样例输出】
1 2 3 5
EMPTY

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
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(k + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
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
