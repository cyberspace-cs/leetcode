# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 031 / 100 题
================================================================
题号 : 146
标题 : LRU 缓存
难度 : 中等
分类 : 链表
链接 : https://leetcode.cn/problems/lru-cache/
================================================================

【题目描述】
设计 LRU（最近最少使用）缓存，支持 get 和 put，且两个操作都要求 O(1) 平均时间复杂度。

【示例】
capacity = 2: put(1,1), put(2,2), get(1) → 1, put(3,3), get(2) → -1

【思路提示】
哈希表 + 双向链表（Python 中也可直接用 collections.OrderedDict）。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class LRUCache:

    def __init__(self, capacity: int):
        # TODO: 初始化容量与数据结构
        pass

    def get(self, key: int) -> int:
        # TODO: 命中则返回并更新为最近使用，未命中返回 -1
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        # TODO: 写入或更新；超出容量时淘汰最久未使用项
        raise NotImplementedError


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # obj = <按题目要求实例化上面的类>

    pass
