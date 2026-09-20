# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 108    标题: 将有序数组转换为二叉搜索树    难度: 简单    分类: 二叉树
# 链接: https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
# 运行: python3 "0108-将有序数组转换为二叉搜索树.py"   （按提示输入，或重定向样例输入）

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


def sorted_array_to_bst(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    # 在这里写你的代码（每次取区间中点为根）
    def build(lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        node = TreeNode(nums[mid])
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return build(0, len(nums) - 1)


def main():
    nums = eval(input())
    print(tree_to_vals(sorted_array_to_bst(nums)))


if __name__ == "__main__":
    main()


# 108. 将有序数组转换为二叉搜索树  简单
#
# 【题目描述】
# 把升序数组转换为高度平衡的二叉搜索树。
#
# 【示例】
# nums = [-10,-3,0,5,9]  →  [0,-3,9,-10,null,5]
#
# 【思路提示】
# 每次取区间中点作为根，再递归构造左右子树。
#
# 【输入格式】
# 一行：升序整数列表，如 [-10,-3,0,5,9]。
#
# 【样例输入】
# [-10,-3,0,5,9]
# 【样例输出】
# [0, -10, 5, None, -3, None, 9]
