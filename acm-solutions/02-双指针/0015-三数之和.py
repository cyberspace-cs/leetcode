# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 15
标题 : 三数之和
难度 : 中等
分类 : 双指针
链接 : https://leetcode.cn/problems/3sum/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个整数。

【输出格式】
第一行：方案数 g；随后 g 行，每行三个升序整数（空格分隔），整体按字典序升序；无解时仅输出 0。

【样例输入】
2
6
-1 0 1 2 -1 -4
3
0 1 1

【样例输出】
2
-1 -1 2
-1 0 1
0

"""

import sys


def solve(it):
    n = int(next(it))
    nums = sorted(int(next(it)) for _ in range(n))
    res = []
    for i in range(n - 2):
        if i and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
    rows = ["%d %d %d" % t for t in res]
    return "\n".join([str(len(rows))] + rows)

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
