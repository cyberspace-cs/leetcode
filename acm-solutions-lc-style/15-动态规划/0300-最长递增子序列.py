# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 300    标题: 最长递增子序列    难度: 中等    分类: 动态规划
# 链接: https://leetcode.cn/problems/longest-increasing-subsequence/
# 运行: python3 "0300-最长递增子序列.py"   （按提示输入，或重定向样例输入）

def length_of_lis(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 在这里写你的代码（贪心 + 二分）
    import bisect
    tails = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def main():
    nums = eval(input())
    print(length_of_lis(nums))


if __name__ == "__main__":
    main()


# 300. 最长递增子序列  中等
#
# 【题目描述】
# 求数组中最长严格递增子序列的长度（子序列不必连续）。
#
# 【示例】
# nums = [10,9,2,5,3,7,101,18]  →  4   # [2,3,7,101]
#
# 【思路提示】
# O(n²) 的 DP 定义；进阶用「贪心 + 二分」维护长度为 L 的最小结尾值，做到 O(n log n)。
#
# 【输入格式】
# 一行：整数列表，如 [10,9,2,5,3,7,101,18]。
#
# 【样例输入】
# [10,9,2,5,3,7,101,18]
# 【样例输出】
# 4
