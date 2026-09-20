# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 200    标题: 岛屿数量    难度: 中等    分类: 图论
# 链接: https://leetcode.cn/problems/number-of-islands/
# 运行: python3 "0200-岛屿数量.py"   （按提示输入，或重定向样例输入）

def num_islands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    # 在这里写你的代码（DFS 洪水填充）
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    seen = [[False] * n for _ in range(m)]
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and not seen[i][j]:
                count += 1
                seen[i][j] = True
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1" and not seen[nx][ny]:
                            seen[nx][ny] = True
                            stack.append((nx, ny))
    return count


def main():
    grid = eval(input())
    print(num_islands(grid))


if __name__ == "__main__":
    main()


# 200. 岛屿数量  中等
#
# 【题目描述】
# 给定由 "1"（陆地）和 "0"（水）组成的二维网格，统计岛屿（上下左右相连的陆地）数量。
#
# 【示例】
# grid = [["1","1","0"],["1","0","0"],["0","0","1"]]  →  2
#
# 【思路提示】
# DFS / BFS 洪水填充，把访问过的陆地标记掉；也可用并查集。
#
# 【输入格式】
# 一行：二维字符网格，如 [["1","1","0"],["1","0","0"],["0","0","1"]]。
#
# 【样例输入】
# [["1","1","0"],["1","0","0"],["0","0","1"]]
# 【样例输出】
# 2
