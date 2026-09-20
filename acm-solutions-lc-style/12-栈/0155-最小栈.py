# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 155    标题: 最小栈    难度: 中等    分类: 栈
# 链接: https://leetcode.cn/problems/min-stack/
# 运行: python3 "0155-最小栈.py"   （按提示输入，或重定向样例输入）

class MinStack:
    """
    :rtype: None
    """

    def __init__(self):
        # 在这里写你的代码
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        # 在这里写你的代码
        self.stack.append(val)
        self.mins.append(val if not self.mins else min(val, self.mins[-1]))

    def pop(self) -> None:
        # 在这里写你的代码
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        # 在这里写你的代码
        return self.stack[-1]

    def get_min(self) -> int:
        # 在这里写你的代码
        return self.mins[-1]


def main():
    ops = eval(input())
    st = MinStack()
    out = []
    for op in ops:
        if op[0] == "push":
            st.push(op[1])
        elif op[0] == "pop":
            st.pop()
        elif op[0] == "top":
            out.append(st.top())
        else:
            out.append(st.get_min())
    print(out)


if __name__ == "__main__":
    main()


# 155. 最小栈  中等
#
# 【题目描述】
# 设计一个支持 push、pop、top 操作，并能在常数时间内检索到最小元素的栈。
#
# 【示例】
# push(-2), push(0), push(-3), getMin() → -3, pop(), getMin() → -2
#
# 【思路提示】
# 使用辅助栈与主栈同步记录「当前最小值」。
#
# 【输入格式】
# 一行：操作列表，如 [["push",-2],["getMin"],["pop"],["top"]]。
#
# 【样例输入】
# [["push",-2],["push",0],["push",-3],["getMin"],["pop"],["top"],["getMin"]]
# 【样例输出】
# [-3, 0, -2]
