# -*- coding: utf-8 -*-
"""普通数组分类 · 个人模板风格（单组输入）。"""

PROBLEMS = [
    dict(
        num=53, func='max_sub_array', params=[('nums', 'List[int]')], ret='int',
        body='''    # 在这里写你的代码
    cur = best = nums[0]
    for x in nums[1:]:
        cur = x if cur < 0 else cur + x
        best = max(best, cur)
    return best''',
        main='''    nums = eval(input())
    print(max_sub_array(nums))''',
        inp='一行：整数列表，如 [-2,1,-3,4,-1,2,1,-5,4]。',
        sample_in='[-2,1,-3,4,-1,2,1,-5,4]\n',
        sample_out='6\n',
    ),
    dict(
        num=56, func='merge', params=[('intervals', 'List[List[int]]')], ret='List[List[int]]',
        body='''    # 在这里写你的代码
    intervals.sort(key=lambda x: x[0])
    res = []
    for l, r in intervals:
        if res and l <= res[-1][1]:
            res[-1][1] = max(res[-1][1], r)
        else:
            res.append([l, r])
    return res''',
        main='''    intervals = eval(input())
    print(merge(intervals))''',
        inp='一行：区间列表，如 [[1,3],[2,6],[8,10],[15,18]]。',
        sample_in='[[1,3],[2,6],[8,10],[15,18]]\n',
        sample_out='[[1, 6], [8, 10], [15, 18]]\n',
    ),
    dict(
        num=189, func='rotate', params=[('nums', 'List[int]'), ('k', 'int')], ret='List[int]',
        body='''    # 在这里写你的代码（原地修改 nums 后返回）
    n = len(nums)
    if n:
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
    return nums''',
        main='''    nums = eval(input())
    k = int(input())
    print(rotate(nums, k))''',
        inp='第一行：整数列表；第二行：k（向右轮转步数）。',
        sample_in='[1,2,3,4,5,6,7]\n3\n',
        sample_out='[5, 6, 7, 1, 2, 3, 4]\n',
    ),
    dict(
        num=238, func='product_except_self', params=[('nums', 'List[int]')], ret='List[int]',
        body='''    # 在这里写你的代码
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res''',
        main='''    nums = eval(input())
    print(product_except_self(nums))''',
        inp='一行：整数列表，如 [1,2,3,4]。',
        sample_in='[1,2,3,4]\n',
        sample_out='[24, 12, 8, 6]\n',
    ),
    dict(
        num=41, func='first_missing_positive', params=[('nums', 'List[int]')], ret='int',
        body='''    # 在这里写你的代码（原地哈希）
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1''',
        main='''    nums = eval(input())
    print(first_missing_positive(nums))''',
        inp='一行：整数列表，如 [3,4,-1,1]。',
        sample_in='[3,4,-1,1]\n',
        sample_out='2\n',
    ),
]
