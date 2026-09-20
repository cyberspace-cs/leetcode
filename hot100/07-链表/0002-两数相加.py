# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 022 / 100 题
================================================================
题号 : 2
标题 : 两数相加
难度 : 中等
分类 : 链表
链接 : https://leetcode.cn/problems/add-two-numbers/
================================================================

【题目描述】
两个非负整数以逆序方式存储在链表中，求它们的和并以同样方式返回。

【示例】
[2,4,3] + [5,6,4]  →  [7,0,8]   # 342 + 465 = 807

【思路提示】
逐位相加并维护进位 carry，注意最后可能还剩一个进位节点。

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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
