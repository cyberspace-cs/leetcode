# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 49    标题: 字母异位词分组    难度: 中等    分类: 哈希
# 链接: https://leetcode.cn/problems/group-anagrams/
# 运行: python3 "0049-字母异位词分组.py"   （按提示输入，或重定向样例输入）

def group_anagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # 在这里写你的代码
    from collections import defaultdict
    groups = defaultdict(list)
    for s in strs:
        groups[''.join(sorted(s))].append(s)
    return list(groups.values())


def main():
    strs = eval(input())
    print(group_anagrams(strs))


if __name__ == "__main__":
    main()


# 49. 字母异位词分组  中等
#
# 【题目描述】
# 给定字符串数组，把字母异位词（字符组成相同、顺序不同）归到同一组，组内与组间顺序不限。
#
# 【示例】
# strs = ["eat","tea","tan","ate","nat","bat"]  →  [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# 【思路提示】
# 以「排序后的字符串」或「26 位字符计数元组」作为哈希键分组。
#
# 【输入格式】
# 一行：字符串列表，如 ["eat","tea","tan","ate","nat","bat"]。
#
# 【样例输入】
# ["eat","tea","tan","ate","nat","bat"]
# 【样例输出】
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
