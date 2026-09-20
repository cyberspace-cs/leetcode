# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 030 / 100 题
================================================================
题号 : 142
标题 : 环形链表 II
难度 : 中等
分类 : 链表
链接 : https://leetcode.cn/problems/linked-list-cycle-ii/
================================================================

【题目描述】
若链表有环，返回入环的第一个节点；否则返回 None。

【示例】
head = [3,2,0,-4], pos = 1  →  值为 2 的节点

【思路提示】
快慢指针相遇后，把一个指针移回头节点，两指针同速前进再次相遇即为入环点。

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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
