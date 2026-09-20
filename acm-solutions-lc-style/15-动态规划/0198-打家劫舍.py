# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 198    标题: 打家劫舍    难度: 中等    分类: 动态规划
# 链接: https://leetcode.cn/problems/house-robber/
# 运行: python3 "0198-打家劫舍.py"   （按提示输入，或重定向样例输入）

def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 在这里写你的代码
    prev = cur = 0
    for x in nums:
        prev, cur = cur, max(cur, prev + x)
    return cur


def main():
    nums = eval(input())
    print(rob(nums))


if __name__ == "__main__":
    main()


# 198. 打家劫舍  中等
#
# 【题目描述】
# 相邻房屋不能在同一晚被偷，求在不触发报警的前提下能偷到的最大金额。
#
# 【示例】
# nums = [2,7,9,3,1]  →  12
#
# 【思路提示】
# dp[i] = max(dp[i-1], dp[i-2] + nums[i])，同样可滚动优化空间。
#
# 【输入格式】
# 一行：每栋房屋金额，如 [2,7,9,3,1]。
#
# 【样例输入】
# [2,7,9,3,1]
# 【样例输出】
# 12
