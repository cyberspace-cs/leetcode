# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 118    标题: 杨辉三角    难度: 简单    分类: 动态规划
# 链接: https://leetcode.cn/problems/pascals-triangle/
# 运行: python3 "0118-杨辉三角.py"   （按提示输入，或重定向样例输入）

def generate(num_rows):
    """
    :type num_rows: int
    :rtype: List[List[int]]
    """
    # 在这里写你的代码
    res = []
    row = []
    for _ in range(num_rows):
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1] if row else [1]
        res.append(row)
    return res


def main():
    num_rows = int(input())
    print(generate(num_rows))


if __name__ == "__main__":
    main()


# 118. 杨辉三角  简单
#
# 【题目描述】
# 生成杨辉三角的前 numRows 行。
#
# 【示例】
# numRows = 5  →  [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
# 【思路提示】
# 逐行构造：每行两端为 1，中间元素等于上一行相邻两数之和。
#
# 【输入格式】
# 一行：numRows（行数）。
#
# 【样例输入】
# 5
# 【样例输出】
# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
