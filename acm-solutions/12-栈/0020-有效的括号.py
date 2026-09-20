# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 20
标题 : 有效的括号
难度 : 简单
分类 : 栈
链接 : https://leetcode.cn/problems/valid-parentheses/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
一行：字符串 s（仅含 ()[]{} ）。

【输出格式】
一行，true 或 false。

【样例输入】
3
()[]{}
(]
([)]

【样例输出】
true
false
false

"""

import sys


def solve(it):
    s = next(it)
    pair = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if not stack or stack.pop() != pair[c]:
                return "false"
    return "true" if not stack else "false"

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
