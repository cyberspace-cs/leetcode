# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 234    标题: 回文链表    难度: 简单    分类: 链表
# 链接: https://leetcode.cn/problems/palindrome-linked-list/
# 运行: python3 "0234-回文链表.py"   （按提示输入，或重定向样例输入）

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


def is_palindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    # 在这里写你的代码
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # 反转后半部分
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    p, q = head, prev
    while q:
        if p.val != q.val:
            return False
        p = p.next
        q = q.next
    return True


def main():
    nums = eval(input())
    print(is_palindrome(build_list(nums)))


if __name__ == "__main__":
    main()


# 234. 回文链表  简单
#
# 【题目描述】
# 判断一个单链表是否为回文链表。
#
# 【示例】
# head = [1,2,2,1]  →  true
#
# 【思路提示】
# 快慢指针找到中点，反转后半段，再逐节点比较。
#
# 【输入格式】
# 一行：链表元素列表，如 [1,2,2,1]。
#
# 【样例输入】
# [1,2,2,1]
# 【样例输出】
# True
