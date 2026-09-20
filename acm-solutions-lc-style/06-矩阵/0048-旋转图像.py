# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 48    标题: 旋转图像    难度: 中等    分类: 矩阵
# 链接: https://leetcode.cn/problems/rotate-image/
# 运行: python3 "0048-旋转图像.py"   （按提示输入，或重定向样例输入）

def rotate_matrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    # 在这里写你的代码（原地旋转后返回）
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix


def main():
    matrix = eval(input())
    print(rotate_matrix(matrix))


if __name__ == "__main__":
    main()


# 48. 旋转图像  中等
#
# 【题目描述】
# 把 n×n 的二维矩阵顺时针旋转 90°，要求原地完成。
#
# 【示例】
# matrix = [[1,2,3],[4,5,6],[7,8,9]]  →  [[7,4,1],[8,5,2],[9,6,3]]
#
# 【思路提示】
# 先沿主对角线做转置，再对每一行做左右翻转。
#
# 【输入格式】
# 一行：n×n 二维列表，如 [[1,2,3],[4,5,6],[7,8,9]]。
#
# 【样例输入】
# [[1,2,3],[4,5,6],[7,8,9]]
# 【样例输出】
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
