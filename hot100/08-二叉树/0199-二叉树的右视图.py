# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 045 / 100 题
================================================================
题号 : 199
标题 : 二叉树的右视图
难度 : 中等
分类 : 二叉树
链接 : https://leetcode.cn/problems/binary-tree-right-side-view/
================================================================

【题目描述】
按从上到下的顺序，返回从右侧能看到的节点值。

【示例】
root = [1,2,3,null,5,null,4]  →  [1,3,4]

【思路提示】
层序遍历，取每层的最后一个节点；也可用 DFS 按「先右后左」首次到达。

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
