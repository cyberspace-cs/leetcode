# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 74    标题: 搜索二维矩阵    难度: 中等    分类: 二分查找
# 链接: https://leetcode.cn/problems/search-a-2d-matrix/
# 运行: python3 "0074-搜索二维矩阵.py"   （按提示输入，或重定向样例输入）

def search_matrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    # 在这里写你的代码（整体视为一维升序数组做二分）
    if not matrix:
        return False
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        v = matrix[mid // n][mid % n]
        if v == target:
            return True
        if v < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


def main():
    matrix = eval(input())
    target = int(input())
    print(search_matrix(matrix, target))


if __name__ == "__main__":
    main()


# 74. 搜索二维矩阵  中等
#
# 【题目描述】
# 在每行升序、且每行首元素大于上一行末元素的矩阵中查找目标值。
#
# 【示例】
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3  →  true
#
# 【思路提示】
# 把二维矩阵视为一维有序数组做二分，通过 divmod 完成下标映射。
#
# 【输入格式】
# 第一行：二维列表（每行升序，且每行首元素大于上一行末元素）；第二行：target。
#
# 【样例输入】
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# 3
# 【样例输出】
# True
