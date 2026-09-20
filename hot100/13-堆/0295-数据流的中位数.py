# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 075 / 100 题
================================================================
题号 : 295
标题 : 数据流的中位数
难度 : 困难
分类 : 堆
链接 : https://leetcode.cn/problems/find-median-from-data-stream/
================================================================

【题目描述】
设计一个数据结构，支持不断添加整数，并随时返回当前所有元素的中位数。

【示例】
addNum(1), addNum(2), findMedian() → 1.5, addNum(3), findMedian() → 2.0

【思路提示】
对顶堆：大顶堆存较小的一半，小顶堆存较大的一半，保持两堆大小平衡。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


class MedianFinder:

    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        raise NotImplementedError

    def findMedian(self) -> float:
        raise NotImplementedError


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # obj = <按题目要求实例化上面的类>

    pass
