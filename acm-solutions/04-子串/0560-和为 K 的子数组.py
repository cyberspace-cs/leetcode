# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 560
标题 : 和为 K 的子数组
难度 : 中等
分类 : 子串
链接 : https://leetcode.cn/problems/subarray-sum-equals-k/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n k；第二行：n 个整数。

【输出格式】
一行，和为 k 的连续子数组个数。

【样例输入】
3
3 2
1 1 1
3 3
1 2 3
4 0
0 0 0 0

【样例输出】
2
2
10

"""

import sys


def solve(it):
    n = int(next(it))
    k = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    cnt = {0: 1}
    pre = 0
    ans = 0
    for x in a:
        pre += x
        ans += cnt.get(pre - k, 0)
        cnt[pre] = cnt.get(pre, 0) + 1
    return ans

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
