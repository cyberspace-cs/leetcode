# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 092 / 100 题
================================================================
题号 : 62
标题 : 不同路径
难度 : 中等
分类 : 多维动态规划
链接 : https://leetcode.cn/problems/unique-paths/
================================================================

【题目描述】
机器人位于 m×n 网格左上角，每次只能向右或向下移动一步，求到达右下角的不同路径数。

【示例】
m = 3, n = 7  →  28

【思路提示】
dp[i][j] = dp[i-1][j] + dp[i][j-1]，可压缩为一维数组。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
