# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 17    标题: 电话号码的字母组合    难度: 中等    分类: 回溯
# 链接: https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
# 运行: python3 "0017-电话号码的字母组合.py"   （按提示输入，或重定向样例输入）

def letter_combinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    # 在这里写你的代码
    if not digits:
        return []
    table = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
    }
    res = []

    def backtrack(i, cur):
        if i == len(digits):
            res.append(cur)
            return
        for ch in table[digits[i]]:
            backtrack(i + 1, cur + ch)

    backtrack(0, "")
    return res


def main():
    digits = input()
    print(letter_combinations(digits))


if __name__ == "__main__":
    main()


# 17. 电话号码的字母组合  中等
#
# 【题目描述】
# 给定仅含数字 2-9 的字符串，返回它所有可能代表的字母组合。
#
# 【示例】
# digits = "23"  →  ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# 【思路提示】
# 回溯 + 电话键盘映射表，逐位枚举可选字母。
#
# 【输入格式】
# 一行：数字字符串（仅含 2-9），如 23。
#
# 【样例输入】
# 23
# 【样例输出】
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
