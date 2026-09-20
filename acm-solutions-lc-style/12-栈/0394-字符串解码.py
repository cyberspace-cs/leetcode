# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 394    标题: 字符串解码    难度: 中等    分类: 栈
# 链接: https://leetcode.cn/problems/decode-string/
# 运行: python3 "0394-字符串解码.py"   （按提示输入，或重定向样例输入）

def decode_string(s):
    """
    :type s: str
    :rtype: str
    """
    # 在这里写你的代码（双栈）
    num_stack = []
    str_stack = []
    cur = []
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            num_stack.append(num)
            str_stack.append(cur)
            cur = []
            num = 0
        elif ch == "]":
            k = num_stack.pop()
            prev = str_stack.pop()
            prev.extend(cur * k)
            cur = prev
        else:
            cur.append(ch)
    return "".join(cur)


def main():
    s = input()
    print(decode_string(s))


if __name__ == "__main__":
    main()


# 394. 字符串解码  中等
#
# 【题目描述】
# 解码形如 k[encoded_string] 的字符串，k 表示其后方括号内内容重复的次数，支持嵌套。
#
# 【示例】
# s = "3[a2[c]]"  →  "accaccacc"
#
# 【思路提示】
# 用数字栈与字符串栈模拟解析；也可写递归下降解析器。
#
# 【输入格式】
# 一行：编码字符串，如 3[a2[c]]。
#
# 【样例输入】
# 3[a2[c]]
# 【样例输出】
# accaccacc
