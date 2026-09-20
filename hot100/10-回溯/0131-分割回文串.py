# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 062 / 100 题
================================================================
题号 : 131
标题 : 分割回文串
难度 : 中等
分类 : 回溯
链接 : https://leetcode.cn/problems/palindrome-partitioning/
================================================================

【题目描述】
把字符串分割成若干子串，使每个子串都是回文串，返回所有可能的分割方案。

【示例】
s = "aab"  →  [["a","a","b"],["aa","b"]]

【思路提示】
回溯 + 剪枝：只有当当前子串是回文时才继续向下递归。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
