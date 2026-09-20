# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 2    标题: 两数相加    难度: 中等    分类: 链表
# 链接: https://leetcode.cn/problems/add-two-numbers/
# 运行: python3 "0002-两数相加.py"   （按提示输入，或重定向样例输入）

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


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # 在这里写你的代码（数字逆序存放，进位相加）
    dummy = cur = ListNode()
    carry = 0
    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        carry, digit = divmod(total, 10)
        cur.next = ListNode(digit)
        cur = cur.next
    return dummy.next


def main():
    a = eval(input())
    b = eval(input())
    head = add_two_numbers(build_list(a), build_list(b))
    print(list_to_vals(head))


if __name__ == "__main__":
    main()


# 2. 两数相加  中等
#
# 【题目描述】
# 两个非负整数以逆序方式存储在链表中，求它们的和并以同样方式返回。
#
# 【示例】
# [2,4,3] + [5,6,4]  →  [7,0,8]   # 342 + 465 = 807
#
# 【思路提示】
# 逐位相加并维护进位 carry，注意最后可能还剩一个进位节点。
#
# 【输入格式】
# 第一行：链表1（低位在前）；第二行：链表2（低位在前）。
#
# 【样例输入】
# [2,4,3]
# [5,6,4]
# 【样例输出】
# [7, 0, 8]
