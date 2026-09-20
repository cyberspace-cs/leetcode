# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 3    标题: 无重复字符的最长子串    难度: 中等    分类: 滑动窗口
# 链接: https://leetcode.cn/problems/longest-substring-without-repeating-characters/
# 运行: python3 "0003-无重复字符的最长子串.py"   （按提示输入，或重定向样例输入）

def length_of_longest_substring(s):
    """
    :type s: str
    :rtype: int
    """
    # 在这里写你的代码
    char_index = {}
    left = 0
    max_length = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            # 字符在当前窗口内重复，左指针跳到重复字符的下一位
            left = char_index[char] + 1
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length


def main():
    s = input()
    print(length_of_longest_substring(s))


if __name__ == "__main__":
    main()


# 3. 无重复字符的最长子串  中等
#
# 【题目描述】
# 给定字符串 s，找出其中不含重复字符的最长子串，返回其长度。
#
# 【示例】
# s = "abcabcbb"  →  3   # 最长子串为 "abc"
#
# 【思路提示】
# 滑动窗口 + 哈希记录字符最近出现下标，遇到重复字符则收缩左边界。
#
# 【输入格式】
# 一行：字符串 s，如 abcabcbb。
#
# 【样例输入】
# abcabcbb
# 【样例输出】
# 3
