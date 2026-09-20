# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 028 / 100 题
================================================================
题号 : 138
标题 : 随机链表的复制
难度 : 中等
分类 : 链表
链接 : https://leetcode.cn/problems/copy-list-with-random-pointer/
================================================================

【题目描述】
复制一个带有 random 随机指针的链表，返回其深拷贝。

【示例】
head = [[7,null],[13,0],[11,4],[10,2],[1,0]]  →  深拷贝后的等值链表

【思路提示】
哈希表映射「原节点 → 新节点」；也可用拼接-拆分的 O(1) 空间做法。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
