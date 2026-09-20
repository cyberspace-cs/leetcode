# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 73    标题: 矩阵置零    难度: 中等    分类: 矩阵
# 链接: https://leetcode.cn/problems/set-matrix-zeroes/
# 运行: python3 "0073-矩阵置零.py"   （按提示输入，或重定向样例输入）

def set_zeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    # 在这里写你的代码（原地修改 matrix 后返回）
    m, n = len(matrix), len(matrix[0])
    rows = [False] * m
    cols = [False] * n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in range(m):
        for j in range(n):
            if rows[i] or cols[j]:
                matrix[i][j] = 0
    return matrix


def main():
    matrix = eval(input())
    print(set_zeroes(matrix))


if __name__ == "__main__":
    main()


# 73. 矩阵置零  中等
#
# 【题目描述】
# 若矩阵中某元素为 0，则把它所在的行和列全部置为 0，要求原地修改。
#
# 【示例】
# matrix = [[1,1,1],[1,0,1],[1,1,1]]  →  [[1,0,1],[0,0,0],[1,0,1]]
#
# 【思路提示】
# 用首行、首列充当标记数组，并单独记录首行/首列本身是否需要置零。
#
# 【输入格式】
# 一行：二维列表，如 [[1,1,1],[1,0,1],[1,1,1]]。
#
# 【样例输入】
# [[1,1,1],[1,0,1],[1,1,1]]
# 【样例输出】
# [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
