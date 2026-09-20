# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 206    标题: 反转链表    难度: 简单    分类: 链表
# 链接: https://leetcode.cn/problems/reverse-linked-list/
# 运行: python3 "0206-反转链表.py"   （按提示输入，或重定向样例输入）

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(nums):
    dummy = ListNode()
    cur = dummy
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


def list_to_vals(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals


def reverse_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # 在这里写你的代码
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def main():
    nums = eval(input())
    head = build_list(nums)
    print(list_to_vals(reverse_list(head)))


if __name__ == "__main__":
    main()


# 206. 反转链表  简单
#
# 【题目描述】
# 反转一个单链表并返回新的头节点。
#
# 【示例】
# head = [1,2,3,4,5]  →  [5,4,3,2,1]
#
# 【思路提示】
# 迭代：用 prev / curr 两个指针逐个改变指向；也可用递归。
#
# 【输入格式】
# 一行：链表元素列表，如 [1,2,3,4,5]。
#
# 【样例输入】
# [1,2,3,4,5]
# 【样例输出】
# [5, 4, 3, 2, 1]
