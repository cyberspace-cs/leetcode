# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 023 / 100 题
================================================================
题号 : 19
标题 : 删除链表的倒数第 N 个结点
难度 : 中等
分类 : 链表
链接 : https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
================================================================

【题目描述】
删除链表的倒数第 n 个节点，并返回头节点。

【示例】
head = [1,2,3,4,5], n = 2  →  [1,2,3,5]

【思路提示】
哑结点 + 快慢指针，快指针先走 n+1 步，再同步前进直到快指针到末尾。

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
