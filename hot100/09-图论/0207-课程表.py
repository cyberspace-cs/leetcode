# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 052 / 100 题
================================================================
题号 : 207
标题 : 课程表
难度 : 中等
分类 : 图论
链接 : https://leetcode.cn/problems/course-schedule/
================================================================

【题目描述】
给定课程数与先修关系，判断能否修完所有课程（即依赖图是否存在环）。

【示例】
numCourses = 2, prerequisites = [[1,0]]  →  true

【思路提示】
拓扑排序（Kahn + 入度队列）；或 DFS 三色标记检测环。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
