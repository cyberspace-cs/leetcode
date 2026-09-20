# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 53    标题: 最大子数组和    难度: 中等    分类: 普通数组
# 链接: https://leetcode.cn/problems/maximum-subarray/
# 运行: python3 "0053-最大子数组和.py"   （按提示输入，或重定向样例输入）

def max_sub_array(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 在这里写你的代码
    cur = best = nums[0]
    for x in nums[1:]:
        cur = x if cur < 0 else cur + x
        best = max(best, cur)
    return best


def main():
    nums = eval(input())
    print(max_sub_array(nums))


if __name__ == "__main__":
    main()


# 53. 最大子数组和  中等
#
# 【题目描述】
# 给定整数数组，找出和最大的连续子数组，返回其最大和。
#
# 【示例】
# nums = [-2,1,-3,4,-1,2,1,-5,4]  →  6   # 子数组 [4,-1,2,1]
#
# 【思路提示】
# Kadane 算法：cur = max(x, cur + x)，同时维护全局最大值。
#
# 【输入格式】
# 一行：整数列表，如 [-2,1,-3,4,-1,2,1,-5,4]。
#
# 【样例输入】
# [-2,1,-3,4,-1,2,1,-5,4]
# 【样例输出】
# 6
