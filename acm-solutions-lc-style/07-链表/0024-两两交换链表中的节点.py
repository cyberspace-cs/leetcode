# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 24    标题: 两两交换链表中的节点    难度: 中等    分类: 链表
# 链接: https://leetcode.cn/problems/swap-nodes-in-pairs/
# 运行: python3 "0024-两两交换链表中的节点.py"   （按提示输入，或重定向样例输入）

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


def swap_pairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # 在这里写你的代码
    dummy = prev = ListNode(0, head)
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return dummy.next


def main():
    nums = eval(input())
    head = swap_pairs(build_list(nums))
    print(list_to_vals(head))


if __name__ == "__main__":
    main()


# 24. 两两交换链表中的节点  中等
#
# 【题目描述】
# 两两交换相邻节点，并返回交换后的头节点；不能修改节点内部的值。
#
# 【示例】
# head = [1,2,3,4]  →  [2,1,4,3]
#
# 【思路提示】
# 哑结点 + 三指针迭代完成局部换位；也可用递归。
#
# 【输入格式】
# 一行：链表元素列表，如 [1,2,3,4]。
#
# 【样例输入】
# [1,2,3,4]
# 【样例输出】
# [2, 1, 4, 3]
