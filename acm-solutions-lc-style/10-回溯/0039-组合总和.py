# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 39    标题: 组合总和    难度: 中等    分类: 回溯
# 链接: https://leetcode.cn/problems/combination-sum/
# 运行: python3 "0039-组合总和.py"   （按提示输入，或重定向样例输入）

def combination_sum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    # 在这里写你的代码
    candidates.sort()
    res = []
    path = []

    def backtrack(start, remain):
        if remain == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                break
            path.append(candidates[i])
            backtrack(i, remain - candidates[i])
            path.pop()

    backtrack(0, target)
    return res


def main():
    candidates = eval(input())
    target = int(input())
    print(combination_sum(candidates, target))


if __name__ == "__main__":
    main()


# 39. 组合总和  中等
#
# 【题目描述】
# 给定无重复元素的候选数组和目标值，找出所有和为目标的组合，每个数字可被重复选取。
#
# 【示例】
# candidates = [2,3,6,7], target = 7  →  [[2,2,3],[7]]
#
# 【思路提示】
# 排序 + 回溯，用 start 下标保证组合不重复，剩余值小于当前数时剪枝。
#
# 【输入格式】
# 第一行：候选数字列表；第二行：target。数字可重复选取。
#
# 【样例输入】
# [2,3,6,7]
# 7
# 【样例输出】
# [[2, 2, 3], [7]]
