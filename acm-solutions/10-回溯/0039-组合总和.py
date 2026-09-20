# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 39
标题 : 组合总和
难度 : 中等
分类 : 回溯
链接 : https://leetcode.cn/problems/combination-sum/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n target；第二行：n 个互不相同的正整数。

【输出格式】
第一行：方案数 g；随后 g 行，每行一个非递减组合（空格分隔）；无解时仅输出 0。

【样例输入】
2
4 7
2 3 6 7
1 1
2

【样例输出】
2
2 2 3
7
0

"""

import sys


def solve(it):
    n = int(next(it))
    target = int(next(it))
    cand = sorted(int(next(it)) for _ in range(n))
    res = []
    path = []

    def bt(start, remain):
        if remain == 0:
            res.append(" ".join(map(str, path)))
            return
        for i in range(start, n):
            if cand[i] > remain:
                break
            path.append(cand[i])
            bt(i, remain - cand[i])
            path.pop()

    bt(0, target)
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
