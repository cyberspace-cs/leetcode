# -*- coding: utf-8 -*-
"""滑动窗口分类 · 个人模板风格（单组输入）。"""

PROBLEMS = [
    dict(
        num=3, func='length_of_longest_substring', params=[('s', 'str')], ret='int',
        body='''    # 在这里写你的代码
    char_index = {}
    left = 0
    max_length = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            # 字符在当前窗口内重复，左指针跳到重复字符的下一位
            left = char_index[char] + 1
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length''',
        main='''    s = input()
    print(length_of_longest_substring(s))''',
        inp='一行：字符串 s，如 abcabcbb。',
        sample_in='abcabcbb\n',
        sample_out='3\n',
    ),
    dict(
        num=438, func='find_anagrams', params=[('s', 'str'), ('p', 'str')], ret='List[int]',
        body='''    # 在这里写你的代码
    need = [0] * 26
    for ch in p:
        need[ord(ch) - 97] += 1
    window = [0] * 26
    k = len(p)
    res = []
    for i, ch in enumerate(s):
        window[ord(ch) - 97] += 1
        if i >= k:
            window[ord(s[i - k]) - 97] -= 1
        if i >= k - 1 and window == need:
            res.append(i - k + 1)
    return res''',
        main='''    s = input()
    p = input()
    print(find_anagrams(s, p))''',
        inp='第一行：字符串 s；第二行：字符串 p。',
        sample_in='cbaebabacd\nabc\n',
        sample_out='[0, 6]\n',
    ),
]
