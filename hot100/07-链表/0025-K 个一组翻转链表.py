# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 027 / 100 题
================================================================
题号 : 25
标题 : K 个一组翻转链表
难度 : 困难
分类 : 链表
链接 : https://leetcode.cn/problems/reverse-nodes-in-k-group/
================================================================

【题目描述】
每 k 个节点为一组进行翻转；不足 k 个的尾部节点保持原有顺序。

【示例】
head = [1,2,3,4,5], k = 2  →  [2,1,4,3,5]

【思路提示】
先探测剩余是否够 k 个，再对这一段做局部反转并接回前后。

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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
