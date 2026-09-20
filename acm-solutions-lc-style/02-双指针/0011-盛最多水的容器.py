# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 11    标题: 盛最多水的容器    难度: 中等    分类: 双指针
# 链接: https://leetcode.cn/problems/container-with-most-water/
# 运行: python3 "0011-盛最多水的容器.py"   （按提示输入，或重定向样例输入）

def max_area(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # 在这里写你的代码
    ans = 0
    left, right = 0, len(height) - 1
    while left < right:
        h = min(height[left], height[right])
        ans = max(ans, h * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return ans


def main():
    height = eval(input())
    print(max_area(height))


if __name__ == "__main__":
    main()


# 11. 盛最多水的容器  中等
#
# 【题目描述】
# 给定高度数组 height，选出两条竖线，使它们与 x 轴围成的容器能盛最多的水。
#
# 【示例】
# height = [1,8,6,2,5,4,8,3,7]  →  49
#
# 【思路提示】
# 左右双指针向中间收缩，每次移动较矮的一侧（面积由短板决定）。
#
# 【输入格式】
# 一行：高度列表，如 [1,8,6,2,5,4,8,3,7]。
#
# 【样例输入】
# [1,8,6,2,5,4,8,3,7]
# 【样例输出】
# 49
