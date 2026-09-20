# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 104    标题: 二叉树的最大深度    难度: 简单    分类: 二叉树
# 链接: https://leetcode.cn/problems/maximum-depth-of-binary-tree/
# 运行: python3 "0104-二叉树的最大深度.py"   （按提示输入，或重定向样例输入）

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


def max_depth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # 在这里写你的代码
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def main():
    nums = eval(input())
    print(max_depth(build_tree(nums)))


if __name__ == "__main__":
    main()


# 104. 二叉树的最大深度  简单
#
# 【题目描述】
# 返回二叉树的最大深度（根到最远叶节点的节点数）。
#
# 【示例】
# root = [3,9,20,null,null,15,7]  →  3
#
# 【思路提示】
# 递归 max(左子树, 右子树) + 1；也可用层序遍历统计层数。
#
# 【输入格式】
# 一行：层序数组（LeetCode 形式，空节点写 None），如 [3,9,20,None,None,15,7]。
#
# 【样例输入】
# [3,9,20,None,None,15,7]
# 【样例输出】
# 3
