# -*- coding: utf-8 -*-
"""哈希分类 · 个人模板风格（单组输入）。"""

PROBLEMS = [
    dict(
        num=1, func='two_sum', params=[('nums', 'List[int]'), ('target', 'int')], ret='List[int]',
        body='''    # 在这里写你的代码
    hashmap = {}
    for i, x in enumerate(nums):
        if target - x in hashmap:
            return [hashmap[target - x], i]
        hashmap[x] = i
    return []''',
        main='''    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())
    print(two_sum(nums, target))''',
        inp='第一行：n；第二行：n 个整数；第三行：target。',
        sample_in='4\n2 7 11 15\n9\n',
        sample_out='[0, 1]\n',
    ),
    dict(
        num=49, func='group_anagrams', params=[('strs', 'List[str]')], ret='List[List[str]]',
        body='''    # 在这里写你的代码
    from collections import defaultdict
    groups = defaultdict(list)
    for s in strs:
        groups[''.join(sorted(s))].append(s)
    return list(groups.values())''',
        main='''    strs = eval(input())
    print(group_anagrams(strs))''',
        inp='一行：字符串列表，如 ["eat","tea","tan","ate","nat","bat"]。',
        sample_in='["eat","tea","tan","ate","nat","bat"]\n',
        sample_out="[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]\n",
    ),
    dict(
        num=128, func='longest_consecutive', params=[('nums', 'List[int]')], ret='int',
        body='''    # 在这里写你的代码
    if not nums:
        return 0
    num_set = set(nums)
    max_length = 0
    for num in num_set:
        if num - 1 not in num_set:
            current = num
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            max_length = max(max_length, length)
    return max_length''',
        main='''    nums = eval(input())
    print(longest_consecutive(nums))''',
        inp='一行：整数列表，如 [100,4,200,1,3,2]。',
        sample_in='[100,4,200,1,3,2]\n',
        sample_out='4\n',
    ),
]
