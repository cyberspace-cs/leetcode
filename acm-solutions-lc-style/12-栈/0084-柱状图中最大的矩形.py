# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 84    标题: 柱状图中最大的矩形    难度: 困难    分类: 栈
# 链接: https://leetcode.cn/problems/largest-rectangle-in-histogram/
# 运行: python3 "0084-柱状图中最大的矩形.py"   （按提示输入，或重定向样例输入）

def largest_rectangle_area(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    # 在这里写你的代码（单调递增栈，首尾补 0）
    hs = list(heights) + [0]
    stack = []
    best = 0
    for i, h in enumerate(hs):
        while stack and hs[stack[-1]] > h:
            j = stack.pop()
            left = stack[-1] if stack else -1
            best = max(best, hs[j] * (i - left - 1))
        stack.append(i)
    return best


def main():
    heights = eval(input())
    print(largest_rectangle_area(heights))


if __name__ == "__main__":
    main()


# 84. 柱状图中最大的矩形  困难
#
# 【题目描述】
# 给定柱状图中各柱子的高度，求其中能勾勒出的最大矩形面积。
#
# 【示例】
# heights = [2,1,5,6,2,3]  →  10
#
# 【思路提示】
# 单调递增栈（首尾各补一个 0），弹栈时以该柱高为矩形高计算面积。
#
# 【输入格式】
# 一行：柱高列表，如 [2,1,5,6,2,3]。
#
# 【样例输入】
# [2,1,5,6,2,3]
# 【样例输出】
# 10
