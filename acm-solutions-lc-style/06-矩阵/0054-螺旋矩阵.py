# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 54    标题: 螺旋矩阵    难度: 中等    分类: 矩阵
# 链接: https://leetcode.cn/problems/spiral-matrix/
# 运行: python3 "0054-螺旋矩阵.py"   （按提示输入，或重定向样例输入）

def spiral_order(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    # 在这里写你的代码
    if not matrix:
        return []
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            res.append(matrix[top][j])
        top += 1
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    return res


def main():
    matrix = eval(input())
    print(spiral_order(matrix))


if __name__ == "__main__":
    main()


# 54. 螺旋矩阵  中等
#
# 【题目描述】
# 按顺时针螺旋顺序返回矩阵中的所有元素。
#
# 【示例】
# matrix = [[1,2,3],[4,5,6],[7,8,9]]  →  [1,2,3,6,9,8,7,4,5]
#
# 【思路提示】
# 维护上、下、左、右四个边界，逐层向内收缩。
#
# 【输入格式】
# 一行：二维列表，如 [[1,2,3],[4,5,6],[7,8,9]]。
#
# 【样例输入】
# [[1,2,3],[4,5,6],[7,8,9]]
# 【样例输出】
# [1, 2, 3, 6, 9, 8, 7, 4, 5]
