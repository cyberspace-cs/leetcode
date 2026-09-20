# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 994    标题: 腐烂的橘子    难度: 中等    分类: 图论
# 链接: https://leetcode.cn/problems/rotting-oranges/
# 运行: python3 "0994-腐烂的橘子.py"   （按提示输入，或重定向样例输入）

def oranges_rotting(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # 在这里写你的代码（多源 BFS）
    from collections import deque
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    dq = deque()
    fresh = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                dq.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1
    minutes = 0
    while dq:
        i, j, t = dq.popleft()
        minutes = max(minutes, t)
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                grid[x][y] = 2
                fresh -= 1
                dq.append((x, y, t + 1))
    return minutes if fresh == 0 else -1


def main():
    grid = eval(input())
    print(oranges_rotting(grid))


if __name__ == "__main__":
    main()


# 994. 腐烂的橘子  中等
#
# 【题目描述】
# 每分钟腐烂橘子会感染上下左右相邻的新鲜橘子，返回所有橘子腐烂所需的最少分钟数；不可能则返回 -1。
#
# 【示例】
# grid = [[2,1,1],[1,1,0],[0,1,1]]  →  4
#
# 【思路提示】
# 多源 BFS：把所有腐烂橘子入队，按层扩展并计时。
#
# 【输入格式】
# 一行：二维整数网格（0 空格 / 1 新鲜 / 2 腐烂）。
#
# 【样例输入】
# [[2,1,1],[1,1,0],[0,1,1]]
# 【样例输出】
# 4
