# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 105    标题: 从前序与中序遍历序列构造二叉树    难度: 中等    分类: 二叉树
# 链接: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 运行: python3 "0105-从前序与中序遍历序列构造二叉树.py"   （按提示输入，或重定向样例输入）

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


def build_tree_from_pre_in(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    # 在这里写你的代码
    pos = {v: i for i, v in enumerate(inorder)}
    idx = 0

    def build(lo, hi):
        nonlocal idx
        if lo > hi:
            return None
        val = preorder[idx]
        idx += 1
        node = TreeNode(val)
        mid = pos[val]
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return build(0, len(preorder) - 1)


def main():
    preorder = eval(input())
    inorder = eval(input())
    print(tree_to_vals(build_tree_from_pre_in(preorder, inorder)))


if __name__ == "__main__":
    main()


# 105. 从前序与中序遍历序列构造二叉树  中等
#
# 【题目描述】
# 根据前序遍历和中序遍历结果构造出原始二叉树（元素不重复）。
#
# 【示例】
# preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]  →  [3,9,20,null,null,15,7]
#
# 【思路提示】
# 前序首元素为根，用哈希表定位它在中序中的下标以划分左右子树。
#
# 【输入格式】
# 第一行：前序遍历列表；第二行：中序遍历列表（元素互不相同）。
#
# 【样例输入】
# [3,9,20,15,7]
# [9,3,15,20,7]
# 【样例输出】
# [3, 9, 20, None, None, 15, 7]
