# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 34    标题: 在排序数组中查找元素的第一个和最后一个位置    难度: 中等    分类: 二分查找
# 链接: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
# 运行: python3 "0034-在排序数组中查找元素的第一个和最后一个位置.py"   （按提示输入，或重定向样例输入）

def search_range(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # 在这里写你的代码（两次二分求左右边界）
    def lower_bound(x):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    left = lower_bound(target)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    return [left, lower_bound(target + 1) - 1]


def main():
    nums = eval(input())
    target = int(input())
    print(search_range(nums, target))


if __name__ == "__main__":
    main()


# 34. 在排序数组中查找元素的第一个和最后一个位置  中等
#
# 【题目描述】
# 返回目标值在升序数组中的起始与结束下标；不存在则返回 [-1,-1]。
#
# 【示例】
# nums = [5,7,7,8,8,10], target = 8  →  [3,4]
#
# 【思路提示】
# 两次二分：一次求左边界（找第一个 >= target），一次求右边界（找最后一个 <= target）。
#
# 【输入格式】
# 第一行：升序整数列表；第二行：target。
#
# 【样例输入】
# [5,7,7,8,8,10]
# 8
# 【样例输出】
# [3, 4]
