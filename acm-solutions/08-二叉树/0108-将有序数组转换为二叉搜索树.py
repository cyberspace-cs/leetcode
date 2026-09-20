# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 108
标题 : 将有序数组转换为二叉搜索树
难度 : 简单
分类 : 二叉树
链接 : https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个升序整数。

【输出格式】
一行，构造出的高度平衡 BST（层序数组形式）。每次取区间中点为根，答案可能不唯一。

【样例输入】
1
5
-10 -3 0 5 9

【样例输出】
0 -10 5 null -3 null 9

"""

import sys


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def read_vals(it, n):
    vals = []
    for _ in range(n):
        tok = next(it)
        vals.append(None if tok == "null" else int(tok))
    return vals


def build_tree(vals):
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    dq = deque([root])
    i = 1
    while dq and i < len(vals):
        node = dq.popleft()
        if i < len(vals):
            v = vals[i]
            if v is not None:
                node.left = TreeNode(v)
                dq.append(node.left)
            i += 1
        if i < len(vals):
            v = vals[i]
            if v is not None:
                node.right = TreeNode(v)
                dq.append(node.right)
            i += 1
    return root


def tree_to_str(root):
    if not root:
        return "EMPTY"
    out = []
    dq = deque([root])
    while dq:
        node = dq.popleft()
        if node is None:
            out.append("null")
            continue
        out.append(str(node.val))
        dq.append(node.left)
        dq.append(node.right)
    while out and out[-1] == "null":
        out.pop()
    return " ".join(out)


def dump_list(vals):
    return " ".join(map(str, vals)) if vals else "EMPTY"


def solve(it):
    n = int(next(it))
    nums = [int(next(it)) for _ in range(n)]

    def build(lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        node = TreeNode(nums[mid])
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return tree_to_str(build(0, n - 1))

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
