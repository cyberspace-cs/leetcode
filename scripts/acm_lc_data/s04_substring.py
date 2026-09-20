# -*- coding: utf-8 -*-
"""子串分类 · 个人模板风格（单组输入）。"""

PROBLEMS = [
    dict(
        num=560, func='subarray_sum', params=[('nums', 'List[int]'), ('k', 'int')], ret='int',
        body='''    # 在这里写你的代码
    count = {0: 1}
    prefix = 0
    res = 0
    for x in nums:
        prefix += x
        res += count.get(prefix - k, 0)
        count[prefix] = count.get(prefix, 0) + 1
    return res''',
        main='''    nums = eval(input())
    k = int(input())
    print(subarray_sum(nums, k))''',
        inp='第一行：整数列表；第二行：k。',
        sample_in='[1,1,1]\n2\n',
        sample_out='2\n',
    ),
    dict(
        num=239, func='max_sliding_window', params=[('nums', 'List[int]'), ('k', 'int')], ret='List[int]',
        body='''    # 在这里写你的代码
    from collections import deque
    dq = deque()
    res = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res''',
        main='''    nums = eval(input())
    k = int(input())
    print(max_sliding_window(nums, k))''',
        inp='第一行：整数列表；第二行：窗口大小 k。',
        sample_in='[1,3,-1,-3,5,3,6,7]\n3\n',
        sample_out='[3, 3, 5, 5, 6, 7]\n',
    ),
    dict(
        num=76, func='min_window', params=[('s', 'str'), ('t', 'str')], ret='str',
        body='''    # 在这里写你的代码
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    missing = len(t)
    left = 0
    best = None
    for right, ch in enumerate(s):
        if need.get(ch, 0) > 0:
            missing -= 1
        need[ch] = need.get(ch, 0) - 1
        while missing == 0:
            if best is None or right - left + 1 < best[1] - best[0] + 1:
                best = (left, right)
            need[s[left]] = need.get(s[left], 0) + 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return s[best[0]:best[1] + 1] if best else ""''',
        main='''    s = input()
    t = input()
    print(min_window(s, t))''',
        inp='第一行：字符串 s；第二行：字符串 t。',
        sample_in='ADOBECODEBANC\nABC\n',
        sample_out='BANC\n',
    ),
]
