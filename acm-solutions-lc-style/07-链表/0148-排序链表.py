# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 148    标题: 排序链表    难度: 中等    分类: 链表
# 链接: https://leetcode.cn/problems/sort-list/
# 运行: python3 "0148-排序链表.py"   （按提示输入，或重定向样例输入）

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


def sort_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # 在这里写你的代码（归并排序）
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = sort_list(head)
    right = sort_list(mid)
    dummy = cur = ListNode()
    while left and right:
        if left.val <= right.val:
            cur.next = left
            left = left.next
        else:
            cur.next = right
            right = right.next
        cur = cur.next
    cur.next = left or right
    return dummy.next


def main():
    nums = eval(input())
    head = sort_list(build_list(nums))
    print(list_to_vals(head))


if __name__ == "__main__":
    main()


# 148. 排序链表  中等
#
# 【题目描述】
# 将链表按升序排序并返回，要求在 O(n log n) 时间内完成。
#
# 【示例】
# head = [4,2,1,3]  →  [1,2,3,4]
#
# 【思路提示】
# 归并排序：快慢指针找中点，递归排序后合并两条有序链表。
#
# 【输入格式】
# 一行：链表元素列表，如 [4,2,1,3]。
#
# 【样例输入】
# [4,2,1,3]
# 【样例输出】
# [1, 2, 3, 4]
