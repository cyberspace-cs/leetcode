# -*- coding: utf-8 -*-
"""技巧分类 · 个人模板风格（单组输入）。"""

PROBLEMS = [
    dict(
        num=136, func='single_number', params=[('nums', 'List[int]')], ret='int',
        body='''    # 在这里写你的代码（异或）
    x = 0
    for v in nums:
        x ^= v
    return x''',
        main='''    nums = eval(input())
    print(single_number(nums))''',
        inp='一行：整数列表（除一个数字外其余均出现两次），如 [4,1,2,1,2]。',
        sample_in='[4,1,2,1,2]\n',
        sample_out='4\n',
    ),
    dict(
        num=169, func='majority_element', params=[('nums', 'List[int]')], ret='int',
        body='''    # 在这里写你的代码（Boyer-Moore 投票）
    cand = None
    count = 0
    for x in nums:
        if count == 0:
            cand = x
            count = 1
        elif x == cand:
            count += 1
        else:
            count -= 1
    return cand''',
        main='''    nums = eval(input())
    print(majority_element(nums))''',
        inp='一行：整数列表（保证存在出现次数 > n/2 的元素）。',
        sample_in='[2,2,1,1,1,2,2]\n',
        sample_out='2\n',
    ),
    dict(
        num=75, func='sort_colors', params=[('nums', 'List[int]')], ret='List[int]',
        body='''    # 在这里写你的代码（荷兰国旗三指针）
    p0, i, p2 = 0, 0, len(nums) - 1
    while i <= p2:
        if nums[i] == 0:
            nums[p0], nums[i] = nums[i], nums[p0]
            p0 += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[p2] = nums[p2], nums[i]
            p2 -= 1
        else:
            i += 1
    return nums''',
        main='''    nums = eval(input())
    print(sort_colors(nums))''',
        inp='一行：只含 0、1、2 的列表，如 [2,0,2,1,1,0]。',
        sample_in='[2,0,2,1,1,0]\n',
        sample_out='[0, 0, 1, 1, 2, 2]\n',
    ),
    dict(
        num=31, func='next_permutation', params=[('nums', 'List[int]')], ret='List[int]',
        body='''    # 在这里写你的代码
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])
    return nums''',
        main='''    nums = eval(input())
    print(next_permutation(nums))''',
        inp='一行：整数列表，如 [1,2,3]。',
        sample_in='[1,2,3]\n',
        sample_out='[1, 3, 2]\n',
    ),
    dict(
        num=287, func='find_duplicate', params=[('nums', 'List[int]')], ret='int',
        body='''    # 在这里写你的代码（Floyd 判圈找环入口）
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow''',
        main='''    nums = eval(input())
    print(find_duplicate(nums))''',
        inp='一行：整数列表（长度 n，取值 1..n-1，仅一个数字重复），如 [1,3,4,2,2]。',
        sample_in='[1,3,4,2,2]\n',
        sample_out='2\n',
    ),
]
