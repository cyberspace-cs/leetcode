# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 024 / 100 题
================================================================
题号 : 21
标题 : 合并两个有序链表
难度 : 简单
分类 : 链表
链接 : https://leetcode.cn/problems/merge-two-sorted-lists/
================================================================

【题目描述】
将两个升序链表合并为一个新的升序链表并返回。

【示例】
[1,2,4] + [1,3,4]  →  [1,1,2,3,4,4]

【思路提示】
哑结点 + 双指针逐个比较接入，最后接上未走完的链表。

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
