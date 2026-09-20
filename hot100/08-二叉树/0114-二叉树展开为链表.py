# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 043 / 100 题
================================================================
题号 : 114
标题 : 二叉树展开为链表
难度 : 中等
分类 : 二叉树
链接 : https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
================================================================

【题目描述】
把二叉树原地展开为只有右子节点的单链表，顺序与前序遍历一致。

【示例】
root = [1,2,5,3,4,null,6]  →  [1,null,2,null,3,null,4,null,5,null,6]

【思路提示】
前序收集节点后重新连接；或用「寻找左子树最右节点」的原地拼接法。

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
    def flatten(self, root: Optional[TreeNode]) -> None:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")


if __name__ == "__main__":
    # TODO: 在这里补充自测用例
    # s = Solution()
    # print(s.<方法名>(...))

    pass
