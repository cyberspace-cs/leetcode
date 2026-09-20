# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 029 / 100 题
================================================================
题号 : 141
标题 : 环形链表
难度 : 简单
分类 : 链表
链接 : https://leetcode.cn/problems/linked-list-cycle/
================================================================

【题目描述】
判断链表中是否存在环。

【示例】
head = [3,2,0,-4], pos = 1  →  true

【思路提示】
快慢指针，若两者相遇则存在环。

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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
