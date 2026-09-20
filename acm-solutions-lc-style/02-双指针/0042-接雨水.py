# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 42    标题: 接雨水    难度: 困难    分类: 双指针
# 链接: https://leetcode.cn/problems/trapping-rain-water/
# 运行: python3 "0042-接雨水.py"   （按提示输入，或重定向样例输入）

def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # 在这里写你的代码
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    result = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            result += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            result += right_max - height[right]
            right -= 1
    return result


def main():
    height = eval(input())
    print(trap(height))


if __name__ == "__main__":
    main()


# 42. 接雨水  困难
#
# 【题目描述】
# 给定柱子高度数组，计算下雨之后这些柱子之间能接住多少雨水。
#
# 【示例】
# height = [0,1,0,2,1,0,1,3,2,1,2,1]  →  6
#
# 【思路提示】
# 每格存水量 = min(左侧最高, 右侧最高) - 当前高度；可用双指针或单调栈实现。
#
# 【输入格式】
# 一行：柱高列表，如 [0,1,0,2,1,0,1,3,2,1,2,1]。
#
# 【样例输入】
# [0,1,0,2,1,0,1,3,2,1,2,1]
# 【样例输出】
# 6
