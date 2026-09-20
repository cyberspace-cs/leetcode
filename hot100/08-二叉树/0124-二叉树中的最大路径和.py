# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 044 / 100 题
================================================================
题号 : 124
标题 : 二叉树中的最大路径和
难度 : 困难
分类 : 二叉树
链接 : https://leetcode.cn/problems/binary-tree-maximum-path-sum/
================================================================

【题目描述】
返回二叉树中任意一条路径的最大路径和（路径可不经过根，但同一节点最多出现一次）。

【示例】
root = [-10,9,20,null,null,15,7]  →  42

【思路提示】
后序递归返回「单边最大贡献」，同时用「左贡献 + 右贡献 + 根值」更新全局答案。

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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
