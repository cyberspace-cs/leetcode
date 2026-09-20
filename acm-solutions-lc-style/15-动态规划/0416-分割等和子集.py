# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 416    标题: 分割等和子集    难度: 中等    分类: 动态规划
# 链接: https://leetcode.cn/problems/partition-equal-subset-sum/
# 运行: python3 "0416-分割等和子集.py"   （按提示输入，或重定向样例输入）

def can_partition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # 在这里写你的代码（01 背包）
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for j in range(target, x - 1, -1):
            if dp[j - x]:
                dp[j] = True
    return dp[target]


def main():
    nums = eval(input())
    print(can_partition(nums))


if __name__ == "__main__":
    main()


# 416. 分割等和子集  中等
#
# 【题目描述】
# 判断能否把数组分割成两个元素和相等的子集。
#
# 【示例】
# nums = [1,5,11,5]  →  true   # [1,5,5] 与 [11]
#
# 【思路提示】
# 01 背包：目标和为 sum/2，dp[j] 表示能否恰好凑出 j（倒序枚举容量）。
#
# 【输入格式】
# 一行：正整数列表，如 [1,5,11,5]。
#
# 【样例输入】
# [1,5,11,5]
# 【样例输出】
# True
