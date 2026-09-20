# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 1    标题: 两数之和    难度: 简单    分类: 哈希
# 链接: https://leetcode.cn/problems/two-sum/
# 运行: python3 "0001-两数之和.py"   （按提示输入，或重定向样例输入）

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # 在这里写你的代码
    hashmap = {}
    for i, x in enumerate(nums):
        if target - x in hashmap:
            return [hashmap[target - x], i]
        hashmap[x] = i
    return []


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())
    print(two_sum(nums, target))


if __name__ == "__main__":
    main()


# 1. 两数之和  简单
#
# 【题目描述】
# 给定整数数组 nums 和整数目标值 target，在数组中找出和为 target 的两个整数，返回它们的数组下标（保证只有一组有效答案）。
#
# 【示例】
# nums = [2,7,11,15], target = 9  →  [0,1]
#
# 【思路提示】
# 哈希表存「值 → 下标」，边遍历边查 target - n。
#
# 【输入格式】
# 第一行：n；第二行：n 个整数；第三行：target。
#
# 【样例输入】
# 4
# 2 7 11 15
# 9
# 【样例输出】
# [0, 1]
