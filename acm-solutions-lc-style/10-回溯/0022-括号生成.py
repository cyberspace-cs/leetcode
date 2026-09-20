# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 22    标题: 括号生成    难度: 中等    分类: 回溯
# 链接: https://leetcode.cn/problems/generate-parentheses/
# 运行: python3 "0022-括号生成.py"   （按提示输入，或重定向样例输入）

def generate_parenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    # 在这里写你的代码
    res = []

    def backtrack(cur, left, right):
        if len(cur) == 2 * n:
            res.append(cur)
            return
        if left < n:
            backtrack(cur + "(", left + 1, right)
        if right < left:
            backtrack(cur + ")", left, right + 1)

    backtrack("", 0, 0)
    return res


def main():
    n = int(input())
    print(generate_parenthesis(n))


if __name__ == "__main__":
    main()


# 22. 括号生成  中等
#
# 【题目描述】
# 生成所有由 n 对括号组成的有效（正确闭合）组合。
#
# 【示例】
# n = 3  →  ["((()))","(()())","(())()","()(())","()()()"]
#
# 【思路提示】
# 回溯：左括号数 < n 时可加左括号；右括号数 < 左括号数时可加右括号。
#
# 【输入格式】
# 一行：n（括号对数）。
#
# 【样例输入】
# 3
# 【样例输出】
# ['((()))', '(()())', '(())()', '()(())', '()()()']
