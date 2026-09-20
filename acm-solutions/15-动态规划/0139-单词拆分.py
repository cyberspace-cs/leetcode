# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 139
标题 : 单词拆分
难度 : 中等
分类 : 动态规划
链接 : https://leetcode.cn/problems/word-break/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：字符串 s；第二行：k；第三行：k 个单词。

【输出格式】
一行，true 或 false。

【样例输入】
3
leetcode
2
leet code
applepenapple
2
apple pen
catsandog
5
cats dog sand and cat

【样例输出】
true
true
false

"""

import sys


def solve(it):
    s = next(it)
    k = int(next(it))
    words = set(next(it) for _ in range(k))
    n = len(s)
    maxlen = max((len(w) for w in words), default=0)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(max(0, i - maxlen), i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return "true" if dp[n] else "false"

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
