# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 46
标题 : 全排列
难度 : 中等
分类 : 回溯
链接 : https://leetcode.cn/problems/permutations/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个互不相同的整数。

【输出格式】
第一行：排列个数 g；随后 g 行，每行一个排列（空格分隔），按回溯顺序输出。

【样例输入】
2
3
1 2 3
2
0 1

【样例输出】
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
2
0 1
1 0

"""

import sys


def solve(it):
    n = int(next(it))
    nums = [int(next(it)) for _ in range(n)]
    res = []
    used = [False] * n
    path = []

    def bt():
        if len(path) == n:
            res.append(" ".join(map(str, path)))
            return
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            bt()
            path.pop()
            used[i] = False

    bt()
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
