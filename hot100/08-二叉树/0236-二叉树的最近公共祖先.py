# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 048 / 100 题
================================================================
题号 : 236
标题 : 二叉树的最近公共祖先
难度 : 中等
分类 : 二叉树
链接 : https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
================================================================

【题目描述】
返回二叉树中两个指定节点的最近公共祖先。

【示例】
root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1  →  3

【思路提示】
后序递归：左右子树各找到一个目标则当前节点即为答案，否则返回非空的一侧。

【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
