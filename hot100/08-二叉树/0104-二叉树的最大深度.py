# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 040 / 100 题
================================================================
题号 : 104
标题 : 二叉树的最大深度
难度 : 简单
分类 : 二叉树
链接 : https://leetcode.cn/problems/maximum-depth-of-binary-tree/
================================================================

【题目描述】
返回二叉树的最大深度（根到最远叶节点的节点数）。

【示例】
root = [3,9,20,null,null,15,7]  →  3

【思路提示】
递归 max(左子树, 右子树) + 1；也可用层序遍历统计层数。

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
