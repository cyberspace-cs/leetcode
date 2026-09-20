# -*- coding: utf-8 -*-
"""栈分类的 ACM 模式完整解题。"""

PROBLEMS = [
    dict(
        num=20, title='有效的括号', difficulty='简单', category='栈', slug='valid-parentheses',
        inp='一行：字符串 s（仅含 ()[]{} ）。',
        outp='一行，true 或 false。',
        sample_in='3\n()[]{}\n(]\n([)]\n',
        sample_out='true\nfalse\nfalse\n',
        code=r'''
def solve(it):
    s = next(it)
    pair = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if not stack or stack.pop() != pair[c]:
                return "false"
    return "true" if not stack else "false"
''',
    ),
    dict(
        num=155, title='最小栈', difficulty='中等', category='栈', slug='min-stack',
        inp='第一行：q；随后 q 行，每行为 push x / pop / top / getMin。',
        outp='一行，按顺序输出所有 top 与 getMin 的结果（空格分隔）；若无输出则输出 EMPTY。',
        sample_in='1\n7\npush -2\npush 0\npush -3\ngetMin\npop\ntop\ngetMin\n',
        sample_out='-3 0 -2\n',
        code=r'''
def solve(it):
    q = int(next(it))
    stack = []
    mins = []
    out = []
    for _ in range(q):
        op = next(it)
        if op == "push":
            x = int(next(it))
            stack.append(x)
            mins.append(x if not mins else min(x, mins[-1]))
        elif op == "pop":
            stack.pop()
            mins.pop()
        elif op == "top":
            out.append(str(stack[-1]))
        else:
            out.append(str(mins[-1]))
    return " ".join(out) if out else "EMPTY"
''',
    ),
    dict(
        num=394, title='字符串解码', difficulty='中等', category='栈', slug='decode-string',
        inp='一行：字符串 s，形如 k[encoded_string]，支持嵌套。',
        outp='一行，解码后的字符串。',
        sample_in='2\n3[a2[c]]\n2[abc]3[cd]ef\n',
        sample_out='accaccacc\nabcabccdcdcdef\n',
        code=r'''
def solve(it):
    s = next(it)
    num_stack = []
    str_stack = []
    cur = []
    num = 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == "[":
            num_stack.append(num)
            str_stack.append(cur)
            cur = []
            num = 0
        elif c == "]":
            k = num_stack.pop()
            prev = str_stack.pop()
            prev.extend(cur * k)
            cur = prev
        else:
            cur.append(c)
    return "".join(cur)
''',
    ),
    dict(
        num=739, title='每日温度', difficulty='中等', category='栈', slug='daily-temperatures',
        inp='第一行：n；第二行：n 个整数表示每日温度。',
        outp='一行，每天需要等待的天数（不会更高则为 0，空格分隔）。',
        sample_in='2\n8\n73 74 75 71 69 72 76 73\n3\n30 40 50\n',
        sample_out='1 1 4 2 1 1 0 0\n1 1 0\n',
        code=r'''
def solve(it):
    n = int(next(it))
    t = [int(next(it)) for _ in range(n)]
    res = [0] * n
    stack = []
    for i in range(n):
        while stack and t[i] > t[stack[-1]]:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return " ".join(map(str, res))
''',
    ),
    dict(
        num=84, title='柱状图中最大的矩形', difficulty='困难', category='栈', slug='largest-rectangle-in-histogram',
        inp='第一行：n；第二行：n 个非负整数表示柱子高度。',
        outp='一行，最大矩形面积。',
        sample_in='3\n6\n2 1 5 6 2 3\n2\n2 4\n1\n0\n',
        sample_out='10\n4\n0\n',
        code=r'''
def solve(it):
    n = int(next(it))
    h = [int(next(it)) for _ in range(n)]
    h = h + [0]
    stack = []
    best = 0
    for i, x in enumerate(h):
        while stack and h[stack[-1]] > x:
            j = stack.pop()
            left = stack[-1] if stack else -1
            area = h[j] * (i - left - 1)
            if area > best:
                best = area
        stack.append(i)
    return best
''',
    ),
]
