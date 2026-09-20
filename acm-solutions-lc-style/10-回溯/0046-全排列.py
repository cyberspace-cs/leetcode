# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 46    标题: 全排列    难度: 中等    分类: 回溯
# 链接: https://leetcode.cn/problems/permutations/
# 运行: python3 "0046-全排列.py"   （按提示输入，或重定向样例输入）

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # 在这里写你的代码
    res = []
    used = [False] * len(nums)
    path = []

    def backtrack():
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return res


def main():
    nums = eval(input())
    print(permute(nums))


if __name__ == "__main__":
    main()


# 46. 全排列  中等
#
# 【题目描述】
# 给定不含重复数字的数组，返回其所有可能的全排列。
#
# 【示例】
# nums = [1,2,3]  →  [[1,2,3],[1,3,2],[2,1,3],...]
#
# 【思路提示】
# 回溯 + used 标记已选元素；也可用「依次交换」的写法。
#
# 【输入格式】
# 一行：互不相同的整数列表，如 [1,2,3]。
#
# 【样例输入】
# [1,2,3]
# 【样例输出】
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
