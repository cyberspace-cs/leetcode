# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 45    标题: 跳跃游戏 II    难度: 中等    分类: 贪心算法
# 链接: https://leetcode.cn/problems/jump-game-ii/
# 运行: python3 "0045-跳跃游戏 II.py"   （按提示输入，或重定向样例输入）

def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 在这里写你的代码（贪心分层）
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps


def main():
    nums = eval(input())
    print(jump(nums))


if __name__ == "__main__":
    main()


# 45. 跳跃游戏 II  中等
#
# 【题目描述】
# 在保证能到达终点的前提下，求跳到最后一个位置所需的最少跳跃次数。
#
# 【示例】
# nums = [2,3,1,1,4]  →  2
#
# 【思路提示】
# 贪心分层：在当前一步能覆盖的范围内，选择能跳到最远的位置作为下一步。
#
# 【输入格式】
# 一行：每格最大跳跃长度（保证可到达终点），如 [2,3,1,1,4]。
#
# 【样例输入】
# [2,3,1,1,4]
# 【样例输出】
# 2
