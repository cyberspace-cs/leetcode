# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 084 / 100 题
================================================================
题号 : 139
标题 : 单词拆分
难度 : 中等
分类 : 动态规划
链接 : https://leetcode.cn/problems/word-break/
================================================================

【题目描述】
判断字符串能否被拆分成字典中出现的一个或多个单词。

【示例】
s = "leetcode", wordDict = ["leet","code"]  →  true

【思路提示】
dp[i] 表示前 i 个字符可被拆分，枚举末尾单词并查表转移。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
