# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 543    标题: 二叉树的直径    难度: 简单    分类: 二叉树
# 链接: https://leetcode.cn/problems/diameter-of-binary-tree/
# 运行: python3 "0543-二叉树的直径.py"   （按提示输入，或重定向样例输入）

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals):
    """按层序数组（LeetCode 形式，None 表示空）构造二叉树。"""
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


def tree_to_vals(root):
    """按层序输出为数组（去掉尾部 None），与 build_tree 互逆。"""
    if not root:
        return []
    out = []
    dq = deque([root])
    while dq:
        node = dq.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        dq.append(node.left)
        dq.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def right_chain_vals(root):
    """沿右指针读出节点值（用于「展开为链表」的输出）。"""
    vals = []
    cur = root
    while cur:
        vals.append(cur.val)
        cur = cur.right
    return vals


def diameter_of_binary_tree(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # 在这里写你的代码
    best = 0

    def depth(node):
        nonlocal best
        if not node:
            return 0
        l = depth(node.left)
        r = depth(node.right)
        best = max(best, l + r)
        return 1 + max(l, r)

    depth(root)
    return best


def main():
    nums = eval(input())
    print(diameter_of_binary_tree(build_tree(nums)))


if __name__ == "__main__":
    main()


# 543. 二叉树的直径  简单
#
# 【题目描述】
# 返回二叉树中任意两个节点之间最长路径的边数。
#
# 【示例】
# root = [1,2,3,4,5]  →  3
#
# 【思路提示】
# 后序递归求深度，同时用「左深度 + 右深度」更新全局答案。
#
# 【输入格式】
# 一行：层序数组（LeetCode 形式，空节点写 None），如 [3,9,20,None,None,15,7]。
#
# 【样例输入】
# [1,2,3,4,5]
# 【样例输出】
# 3
