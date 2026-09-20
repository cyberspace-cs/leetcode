# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 102    标题: 二叉树的层序遍历    难度: 中等    分类: 二叉树
# 链接: https://leetcode.cn/problems/binary-tree-level-order-traversal/
# 运行: python3 "0102-二叉树的层序遍历.py"   （按提示输入，或重定向样例输入）

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


def level_order(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    # 在这里写你的代码
    if not root:
        return []
    res = []
    dq = deque([root])
    while dq:
        level = []
        for _ in range(len(dq)):
            node = dq.popleft()
            level.append(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        res.append(level)
    return res


def main():
    nums = eval(input())
    print(level_order(build_tree(nums)))


if __name__ == "__main__":
    main()


# 102. 二叉树的层序遍历  中等
#
# 【题目描述】
# 按层返回二叉树节点的值（从上到下、每层从左到右）。
#
# 【示例】
# root = [3,9,20,null,null,15,7]  →  [[3],[9,20],[15,7]]
#
# 【思路提示】
# 队列 BFS，每轮先记录当前队列长度，即该层节点数。
#
# 【输入格式】
# 一行：层序数组（LeetCode 形式，空节点写 None），如 [3,9,20,None,None,15,7]。
#
# 【样例输入】
# [3,9,20,None,None,15,7]
# 【样例输出】
# [[3], [9, 20], [15, 7]]
