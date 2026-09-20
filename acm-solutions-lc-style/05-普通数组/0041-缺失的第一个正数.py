# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 41    标题: 缺失的第一个正数    难度: 困难    分类: 普通数组
# 链接: https://leetcode.cn/problems/first-missing-positive/
# 运行: python3 "0041-缺失的第一个正数.py"   （按提示输入，或重定向样例输入）

def first_missing_positive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 在这里写你的代码（原地哈希）
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1


def main():
    nums = eval(input())
    print(first_missing_positive(nums))


if __name__ == "__main__":
    main()


# 41. 缺失的第一个正数  困难
#
# 【题目描述】
# 找出未在数组中出现的最小正整数，要求 O(n) 时间、O(1) 额外空间。
#
# 【示例】
# nums = [3,4,-1,1]  →  2
#
# 【思路提示】
# 原地哈希：把数值 x 交换到下标 x-1 处，再找第一个 nums[i] != i+1 的位置。
#
# 【输入格式】
# 一行：整数列表，如 [3,4,-1,1]。
#
# 【样例输入】
# [3,4,-1,1]
# 【样例输出】
# 2
