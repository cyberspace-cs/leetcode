# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 114    标题: 二叉树展开为链表    难度: 中等    分类: 二叉树
# 链接: https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
# 运行: python3 "0114-二叉树展开为链表.py"   （按提示输入，或重定向样例输入）

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


def flatten(root):
    """
    :type root: TreeNode
    :rtype: None
    """
    # 在这里写你的代码（原地展开为只有右子节点的单链表）
    cur = root
    while cur:
        if cur.left:
            rightmost = cur.left
            while rightmost.right:
                rightmost = rightmost.right
            rightmost.right = cur.right
            cur.right = cur.left
            cur.left = None
        cur = cur.right


def main():
    nums = eval(input())
    root = build_tree(nums)
    flatten(root)
    print(right_chain_vals(root))


if __name__ == "__main__":
    main()


# 114. 二叉树展开为链表  中等
#
# 【题目描述】
# 把二叉树原地展开为只有右子节点的单链表，顺序与前序遍历一致。
#
# 【示例】
# root = [1,2,5,3,4,null,6]  →  [1,null,2,null,3,null,4,null,5,null,6]
#
# 【思路提示】
# 前序收集节点后重新连接；或用「寻找左子树最右节点」的原地拼接法。
#
# 【输入格式】
# 一行：层序数组（LeetCode 形式，空节点写 None），如 [3,9,20,None,None,15,7]。
#
# 【样例输入】
# [1,2,5,3,4,None,6]
# 【样例输出】
# [1, 2, 3, 4, 5, 6]
