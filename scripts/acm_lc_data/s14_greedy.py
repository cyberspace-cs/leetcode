# -*- coding: utf-8 -*-
"""贪心算法分类 · 个人模板风格（单组输入）。"""

PROBLEMS = [
    dict(
        num=121, func='max_profit', params=[('prices', 'List[int]')], ret='int',
        body='''    # 在这里写你的代码
    low = prices[0]
    best = 0
    for p in prices[1:]:
        best = max(best, p - low)
        low = min(low, p)
    return best''',
        main='''    prices = eval(input())
    print(max_profit(prices))''',
        inp='一行：每日股价列表，如 [7,1,5,3,6,4]。',
        sample_in='[7,1,5,3,6,4]\n',
        sample_out='5\n',
    ),
    dict(
        num=55, func='can_jump', params=[('nums', 'List[int]')], ret='bool',
        body='''    # 在这里写你的代码
    reach = 0
    for i, x in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + x)
    return True''',
        main='''    nums = eval(input())
    print(can_jump(nums))''',
        inp='一行：每格最大跳跃长度，如 [2,3,1,1,4]。',
        sample_in='[2,3,1,1,4]\n',
        sample_out='True\n',
    ),
    dict(
        num=45, func='jump', params=[('nums', 'List[int]')], ret='int',
        body='''    # 在这里写你的代码（贪心分层）
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps''',
        main='''    nums = eval(input())
    print(jump(nums))''',
        inp='一行：每格最大跳跃长度（保证可到达终点），如 [2,3,1,1,4]。',
        sample_in='[2,3,1,1,4]\n',
        sample_out='2\n',
    ),
    dict(
        num=763, func='partition_labels', params=[('s', 'str')], ret='List[int]',
        body='''    # 在这里写你的代码
    last = {}
    for i, ch in enumerate(s):
        last[ch] = i
    res = []
    start = end = 0
    for i, ch in enumerate(s):
        end = max(end, last[ch])
        if i == end:
            res.append(end - start + 1)
            start = i + 1
    return res''',
        main='''    s = input()
    print(partition_labels(s))''',
        inp='一行：字符串（仅含小写字母），如 ababcbacadefegdehijhklij。',
        sample_in='ababcbacadefegdehijhklij\n',
        sample_out='[9, 7, 8]\n',
    ),
]
