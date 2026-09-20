# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 295    标题: 数据流的中位数    难度: 困难    分类: 堆
# 链接: https://leetcode.cn/problems/find-median-from-data-stream/
# 运行: python3 "0295-数据流的中位数.py"   （按提示输入，或重定向样例输入）

class MedianFinder:
    """
    :rtype: None
    """

    def __init__(self):
        # 在这里写你的代码（对顶堆：大顶堆存较小一半，小顶堆存较大一半）
        import heapq
        self.heapq = heapq
        self.small = []
        self.large = []

    def add_num(self, num: int) -> None:
        # 在这里写你的代码
        self.heapq.heappush(self.small, -num)
        self.heapq.heappush(self.large, -self.heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            self.heapq.heappush(self.small, -self.heapq.heappop(self.large))

    def find_median(self) -> float:
        # 在这里写你的代码
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


def main():
    ops = eval(input())
    mf = MedianFinder()
    out = []
    for op in ops:
        if op[0] == "addNum":
            mf.add_num(op[1])
        else:
            out.append(mf.find_median())
    print(out)


if __name__ == "__main__":
    main()


# 295. 数据流的中位数  困难
#
# 【题目描述】
# 设计一个数据结构，支持不断添加整数，并随时返回当前所有元素的中位数。
#
# 【示例】
# addNum(1), addNum(2), findMedian() → 1.5, addNum(3), findMedian() → 2.0
#
# 【思路提示】
# 对顶堆：大顶堆存较小的一半，小顶堆存较大的一半，保持两堆大小平衡。
#
# 【输入格式】
# 一行：操作列表，如 [["addNum",1],["addNum",2],["findMedian"]]。
#
# 【样例输入】
# [["addNum",1],["addNum",2],["findMedian"],["addNum",3],["findMedian"]]
# 【样例输出】
# [1.5, 2.0]
