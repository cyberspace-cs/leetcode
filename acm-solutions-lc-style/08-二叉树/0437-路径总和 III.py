# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 437    标题: 路径总和 III    难度: 中等    分类: 二叉树
# 链接: https://leetcode.cn/problems/path-sum-iii/
# 运行: python3 "0437-路径总和 III.py"   （按提示输入，或重定向样例输入）

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


def path_sum(root, target_sum):
    """
    :type root: TreeNode
    :type target_sum: int
    :rtype: int
    """
    # 在这里写你的代码（前缀和 + 回溯）
    count = {0: 1}
    res = 0

    def dfs(node, prefix):
        nonlocal res
        if not node:
            return
        prefix += node.val
        res += count.get(prefix - target_sum, 0)
        count[prefix] = count.get(prefix, 0) + 1
        dfs(node.left, prefix)
        dfs(node.right, prefix)
        count[prefix] -= 1

    dfs(root, 0)
    return res


def main():
    nums = eval(input())
    target_sum = int(input())
    print(path_sum(build_tree(nums), target_sum))


if __name__ == "__main__":
    main()


# 437. 路径总和 III  中等
#
# 【题目描述】
# 统计二叉树中节点值之和等于 targetSum 的路径条数（路径方向只能向下，不必从根开始）。
#
# 【示例】
# root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8  →  3
#
# 【思路提示】
# 前缀和 + 回溯：遍历时统计 (当前前缀和 - targetSum) 在哈希表中的出现次数。
#
# 【输入格式】
# 第一行：层序数组；第二行：targetSum。
#
# 【样例输入】
# [10,5,-3,3,2,None,11,3,-2,None,1]
# 8
# 【样例输出】
# 3
