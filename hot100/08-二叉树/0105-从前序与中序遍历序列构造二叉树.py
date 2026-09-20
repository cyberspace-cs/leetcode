# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 041 / 100 题
================================================================
题号 : 105
标题 : 从前序与中序遍历序列构造二叉树
难度 : 中等
分类 : 二叉树
链接 : https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
================================================================

【题目描述】
根据前序遍历和中序遍历结果构造出原始二叉树（元素不重复）。

【示例】
preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]  →  [3,9,20,null,null,15,7]

【思路提示】
前序首元素为根，用哈希表定位它在中序中的下标以划分左右子树。

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
