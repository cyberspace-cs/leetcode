# -*- coding: utf-8 -*-
"""滑动窗口分类的 ACM 模式完整解题。"""

PROBLEMS = [
    dict(
        num=3, title='无重复字符的最长子串', difficulty='中等', category='滑动窗口',
        slug='longest-substring-without-repeating-characters',
        inp='一行：字符串 s（不含空白字符）。',
        outp='一行，不含重复字符的最长子串长度。',
        sample_in='3\nabcabcbb\nbbbbb\npwwkew\n',
        sample_out='3\n1\n3\n',
        code=r'''
def solve(it):
    s = next(it)
    last = {}
    left = best = 0
    for i, c in enumerate(s):
        if c in last and last[c] >= left:
            left = last[c] + 1
        last[c] = i
        if i - left + 1 > best:
            best = i - left + 1
    return best
''',
    ),
    dict(
        num=438, title='找到字符串中所有字母异位词', difficulty='中等', category='滑动窗口',
        slug='find-all-anagrams-in-a-string',
        inp='第一行：字符串 s；第二行：字符串 p（均不含空白字符）。',
        outp='第一行：个数 g；随后 g 行，每行一个升序排列的起始下标；无解时仅输出 0。',
        sample_in='2\ncbaebabacd\nabc\nabab\nab\n',
        sample_out='2\n0\n6\n3\n0\n1\n2\n',
        code=r'''
def solve(it):
    s = next(it)
    p = next(it)
    need = [0] * 26
    for c in p:
        need[ord(c) - 97] += 1
    win = [0] * 26
    k = len(p)
    res = []
    for i, c in enumerate(s):
        win[ord(c) - 97] += 1
        if i >= k:
            win[ord(s[i - k]) - 97] -= 1
        if i >= k - 1 and win == need:
            res.append(i - k + 1)
    return "\n".join([str(len(res))] + [str(x) for x in res])
''',
    ),
]
