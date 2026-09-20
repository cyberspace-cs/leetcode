# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 101    标题: 对称二叉树    难度: 简单    分类: 二叉树
# 链接: https://leetcode.cn/problems/symmetric-tree/
# 运行: python3 "0101-对称二叉树.py"   （按提示输入，或重定向样例输入）

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


def is_symmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    # 在这里写你的代码
    def mirror(a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return mirror(a.left, b.right) and mirror(a.right, b.left)

    return not root or mirror(root.left, root.right)


def main():
    nums = eval(input())
    print(is_symmetric(build_tree(nums)))


if __name__ == "__main__":
    main()


# 101. 对称二叉树  简单
#
# 【题目描述】
# 判断二叉树是否轴对称。
#
# 【示例】
# root = [1,2,2,3,4,4,3]  →  true
#
# 【思路提示】
# 递归比较 (左.left, 右.right) 与 (左.right, 右.left)；也可用队列迭代。
#
# 【输入格式】
# 一行：层序数组（LeetCode 形式，空节点写 None），如 [3,9,20,None,None,15,7]。
#
# 【样例输入】
# [1,2,2,3,4,4,3]
# 【样例输出】
# True
