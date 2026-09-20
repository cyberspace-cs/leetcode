# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 071 / 100 题
================================================================
题号 : 155
标题 : 最小栈
难度 : 中等
分类 : 栈
链接 : https://leetcode.cn/problems/min-stack/
================================================================

【题目描述】
设计一个支持 push、pop、top 操作，并能在常数时间内检索到最小元素的栈。

【示例】
push(-2), push(0), push(-3), getMin() → -3, pop(), getMin() → -2

【思路提示】
使用辅助栈与主栈同步记录「当前最小值」。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class MinStack:

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        raise NotImplementedError

    def pop(self) -> None:
        raise NotImplementedError

    def top(self) -> int:
        raise NotImplementedError

    def getMin(self) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # obj = <按题目要求实例化上面的类>

    pass
