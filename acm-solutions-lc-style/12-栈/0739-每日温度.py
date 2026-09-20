# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 739    标题: 每日温度    难度: 中等    分类: 栈
# 链接: https://leetcode.cn/problems/daily-temperatures/
# 运行: python3 "0739-每日温度.py"   （按提示输入，或重定向样例输入）

def daily_temperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    # 在这里写你的代码（单调递减栈）
    n = len(temperatures)
    res = [0] * n
    stack = []
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res


def main():
    temperatures = eval(input())
    print(daily_temperatures(temperatures))


if __name__ == "__main__":
    main()


# 739. 每日温度  中等
#
# 【题目描述】
# 给定每日温度，返回每天需要等待多少天才会出现更高的温度；不会出现则记为 0。
#
# 【示例】
# temperatures = [73,74,75,71,69,72,76,73]  →  [1,1,4,2,1,1,0,0]
#
# 【思路提示】
# 单调递减栈存下标，遇到更高温度时不断弹栈并结算答案。
#
# 【输入格式】
# 一行：每日温度列表，如 [73,74,75,71,69,72,76,73]。
#
# 【样例输入】
# [73,74,75,71,69,72,76,73]
# 【样例输出】
# [1, 1, 4, 2, 1, 1, 0, 0]
