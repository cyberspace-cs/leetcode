# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 763    标题: 划分字母区间    难度: 中等    分类: 贪心算法
# 链接: https://leetcode.cn/problems/partition-labels/
# 运行: python3 "0763-划分字母区间.py"   （按提示输入，或重定向样例输入）

def partition_labels(s):
    """
    :type s: str
    :rtype: List[int]
    """
    # 在这里写你的代码
    last = {}
    for i, ch in enumerate(s):
        last[ch] = i
    res = []
    start = end = 0
    for i, ch in enumerate(s):
        end = max(end, last[ch])
        if i == end:
            res.append(end - start + 1)
            start = i + 1
    return res


def main():
    s = input()
    print(partition_labels(s))


if __name__ == "__main__":
    main()


# 763. 划分字母区间  中等
#
# 【题目描述】
# 把字符串划分为尽可能多的片段，使同一字母最多只出现在一个片段中，返回每个片段的长度。
#
# 【示例】
# s = "ababcbacadefegdehijhklij"  →  [9,7,8]
#
# 【思路提示】
# 先记录每个字符最后出现的位置，再遍历并不断扩张当前片段的右边界。
#
# 【输入格式】
# 一行：字符串（仅含小写字母），如 ababcbacadefegdehijhklij。
#
# 【样例输入】
# ababcbacadefegdehijhklij
# 【样例输出】
# [9, 7, 8]
