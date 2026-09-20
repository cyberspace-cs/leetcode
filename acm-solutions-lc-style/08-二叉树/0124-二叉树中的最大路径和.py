# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 124    标题: 二叉树中的最大路径和    难度: 困难    分类: 二叉树
# 链接: https://leetcode.cn/problems/binary-tree-maximum-path-sum/
# 运行: python3 "0124-二叉树中的最大路径和.py"   （按提示输入，或重定向样例输入）

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


def max_path_sum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # 在这里写你的代码
    best = [None]

    def gain(node):
        if not node:
            return 0
        left = max(gain(node.left), 0)
        right = max(gain(node.right), 0)
        total = node.val + left + right
        if best[0] is None or total > best[0]:
            best[0] = total
        return node.val + max(left, right)

    gain(root)
    return best[0]


def main():
    nums = eval(input())
    print(max_path_sum(build_tree(nums)))


if __name__ == "__main__":
    main()


# 124. 二叉树中的最大路径和  困难
#
# 【题目描述】
# 返回二叉树中任意一条路径的最大路径和（路径可不经过根，但同一节点最多出现一次）。
#
# 【示例】
# root = [-10,9,20,null,null,15,7]  →  42
#
# 【思路提示】
# 后序递归返回「单边最大贡献」，同时用「左贡献 + 右贡献 + 根值」更新全局答案。
#
# 【输入格式】
# 一行：层序数组（LeetCode 形式，空节点写 None），如 [3,9,20,None,None,15,7]。
#
# 【样例输入】
# [-10,9,20,None,None,15,7]
# 【样例输出】
# 42
