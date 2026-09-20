# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 33
标题 : 搜索旋转排序数组
难度 : 中等
分类 : 二分查找
链接 : https://leetcode.cn/problems/search-in-rotated-sorted-array/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n target；第二行：n 个互不相同的整数（由升序数组旋转得到）。

【输出格式】
一行，目标值下标；不存在输出 -1。

【样例输入】
3
7 0
4 5 6 7 0 1 2
7 3
4 5 6 7 0 1 2
1 3
1

【样例输出】
4
-1
-1

"""

import sys


def solve(it):
    n = int(next(it))
    target = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    lo, hi = 0, n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[lo] <= a[mid]:
            if a[lo] <= target < a[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if a[mid] < target <= a[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        out.append(str(solve(it)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
