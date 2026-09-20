# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 21
标题 : 合并两个有序链表
难度 : 简单
分类 : 链表
链接 : https://leetcode.cn/problems/merge-two-sorted-lists/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数；第三行：m；第四行：m 个整数（两链表均升序）。

【输出格式】
一行，合并后的升序链表值（空格分隔）。

【样例输入】
2
3
1 2 4
3
1 3 4
1
5
1
1

【样例输出】
1 1 2 3 4 4
1 5

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
    while h1 and h2:
        if h1.val <= h2.val:
            cur.next = h1
            h1 = h1.next
        else:
            cur.next = h2
            h2 = h2.next
        cur = cur.next
    cur.next = h1 or h2
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
