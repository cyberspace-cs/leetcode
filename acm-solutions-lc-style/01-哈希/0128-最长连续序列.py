# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 128    标题: 最长连续序列    难度: 中等    分类: 哈希
# 链接: https://leetcode.cn/problems/longest-consecutive-sequence/
# 运行: python3 "0128-最长连续序列.py"   （按提示输入，或重定向样例输入）

def longest_consecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 在这里写你的代码
    if not nums:
        return 0
    num_set = set(nums)
    max_length = 0
    for num in num_set:
        if num - 1 not in num_set:
            current = num
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            max_length = max(max_length, length)
    return max_length


def main():
    nums = eval(input())
    print(longest_consecutive(nums))


if __name__ == "__main__":
    main()


# 128. 最长连续序列  中等
#
# 【题目描述】
# 给定未排序整数数组 nums，找出数字连续的最长序列长度，要求算法时间复杂度 O(n)。
#
# 【示例】
# nums = [100,4,200,1,3,2]  →  4   # 最长连续序列为 1,2,3,4
#
# 【思路提示】
# 全部放入集合，仅从「没有前驱 x-1」的数字开始向后计数，避免重复扫描。
#
# 【输入格式】
# 一行：整数列表，如 [100,4,200,1,3,2]。
#
# 【样例输入】
# [100,4,200,1,3,2]
# 【样例输出】
# 4
