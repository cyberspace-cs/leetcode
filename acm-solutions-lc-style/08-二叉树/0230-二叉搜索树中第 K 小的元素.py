# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 230    标题: 二叉搜索树中第 K 小的元素    难度: 中等    分类: 二叉树
# 链接: https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
# 运行: python3 "0230-二叉搜索树中第 K 小的元素.py"   （按提示输入，或重定向样例输入）

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


def kth_smallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    # 在这里写你的代码（中序遍历计数）
    stack, cur = [], root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val
        cur = cur.right
    return -1


def main():
    nums = eval(input())
    k = int(input())
    print(kth_smallest(build_tree(nums), k))


if __name__ == "__main__":
    main()


# 230. 二叉搜索树中第 K 小的元素  中等
#
# 【题目描述】
# 返回二叉搜索树中第 k 小的元素值。
#
# 【示例】
# root = [3,1,4,null,2], k = 1  →  1
#
# 【思路提示】
# 中序遍历，计数到第 k 个即返回（可提前剪枝）。
#
# 【输入格式】
# 第一行：层序数组；第二行：k。
#
# 【样例输入】
# [3,1,4,None,2]
# 1
# 【样例输出】
# 1
