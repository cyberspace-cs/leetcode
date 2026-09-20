# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 240    标题: 搜索二维矩阵 II    难度: 中等    分类: 矩阵
# 链接: https://leetcode.cn/problems/search-a-2d-matrix-ii/
# 运行: python3 "0240-搜索二维矩阵 II.py"   （按提示输入，或重定向样例输入）

def search_matrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    # 在这里写你的代码（从右上角出发）
    if not matrix:
        return False
    i, j = 0, len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target:
            return True
        if matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return False


def main():
    matrix = eval(input())
    target = int(input())
    print(search_matrix(matrix, target))


if __name__ == "__main__":
    main()


# 240. 搜索二维矩阵 II  中等
#
# 【题目描述】
# 在每行从左到右、每列从上到下均递增的矩阵中查找目标值是否存在。
#
# 【示例】
# matrix = [[1,4,7],[2,5,8],[3,6,9]], target = 5  →  true
#
# 【思路提示】
# 从右上角出发：当前值大于目标则左移一列，小于目标则下移一行。
#
# 【输入格式】
# 第一行：二维列表（每行每列均升序）；第二行：target。
#
# 【样例输入】
# [[1,4,7],[2,5,8],[3,6,9]]
# 5
# 【样例输出】
# True
