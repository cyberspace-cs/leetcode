# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 236
标题 : 二叉树的最近公共祖先
难度 : 中等
分类 : 二叉树
链接 : https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n p q；第二行：n 个 token（层序数组，含 null）。p、q 为节点值，保证存在。

【输出格式】
一行，最近公共祖先的节点值。

【样例输入】
2
11 5 1
3 5 1 6 2 0 8 null null 7 4
3 1 2
1 2 3

【样例输出】
3
1

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
    p = int(next(it))
    q = int(next(it))
    root = build_tree(read_vals(it, n))

    def lca(node):
        if not node:
            return None
        if node.val == p or node.val == q:
            return node
        l = lca(node.left)
        r = lca(node.right)
        if l and r:
            return node
        return l or r

    res = lca(root)
    return res.val if res else -1

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
