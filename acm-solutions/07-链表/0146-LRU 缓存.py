# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 146
标题 : LRU 缓存
难度 : 中等
分类 : 链表
链接 : https://leetcode.cn/problems/lru-cache/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：capacity q；随后 q 行，每行为 "get key" 或 "put key value"。

【输出格式】
一行，按顺序输出所有 get 的结果（空格分隔）；若没有 get 操作输出 EMPTY。
为便于按行对齐，本题固定在每组输出恰好一行。

【样例输入】
2
2 5
get 1
put 1 1
put 2 2
get 1
put 3 3
1 3
put 1 1
get 1
get 2

【样例输出】
-1 1
1 -1

"""

import sys


def solve(it):
    cap = int(next(it))
    q = int(next(it))
    od = {}
    out = []
    for _ in range(q):
        op = next(it)
        if op == "get":
            k = int(next(it))
            if k in od:
                v = od.pop(k)
                od[k] = v
                out.append(str(v))
            else:
                out.append("-1")
        else:
            k = int(next(it))
            v = int(next(it))
            if k in od:
                od.pop(k)
            od[k] = v
            if len(od) > cap:
                od.pop(next(iter(od)))
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
