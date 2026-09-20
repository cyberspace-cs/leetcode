# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 56    标题: 合并区间    难度: 中等    分类: 普通数组
# 链接: https://leetcode.cn/problems/merge-intervals/
# 运行: python3 "0056-合并区间.py"   （按提示输入，或重定向样例输入）

def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    # 在这里写你的代码
    intervals.sort(key=lambda x: x[0])
    res = []
    for l, r in intervals:
        if res and l <= res[-1][1]:
            res[-1][1] = max(res[-1][1], r)
        else:
            res.append([l, r])
    return res


def main():
    intervals = eval(input())
    print(merge(intervals))


if __name__ == "__main__":
    main()


# 56. 合并区间  中等
#
# 【题目描述】
# 合并所有重叠的区间，返回互不重叠的区间数组。
#
# 【示例】
# intervals = [[1,3],[2,6],[8,10],[15,18]]  →  [[1,6],[8,10],[15,18]]
#
# 【思路提示】
# 按左端点排序后一次遍历，判断当前区间是否与结果末尾重叠。
#
# 【输入格式】
# 一行：区间列表，如 [[1,3],[2,6],[8,10],[15,18]]。
#
# 【样例输入】
# [[1,3],[2,6],[8,10],[15,18]]
# 【样例输出】
# [[1, 6], [8, 10], [15, 18]]
