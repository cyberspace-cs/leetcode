# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 19    标题: 删除链表的倒数第 N 个结点    难度: 中等    分类: 链表
# 链接: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
# 运行: python3 "0019-删除链表的倒数第 N 个结点.py"   （按提示输入，或重定向样例输入）

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


def remove_nth_from_end(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # 在这里写你的代码
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


def main():
    nums = eval(input())
    n = int(input())
    head = remove_nth_from_end(build_list(nums), n)
    print(list_to_vals(head))


if __name__ == "__main__":
    main()


# 19. 删除链表的倒数第 N 个结点  中等
#
# 【题目描述】
# 删除链表的倒数第 n 个节点，并返回头节点。
#
# 【示例】
# head = [1,2,3,4,5], n = 2  →  [1,2,3,5]
#
# 【思路提示】
# 哑结点 + 快慢指针，快指针先走 n+1 步，再同步前进直到快指针到末尾。
#
# 【输入格式】
# 第一行：链表元素列表；第二行：n（删除倒数第 n 个节点）。
#
# 【样例输入】
# [1,2,3,4,5]
# 2
# 【样例输出】
# [1, 2, 3, 5]
