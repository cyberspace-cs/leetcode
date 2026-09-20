# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 010 / 100 题
================================================================
题号 : 76
标题 : 最小覆盖子串
难度 : 困难
分类 : 子串
链接 : https://leetcode.cn/problems/minimum-window-substring/
================================================================

【题目描述】
在 s 中找出涵盖 t 中所有字符（含重复计数）的最短子串，不存在则返回空串。

【示例】
s = "ADOBECODEBANC", t = "ABC"  →  "BANC"

【思路提示】
滑动窗口 + need/window 计数，窗口满足条件后不断收缩左边界取最优。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
