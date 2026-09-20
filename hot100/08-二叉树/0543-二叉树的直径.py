# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 050 / 100 题
================================================================
题号 : 543
标题 : 二叉树的直径
难度 : 简单
分类 : 二叉树
链接 : https://leetcode.cn/problems/diameter-of-binary-tree/
================================================================

【题目描述】
返回二叉树中任意两个节点之间最长路径的边数。

【示例】
root = [1,2,3,4,5]  →  3

【思路提示】
后序递归求深度，同时用「左深度 + 右深度」更新全局答案。

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
