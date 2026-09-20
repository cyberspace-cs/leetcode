# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 025 / 100 题
================================================================
题号 : 23
标题 : 合并 K 个升序链表
难度 : 困难
分类 : 链表
链接 : https://leetcode.cn/problems/merge-k-sorted-lists/
================================================================

【题目描述】
合并 k 个升序链表为一个升序链表。

【示例】
lists = [[1,4,5],[1,3,4],[2,6]]  →  [1,1,2,3,4,4,5,6]

【思路提示】
分治法两两合并，或用最小堆维护 k 个当前头节点。

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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
