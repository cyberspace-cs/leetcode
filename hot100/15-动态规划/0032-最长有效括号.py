# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 081 / 100 题
================================================================
题号 : 32
标题 : 最长有效括号
难度 : 困难
分类 : 动态规划
链接 : https://leetcode.cn/problems/longest-valid-parentheses/
================================================================

【题目描述】
找出字符串中最长的有效（正确闭合）括号子串，返回其长度。

【示例】
s = "(()"  →  2

【思路提示】
栈存下标（先压入哨兵 -1）；或用 DP：dp[i] 表示以 i 结尾的最长有效长度。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
