# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 032 / 100 题
================================================================
题号 : 148
标题 : 排序链表
难度 : 中等
分类 : 链表
链接 : https://leetcode.cn/problems/sort-list/
================================================================

【题目描述】
将链表按升序排序并返回，要求在 O(n log n) 时间内完成。

【示例】
head = [4,2,1,3]  →  [1,2,3,4]

【思路提示】
归并排序：快慢指针找中点，递归排序后合并两条有序链表。

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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
