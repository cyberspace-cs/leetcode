# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 23    标题: 合并 K 个升序链表    难度: 困难    分类: 链表
# 链接: https://leetcode.cn/problems/merge-k-sorted-lists/
# 运行: python3 "0023-合并 K 个升序链表.py"   （按提示输入，或重定向样例输入）

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


def _merge_two(a, b):
    dummy = cur = ListNode()
    while a and b:
        if a.val <= b.val:
            cur.next = a
            a = a.next
        else:
            cur.next = b
            b = b.next
        cur = cur.next
    cur.next = a or b
    return dummy.next


def merge_k_lists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    # 在这里写你的代码（分治两两合并）
    if not lists:
        return None
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            a = lists[i]
            b = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(_merge_two(a, b))
        lists = merged
    return lists[0]


def main():
    groups = eval(input())
    lists = [build_list(g) for g in groups]
    head = merge_k_lists(lists)
    print(list_to_vals(head))


if __name__ == "__main__":
    main()


# 23. 合并 K 个升序链表  困难
#
# 【题目描述】
# 合并 k 个升序链表为一个升序链表。
#
# 【示例】
# lists = [[1,4,5],[1,3,4],[2,6]]  →  [1,1,2,3,4,4,5,6]
#
# 【思路提示】
# 分治法两两合并，或用最小堆维护 k 个当前头节点。
#
# 【输入格式】
# 一行：二维列表，每个子列表为一条升序链表，如 [[1,4,5],[1,3,4],[2,6]]。
#
# 【样例输入】
# [[1,4,5],[1,3,4],[2,6]]
# 【样例输出】
# [1, 1, 2, 3, 4, 4, 5, 6]
