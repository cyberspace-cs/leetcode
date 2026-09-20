# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 64    标题: 最小路径和    难度: 中等    分类: 多维动态规划
# 链接: https://leetcode.cn/problems/minimum-path-sum/
# 运行: python3 "0064-最小路径和.py"   （按提示输入，或重定向样例输入）

def min_path_sum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # 在这里写你的代码（原地更新）
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i == 0:
                grid[i][j] += grid[i][j - 1]
            elif j == 0:
                grid[i][j] += grid[i - 1][j]
            else:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    return grid[m - 1][n - 1]


def main():
    grid = eval(input())
    print(min_path_sum(grid))


if __name__ == "__main__":
    main()


# 64. 最小路径和  中等
#
# 【题目描述】
# 在只能向右或向下移动的前提下，求从网格左上角到右下角的最小路径数字总和。
#
# 【示例】
# grid = [[1,3,1],[1,5,1],[4,2,1]]  →  7
#
# 【思路提示】
# 二维 DP，可直接原地更新网格，注意第一行与第一列的边界处理。
#
# 【输入格式】
# 一行：二维非负整数列表，如 [[1,3,1],[1,5,1],[4,2,1]]。
#
# 【样例输入】
# [[1,3,1],[1,5,1],[4,2,1]]
# 【样例输出】
# 7
