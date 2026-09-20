# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 78    标题: 子集    难度: 中等    分类: 回溯
# 链接: https://leetcode.cn/problems/subsets/
# 运行: python3 "0078-子集.py"   （按提示输入，或重定向样例输入）

def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # 在这里写你的代码
    res = []
    path = []

    def backtrack(start):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return res


def main():
    nums = eval(input())
    print(subsets(nums))


if __name__ == "__main__":
    main()


# 78. 子集  中等
#
# 【题目描述】
# 给定不含重复元素的数组，返回其所有可能的子集（幂集）。
#
# 【示例】
# nums = [1,2,3]  →  [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
#
# 【思路提示】
# 回溯：对每个位置做「选 / 不选」两个分支。
#
# 【输入格式】
# 一行：互不相同的整数列表，如 [1,2,3]。
#
# 【样例输入】
# [1,2,3]
# 【样例输出】
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
