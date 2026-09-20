# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 033 / 100 题
================================================================
题号 : 160
标题 : 相交链表
难度 : 简单
分类 : 链表
链接 : https://leetcode.cn/problems/intersection-of-two-linked-lists/
================================================================

【题目描述】
找出两个单链表相交的起始节点；若不相交则返回 None。

【示例】
intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]  →  值为 8 的节点

【思路提示】
双指针各自走完本链表后切换到对方头节点，两指针相遇处即为交点。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
