# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 124
标题 : 二叉树中的最大路径和
难度 : 困难
分类 : 二叉树
链接 : https://leetcode.cn/problems/binary-tree-maximum-path-sum/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：n；第二行：n 个 token，每个为整数或 null，按层序（LeetCode 数组形式）描述二叉树。

【输出格式】
一行，最大路径和。

【样例输入】
2
7
-10 9 20 null null 15 7
1
-3

【样例输出】
42
-3

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
    root = build_tree(read_vals(it, n))
    best = [None]

    def gain(node):
        if not node:
            return 0
        l = max(gain(node.left), 0)
        r = max(gain(node.right), 0)
        total = node.val + l + r
        if best[0] is None or total > best[0]:
            best[0] = total
        return node.val + max(l, r)

    gain(root)
    return best[0]

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
