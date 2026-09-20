# -*- coding: utf-8 -*-
"""栈分类 · 个人模板风格（单组输入）。"""

PROBLEMS = [
    dict(
        num=20, func='is_valid', params=[('s', 'str')], ret='bool',
        body='''    # 在这里写你的代码
    pair = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack.pop() != pair[ch]:
                return False
    return not stack''',
        main='''    s = input()
    print(is_valid(s))''',
        inp='一行：括号字符串，如 ()[]{}。',
        sample_in='()[]{}\n',
        sample_out='True\n',
    ),
    dict(
        num=155, func=None, params=[], ret='None',
        code='''class MinStack:
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
        return self.mins[-1]''',
        main='''    ops = eval(input())
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
    print(out)''',
        inp='一行：操作列表，如 [["push",-2],["getMin"],["pop"],["top"]]。',
        sample_in='[["push",-2],["push",0],["push",-3],["getMin"],["pop"],["top"],["getMin"]]\n',
        sample_out='[-3, 0, -2]\n',
    ),
    dict(
        num=394, func='decode_string', params=[('s', 'str')], ret='str',
        body='''    # 在这里写你的代码（双栈）
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
    return "".join(cur)''',
        main='''    s = input()
    print(decode_string(s))''',
        inp='一行：编码字符串，如 3[a2[c]]。',
        sample_in='3[a2[c]]\n',
        sample_out='accaccacc\n',
    ),
    dict(
        num=739, func='daily_temperatures',
        params=[('temperatures', 'List[int]')], ret='List[int]',
        body='''    # 在这里写你的代码（单调递减栈）
    n = len(temperatures)
    res = [0] * n
    stack = []
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res''',
        main='''    temperatures = eval(input())
    print(daily_temperatures(temperatures))''',
        inp='一行：每日温度列表，如 [73,74,75,71,69,72,76,73]。',
        sample_in='[73,74,75,71,69,72,76,73]\n',
        sample_out='[1, 1, 4, 2, 1, 1, 0, 0]\n',
    ),
    dict(
        num=84, func='largest_rectangle_area', params=[('heights', 'List[int]')], ret='int',
        body='''    # 在这里写你的代码（单调递增栈，首尾补 0）
    hs = list(heights) + [0]
    stack = []
    best = 0
    for i, h in enumerate(hs):
        while stack and hs[stack[-1]] > h:
            j = stack.pop()
            left = stack[-1] if stack else -1
            best = max(best, hs[j] * (i - left - 1))
        stack.append(i)
    return best''',
        main='''    heights = eval(input())
    print(largest_rectangle_area(heights))''',
        inp='一行：柱高列表，如 [2,1,5,6,2,3]。',
        sample_in='[2,1,5,6,2,3]\n',
        sample_out='10\n',
    ),
]
