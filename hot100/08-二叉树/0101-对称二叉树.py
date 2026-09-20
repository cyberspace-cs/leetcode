# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 038 / 100 题
================================================================
题号 : 101
标题 : 对称二叉树
难度 : 简单
分类 : 二叉树
链接 : https://leetcode.cn/problems/symmetric-tree/
================================================================

【题目描述】
判断二叉树是否轴对称。

【示例】
root = [1,2,2,3,4,4,3]  →  true

【思路提示】
递归比较 (左.left, 右.right) 与 (左.right, 右.left)；也可用队列迭代。

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
