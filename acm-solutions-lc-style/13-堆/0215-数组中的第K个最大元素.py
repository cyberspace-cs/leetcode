# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 215    标题: 数组中的第K个最大元素    难度: 中等    分类: 堆
# 链接: https://leetcode.cn/problems/kth-largest-element-in-an-array/
# 运行: python3 "0215-数组中的第K个最大元素.py"   （按提示输入，或重定向样例输入）

def find_kth_largest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # 在这里写你的代码（大小为 k 的小顶堆）
    import heapq
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def main():
    nums = eval(input())
    k = int(input())
    print(find_kth_largest(nums, k))


if __name__ == "__main__":
    main()


# 215. 数组中的第K个最大元素  中等
#
# 【题目描述】
# 返回数组中第 k 个最大的元素（按排序后的位置计，不去重）。
#
# 【示例】
# nums = [3,2,1,5,6,4], k = 2  →  5
#
# 【思路提示】
# 维护大小为 k 的小顶堆；或用快速选择（平均 O(n)）。
#
# 【输入格式】
# 第一行：整数列表；第二行：k。
#
# 【样例输入】
# [3,2,1,5,6,4]
# 2
# 【样例输出】
# 5
