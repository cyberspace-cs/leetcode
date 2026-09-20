# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 21    标题: 合并两个有序链表    难度: 简单    分类: 链表
# 链接: https://leetcode.cn/problems/merge-two-sorted-lists/
# 运行: python3 "0021-合并两个有序链表.py"   （按提示输入，或重定向样例输入）

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


def merge_two_lists(list1, list2):
    """
    :type list1: ListNode
    :type list2: ListNode
    :rtype: ListNode
    """
    # 在这里写你的代码
    dummy = cur = ListNode()
    while list1 and list2:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    cur.next = list1 or list2
    return dummy.next


def main():
    a = eval(input())
    b = eval(input())
    head = merge_two_lists(build_list(a), build_list(b))
    print(list_to_vals(head))


if __name__ == "__main__":
    main()


# 21. 合并两个有序链表  简单
#
# 【题目描述】
# 将两个升序链表合并为一个新的升序链表并返回。
#
# 【示例】
# [1,2,4] + [1,3,4]  →  [1,1,2,3,4,4]
#
# 【思路提示】
# 哑结点 + 双指针逐个比较接入，最后接上未走完的链表。
#
# 【输入格式】
# 第一行：链表1（升序）；第二行：链表2（升序）。
#
# 【样例输入】
# [1,2,4]
# [1,3,4]
# 【样例输出】
# [1, 1, 2, 3, 4, 4]
