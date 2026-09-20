# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 20    标题: 有效的括号    难度: 简单    分类: 栈
# 链接: https://leetcode.cn/problems/valid-parentheses/
# 运行: python3 "0020-有效的括号.py"   （按提示输入，或重定向样例输入）

def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    # 在这里写你的代码
    pair = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack.pop() != pair[ch]:
                return False
    return not stack


def main():
    s = input()
    print(is_valid(s))


if __name__ == "__main__":
    main()


# 20. 有效的括号  简单
#
# 【题目描述】
# 判断只含 ()[]{} 的字符串中的括号是否有效闭合。
#
# 【示例】
# s = "()[]{}"  →  true
#
# 【思路提示】
# 左括号入栈，遇到右括号时与栈顶匹配，最终栈必须为空。
#
# 【输入格式】
# 一行：括号字符串，如 ()[]{}。
#
# 【样例输入】
# ()[]{}
# 【样例输出】
# True
