# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 139    标题: 单词拆分    难度: 中等    分类: 动态规划
# 链接: https://leetcode.cn/problems/word-break/
# 运行: python3 "0139-单词拆分.py"   （按提示输入，或重定向样例输入）

def word_break(s, word_dict):
    """
    :type s: str
    :type word_dict: List[str]
    :rtype: bool
    """
    # 在这里写你的代码
    words = set(word_dict)
    max_len = max((len(w) for w in words), default=0)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(max(0, i - max_len), i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]


def main():
    s = input()
    word_dict = eval(input())
    print(word_break(s, word_dict))


if __name__ == "__main__":
    main()


# 139. 单词拆分  中等
#
# 【题目描述】
# 判断字符串能否被拆分成字典中出现的一个或多个单词。
#
# 【示例】
# s = "leetcode", wordDict = ["leet","code"]  →  true
#
# 【思路提示】
# dp[i] 表示前 i 个字符可被拆分，枚举末尾单词并查表转移。
#
# 【输入格式】
# 第一行：字符串 s；第二行：单词列表，如 ["leet","code"]。
#
# 【样例输入】
# leetcode
# ["leet","code"]
# 【样例输出】
# True
