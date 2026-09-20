# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 026 / 100 题
================================================================
题号 : 24
标题 : 两两交换链表中的节点
难度 : 中等
分类 : 链表
链接 : https://leetcode.cn/problems/swap-nodes-in-pairs/
================================================================

【题目描述】
两两交换相邻节点，并返回交换后的头节点；不能修改节点内部的值。

【示例】
head = [1,2,3,4]  →  [2,1,4,3]

【思路提示】
哑结点 + 三指针迭代完成局部换位；也可用递归。

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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
