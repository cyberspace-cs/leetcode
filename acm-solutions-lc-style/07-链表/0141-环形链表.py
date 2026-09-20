# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 141    标题: 环形链表    难度: 简单    分类: 链表
# 链接: https://leetcode.cn/problems/linked-list-cycle/
# 运行: python3 "0141-环形链表.py"   （按提示输入，或重定向样例输入）

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


def make_cycle(head, pos):
    """把链表的末节点指向下标 pos 处，构造环形链表；pos < 0 表示不构造。"""
    if pos < 0 or not head:
        return head
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    nodes[-1].next = nodes[pos]
    return head


def has_cycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    # 在这里写你的代码
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def main():
    nums = eval(input())
    pos = int(input())
    head = make_cycle(build_list(nums), pos)
    print(has_cycle(head))


if __name__ == "__main__":
    main()


# 141. 环形链表  简单
#
# 【题目描述】
# 判断链表中是否存在环。
#
# 【示例】
# head = [3,2,0,-4], pos = 1  →  true
#
# 【思路提示】
# 快慢指针，若两者相遇则存在环。
#
# 【输入格式】
# 第一行：链表元素列表；第二行：pos（入环位置 0-based，-1 表示无环）。
#
# 【样例输入】
# [3,2,0,-4]
# 1
# 【样例输出】
# True
