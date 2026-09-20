# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 236    标题: 二叉树的最近公共祖先    难度: 中等    分类: 二叉树
# 链接: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
# 运行: python3 "0236-二叉树的最近公共祖先.py"   （按提示输入，或重定向样例输入）

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


def lowest_common_ancestor(root, p, q):
    """
    :type root: TreeNode
    :type p: int
    :type q: int
    :rtype: TreeNode
    """
    # 在这里写你的代码（p、q 用节点值表示，保证存在且互不相同）
    def lca(node):
        if not node:
            return None
        if node.val == p or node.val == q:
            return node
        left = lca(node.left)
        right = lca(node.right)
        if left and right:
            return node
        return left or right

    return lca(root)


def main():
    nums = eval(input())
    p = int(input())
    q = int(input())
    node = lowest_common_ancestor(build_tree(nums), p, q)
    print(node.val if node else -1)


if __name__ == "__main__":
    main()


# 236. 二叉树的最近公共祖先  中等
#
# 【题目描述】
# 返回二叉树中两个指定节点的最近公共祖先。
#
# 【示例】
# root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1  →  3
#
# 【思路提示】
# 后序递归：左右子树各找到一个目标则当前节点即为答案，否则返回非空的一侧。
#
# 【输入格式】
# 第一行：层序数组；第二行：p（节点值）；第三行：q（节点值）。
#
# 【样例输入】
# [3,5,1,6,2,0,8,None,None,7,4]
# 5
# 1
# 【样例输出】
# 3
