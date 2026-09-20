# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 199    标题: 二叉树的右视图    难度: 中等    分类: 二叉树
# 链接: https://leetcode.cn/problems/binary-tree-right-side-view/
# 运行: python3 "0199-二叉树的右视图.py"   （按提示输入，或重定向样例输入）

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


def right_side_view(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # 在这里写你的代码
    if not root:
        return []
    res = []
    dq = deque([root])
    while dq:
        size = len(dq)
        for i in range(size):
            node = dq.popleft()
            if i == size - 1:
                res.append(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
    return res


def main():
    nums = eval(input())
    print(right_side_view(build_tree(nums)))


if __name__ == "__main__":
    main()


# 199. 二叉树的右视图  中等
#
# 【题目描述】
# 按从上到下的顺序，返回从右侧能看到的节点值。
#
# 【示例】
# root = [1,2,3,null,5,null,4]  →  [1,3,4]
#
# 【思路提示】
# 层序遍历，取每层的最后一个节点；也可用 DFS 按「先右后左」首次到达。
#
# 【输入格式】
# 一行：层序数组（LeetCode 形式，空节点写 None），如 [3,9,20,None,None,15,7]。
#
# 【样例输入】
# [1,2,3,None,5,None,4]
# 【样例输出】
# [1, 3, 4]
