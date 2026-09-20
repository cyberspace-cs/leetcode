# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 053 / 100 题
================================================================
题号 : 208
标题 : 实现 Trie (前缀树)
难度 : 中等
分类 : 图论
链接 : https://leetcode.cn/problems/implement-trie-prefix-tree/
================================================================

【题目描述】
实现前缀树 Trie，支持插入单词、查询完整单词、查询是否存在指定前缀。

【示例】
insert("apple"), search("apple") → true, search("app") → false, startsWith("app") → true

【思路提示】
每个节点用 dict / 定长数组保存子节点，并用布尔标记是否为单词结尾。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Trie:

    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError

    def startsWith(self, prefix: str) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # obj = <按题目要求实例化上面的类>

    pass
