# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 056 / 100 题
================================================================
题号 : 22
标题 : 括号生成
难度 : 中等
分类 : 回溯
链接 : https://leetcode.cn/problems/generate-parentheses/
================================================================

【题目描述】
生成所有由 n 对括号组成的有效（正确闭合）组合。

【示例】
n = 3  →  ["((()))","(()())","(())()","()(())","()()()"]

【思路提示】
回溯：左括号数 < n 时可加左括号；右括号数 < 左括号数时可加右括号。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
