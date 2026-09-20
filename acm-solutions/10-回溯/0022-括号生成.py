# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 22
标题 : 括号生成
难度 : 中等
分类 : 回溯
链接 : https://leetcode.cn/problems/generate-parentheses/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
一行：n，表示括号对数。

【输出格式】
第一行：方案数 g；随后 g 行，每行一个合法括号串。

【样例输入】
2
3
1

【样例输出】
5
((()))
(()())
(())()
()(())
()()()
1
()

"""

import sys


def solve(it):
    n = int(next(it))
    res = []

    def bt(cur, left, right):
        if len(cur) == 2 * n:
            res.append(cur)
            return
        if left < n:
            bt(cur + "(", left + 1, right)
        if right < left:
            bt(cur + ")", left, right + 1)

    bt("", 0, 0)
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
