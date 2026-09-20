# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 4    标题: 寻找两个正序数组的中位数    难度: 困难    分类: 二分查找
# 链接: https://leetcode.cn/problems/median-of-two-sorted-arrays/
# 运行: python3 "0004-寻找两个正序数组的中位数.py"   （按提示输入，或重定向样例输入）

def find_median_sorted_arrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # 在这里写你的代码（在较短数组上二分划分点）
    a, b = nums1, nums2
    if len(a) > len(b):
        a, b = b, a
    n, m = len(a), len(b)
    total = n + m
    half = (total + 1) // 2
    lo, hi = 0, n
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        left_a = a[i - 1] if i > 0 else float("-inf")
        right_a = a[i] if i < n else float("inf")
        left_b = b[j - 1] if j > 0 else float("-inf")
        right_b = b[j] if j < m else float("inf")
        if left_a > right_b:
            hi = i - 1
        elif left_b > right_a:
            lo = i + 1
        else:
            if total % 2:
                return float(max(left_a, left_b))
            return (max(left_a, left_b) + min(right_a, right_b)) / 2.0
    return 0.0


def main():
    nums1 = eval(input())
    nums2 = eval(input())
    print(find_median_sorted_arrays(nums1, nums2))


if __name__ == "__main__":
    main()


# 4. 寻找两个正序数组的中位数  困难
#
# 【题目描述】
# 给定两个正序数组，返回它们合并后的中位数，要求时间复杂度 O(log(m+n))。
#
# 【示例】
# nums1 = [1,3], nums2 = [2]  →  2.0
#
# 【思路提示】
# 在较短数组上二分划分点，使左半部分元素总数正确且「左最大 ≤ 右最小」。
#
# 【输入格式】
# 第一行：升序数组1；第二行：升序数组2。
#
# 【样例输入】
# [1,3]
# [2]
# 【样例输出】
# 2.0
