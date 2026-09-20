# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 039 / 100 题
================================================================
题号 : 102
标题 : 二叉树的层序遍历
难度 : 中等
分类 : 二叉树
链接 : https://leetcode.cn/problems/binary-tree-level-order-traversal/
================================================================

【题目描述】
按层返回二叉树节点的值（从上到下、每层从左到右）。

【示例】
root = [3,9,20,null,null,15,7]  →  [[3],[9,20],[15,7]]

【思路提示】
队列 BFS，每轮先记录当前队列长度，即该层节点数。

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
