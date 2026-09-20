# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 034 / 100 题
================================================================
题号 : 206
标题 : 反转链表
难度 : 简单
分类 : 链表
链接 : https://leetcode.cn/problems/reverse-linked-list/
================================================================

【题目描述】
反转一个单链表并返回新的头节点。

【示例】
head = [1,2,3,4,5]  →  [5,4,3,2,1]

【思路提示】
迭代：用 prev / curr 两个指针逐个改变指向；也可用递归。

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
