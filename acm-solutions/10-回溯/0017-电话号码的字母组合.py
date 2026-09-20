# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 17
标题 : 电话号码的字母组合
难度 : 中等
分类 : 回溯
链接 : https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
一行：数字字符串 digits（仅含 2-9）。

【输出格式】
第一行：组合个数 g；随后 g 行，每行一个字母组合；digits 为空时仅输出 0。

【样例输入】
2
23
9

【样例输出】
9
ad
ae
af
bd
be
bf
cd
ce
cf
4
w
x
y
z

"""

import sys


def solve(it):
    digits = next(it)
    if not digits:
        return "0"
    table = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
    }
    res = []

    def bt(i, cur):
        if i == len(digits):
            res.append(cur)
            return
        for c in table[digits[i]]:
            bt(i + 1, cur + c)

    bt(0, "")
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
