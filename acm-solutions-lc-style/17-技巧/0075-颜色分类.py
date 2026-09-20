# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 75    标题: 颜色分类    难度: 中等    分类: 技巧
# 链接: https://leetcode.cn/problems/sort-colors/
# 运行: python3 "0075-颜色分类.py"   （按提示输入，或重定向样例输入）

def sort_colors(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # 在这里写你的代码（荷兰国旗三指针）
    p0, i, p2 = 0, 0, len(nums) - 1
    while i <= p2:
        if nums[i] == 0:
            nums[p0], nums[i] = nums[i], nums[p0]
            p0 += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[p2] = nums[p2], nums[i]
            p2 -= 1
        else:
            i += 1
    return nums


def main():
    nums = eval(input())
    print(sort_colors(nums))


if __name__ == "__main__":
    main()


# 75. 颜色分类  中等
#
# 【题目描述】
# 给定只含 0、1、2 的数组，原地排序使相同元素相邻并按 0、1、2 顺序排列；不能使用库排序。
#
# 【示例】
# nums = [2,0,2,1,1,0]  →  [0,0,1,1,2,2]
#
# 【思路提示】
# 荷兰国旗问题：用 p0、i、p2 三个指针一次遍历完成分区。
#
# 【输入格式】
# 一行：只含 0、1、2 的列表，如 [2,0,2,1,1,0]。
#
# 【样例输入】
# [2,0,2,1,1,0]
# 【样例输出】
# [0, 0, 1, 1, 2, 2]
