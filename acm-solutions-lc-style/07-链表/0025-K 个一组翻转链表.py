# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 25    标题: K 个一组翻转链表    难度: 困难    分类: 链表
# 链接: https://leetcode.cn/problems/reverse-nodes-in-k-group/
# 运行: python3 "0025-K 个一组翻转链表.py"   （按提示输入，或重定向样例输入）

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


def reverse_k_group(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    # 在这里写你的代码
    if k <= 1:
        return head
    dummy = ListNode(0, head)
    group_prev = dummy
    while True:
        kth = group_prev
        ok = True
        for _ in range(k):
            kth = kth.next
            if not kth:
                ok = False
                break
        if not ok:
            break
        group_next = kth.next
        prev, cur = group_next, group_prev.next
        while cur is not group_next:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        start = group_prev.next
        group_prev.next = kth
        group_prev = start
    return dummy.next


def main():
    nums = eval(input())
    k = int(input())
    head = reverse_k_group(build_list(nums), k)
    print(list_to_vals(head))


if __name__ == "__main__":
    main()


# 25. K 个一组翻转链表  困难
#
# 【题目描述】
# 每 k 个节点为一组进行翻转；不足 k 个的尾部节点保持原有顺序。
#
# 【示例】
# head = [1,2,3,4,5], k = 2  →  [2,1,4,3,5]
#
# 【思路提示】
# 先探测剩余是否够 k 个，再对这一段做局部反转并接回前后。
#
# 【输入格式】
# 第一行：链表元素列表；第二行：k。不足 k 个的尾部保持原样。
#
# 【样例输入】
# [1,2,3,4,5]
# 2
# 【样例输出】
# [2, 1, 4, 3, 5]
