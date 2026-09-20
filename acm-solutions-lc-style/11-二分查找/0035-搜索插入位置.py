# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 35    标题: 搜索插入位置    难度: 简单    分类: 二分查找
# 链接: https://leetcode.cn/problems/search-insert-position/
# 运行: python3 "0035-搜索插入位置.py"   （按提示输入，或重定向样例输入）

def search_insert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # 在这里写你的代码
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def main():
    nums = eval(input())
    target = int(input())
    print(search_insert(nums, target))


if __name__ == "__main__":
    main()


# 35. 搜索插入位置  简单
#
# 【题目描述】
# 在升序数组中查找目标值，存在则返回下标，不存在则返回它应被插入的位置。
#
# 【示例】
# nums = [1,3,5,6], target = 5  →  2
#
# 【思路提示】
# 标准二分查找，循环结束时返回左边界 left。
#
# 【输入格式】
# 第一行：升序整数列表；第二行：target。
#
# 【样例输入】
# [1,3,5,6]
# 5
# 【样例输出】
# 2
