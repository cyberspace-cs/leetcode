# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 152    标题: 乘积最大子数组    难度: 中等    分类: 动态规划
# 链接: https://leetcode.cn/problems/maximum-product-subarray/
# 运行: python3 "0152-乘积最大子数组.py"   （按提示输入，或重定向样例输入）

def max_product(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 在这里写你的代码（同时维护最大 / 最小乘积）
    hi = lo = best = nums[0]
    for x in nums[1:]:
        if x < 0:
            hi, lo = lo, hi
        hi = max(x, hi * x)
        lo = min(x, lo * x)
        best = max(best, hi)
    return best


def main():
    nums = eval(input())
    print(max_product(nums))


if __name__ == "__main__":
    main()


# 152. 乘积最大子数组  中等
#
# 【题目描述】
# 找出数组中乘积最大的连续子数组，返回该乘积。
#
# 【示例】
# nums = [2,3,-2,4]  →  6   # [2,3]
#
# 【思路提示】
# 同时维护以 i 结尾的最大乘积与最小乘积，因为负数相乘会翻转大小关系。
#
# 【输入格式】
# 一行：整数列表，如 [2,3,-2,4]。
#
# 【样例输入】
# [2,3,-2,4]
# 【样例输出】
# 6
