# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 78
标题 : 子集
难度 : 中等
分类 : 回溯
链接 : https://leetcode.cn/problems/subsets/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个互不相同的整数。

【输出格式】
第一行：子集个数 g；随后 g 行，每行一个子集（空格分隔）。
空子集输出为一个空行；整体按回溯顺序（依次选择 / 不选择）。

【样例输入】
1
3
1 2 3

【样例输出】
8

1
1 2
1 2 3
1 3
2
2 3
3

"""

import sys


def solve(it):
    n = int(next(it))
    nums = [int(next(it)) for _ in range(n)]
    res = []
    path = []

    def bt(start):
        res.append(" ".join(map(str, path)))
        for i in range(start, n):
            path.append(nums[i])
            bt(i + 1)
            path.pop()

    bt(0)
    return "\n".join([str(len(res))] + res)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        out.append(str(solve(it)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
