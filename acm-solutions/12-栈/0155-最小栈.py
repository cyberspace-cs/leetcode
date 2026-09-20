# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 155
标题 : 最小栈
难度 : 中等
分类 : 栈
链接 : https://leetcode.cn/problems/min-stack/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：q；随后 q 行，每行为 push x / pop / top / getMin。

【输出格式】
一行，按顺序输出所有 top 与 getMin 的结果（空格分隔）；若无输出则输出 EMPTY。

【样例输入】
1
7
push -2
push 0
push -3
getMin
pop
top
getMin

【样例输出】
-3 0 -2

"""

import sys


def solve(it):
    q = int(next(it))
    stack = []
    mins = []
    out = []
    for _ in range(q):
        op = next(it)
        if op == "push":
            x = int(next(it))
            stack.append(x)
            mins.append(x if not mins else min(x, mins[-1]))
        elif op == "pop":
            stack.pop()
            mins.pop()
        elif op == "top":
            out.append(str(stack[-1]))
        else:
            out.append(str(mins[-1]))
    return " ".join(out) if out else "EMPTY"

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
