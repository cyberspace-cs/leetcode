# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 394
标题 : 字符串解码
难度 : 中等
分类 : 栈
链接 : https://leetcode.cn/problems/decode-string/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
一行：字符串 s，形如 k[encoded_string]，支持嵌套。

【输出格式】
一行，解码后的字符串。

【样例输入】
2
3[a2[c]]
2[abc]3[cd]ef

【样例输出】
accaccacc
abcabccdcdcdef

"""

import sys


def solve(it):
    s = next(it)
    num_stack = []
    str_stack = []
    cur = []
    num = 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == "[":
            num_stack.append(num)
            str_stack.append(cur)
            cur = []
            num = 0
        elif c == "]":
            k = num_stack.pop()
            prev = str_stack.pop()
            prev.extend(cur * k)
            cur = prev
        else:
            cur.append(c)
    return "".join(cur)

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
