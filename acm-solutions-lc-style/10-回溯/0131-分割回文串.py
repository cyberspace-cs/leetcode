# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 131    标题: 分割回文串    难度: 中等    分类: 回溯
# 链接: https://leetcode.cn/problems/palindrome-partitioning/
# 运行: python3 "0131-分割回文串.py"   （按提示输入，或重定向样例输入）

def partition(s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    # 在这里写你的代码
    res = []
    path = []
    n = len(s)

    def is_palindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def backtrack(start):
        if start == n:
            res.append(path[:])
            return
        for end in range(start, n):
            if is_palindrome(start, end):
                path.append(s[start:end + 1])
                backtrack(end + 1)
                path.pop()

    backtrack(0)
    return res


def main():
    s = input()
    print(partition(s))


if __name__ == "__main__":
    main()


# 131. 分割回文串  中等
#
# 【题目描述】
# 把字符串分割成若干子串，使每个子串都是回文串，返回所有可能的分割方案。
#
# 【示例】
# s = "aab"  →  [["a","a","b"],["aa","b"]]
#
# 【思路提示】
# 回溯 + 剪枝：只有当当前子串是回文时才继续向下递归。
#
# 【输入格式】
# 一行：字符串 s（仅含小写字母），如 aab。
#
# 【样例输入】
# aab
# 【样例输出】
# [['a', 'a', 'b'], ['aa', 'b']]
