# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 226    标题: 翻转二叉树    难度: 简单    分类: 二叉树
# 链接: https://leetcode.cn/problems/invert-binary-tree/
# 运行: python3 "0226-翻转二叉树.py"   （按提示输入，或重定向样例输入）

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


def invert_tree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    # 在这里写你的代码
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def main():
    nums = eval(input())
    print(tree_to_vals(invert_tree(build_tree(nums))))


if __name__ == "__main__":
    main()


# 226. 翻转二叉树  简单
#
# 【题目描述】
# 翻转二叉树，使每个节点的左右子树互换，返回根节点。
#
# 【示例】
# root = [4,2,7,1,3,6,9]  →  [4,7,2,9,6,3,1]
#
# 【思路提示】
# 递归交换每个节点的左右子树。
#
# 【输入格式】
# 一行：层序数组（LeetCode 形式，空节点写 None），如 [3,9,20,None,None,15,7]。
#
# 【样例输入】
# [4,2,7,1,3,6,9]
# 【样例输出】
# [4, 7, 2, 9, 6, 3, 1]
