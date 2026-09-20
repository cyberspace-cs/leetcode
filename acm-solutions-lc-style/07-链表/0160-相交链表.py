# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 160    标题: 相交链表    难度: 简单    分类: 链表
# 链接: https://leetcode.cn/problems/intersection-of-two-linked-lists/
# 运行: python3 "0160-相交链表.py"   （按提示输入，或重定向样例输入）

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


def build_intersect(a_vals, b_vals, k):
    """构造相交链表：两表末尾 k 个节点共享；k <= 0 表示不相交。返回 (headA, headB)。"""
    if k <= 0 or k > len(a_vals) or k > len(b_vals):
        return build_list(a_vals), build_list(b_vals)
    common = build_list(a_vals[len(a_vals) - k:])
    headA = build_list(a_vals[:len(a_vals) - k])
    headB = build_list(b_vals[:len(b_vals) - k])
    for head in (headA, headB):
        if head:
            cur = head
            while cur.next:
                cur = cur.next
            cur.next = common
    return (headA or common), (headB or common)


def get_intersection_node(headA, headB):
    """
    :type headA: ListNode
    :type headB: ListNode
    :rtype: ListNode
    """
    # 在这里写你的代码
    p, q = headA, headB
    while p is not q:
        p = p.next if p else headB
        q = q.next if q else headA
    return p


def main():
    a = eval(input())
    b = eval(input())
    k = int(input())
    headA, headB = build_intersect(a, b, k)
    node = get_intersection_node(headA, headB)
    print(node.val if node else -1)


if __name__ == "__main__":
    main()


# 160. 相交链表  简单
#
# 【题目描述】
# 找出两个单链表相交的起始节点；若不相交则返回 None。
#
# 【示例】
# intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]  →  值为 8 的节点
#
# 【思路提示】
# 双指针各自走完本链表后切换到对方头节点，两指针相遇处即为交点。
#
# 【输入格式】
# 第一行：链表 a 的列表；第二行：链表 b 的列表；第三行：k（公共尾部长度，0 表示不相交）。
#
# 【样例输入】
# [4,1,8,4,5]
# [5,6,1,8,4,5]
# 3
# 【样例输出】
# 8
