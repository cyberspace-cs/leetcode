# -*- coding: utf-8 -*-
"""二分查找分类 · 个人模板风格（单组输入）。"""

PROBLEMS = [
    dict(
        num=35, func='search_insert', params=[('nums', 'List[int]'), ('target', 'int')], ret='int',
        body='''    # 在这里写你的代码
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo''',
        main='''    nums = eval(input())
    target = int(input())
    print(search_insert(nums, target))''',
        inp='第一行：升序整数列表；第二行：target。',
        sample_in='[1,3,5,6]\n5\n',
        sample_out='2\n',
    ),
    dict(
        num=74, func='search_matrix',
        params=[('matrix', 'List[List[int]]'), ('target', 'int')], ret='bool',
        body='''    # 在这里写你的代码（整体视为一维升序数组做二分）
    if not matrix:
        return False
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        v = matrix[mid // n][mid % n]
        if v == target:
            return True
        if v < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False''',
        main='''    matrix = eval(input())
    target = int(input())
    print(search_matrix(matrix, target))''',
        inp='第一行：二维列表（每行升序，且每行首元素大于上一行末元素）；第二行：target。',
        sample_in='[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n',
        sample_out='True\n',
    ),
    dict(
        num=34, func='search_range', params=[('nums', 'List[int]'), ('target', 'int')], ret='List[int]',
        body='''    # 在这里写你的代码（两次二分求左右边界）
    def lower_bound(x):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    left = lower_bound(target)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    return [left, lower_bound(target + 1) - 1]''',
        main='''    nums = eval(input())
    target = int(input())
    print(search_range(nums, target))''',
        inp='第一行：升序整数列表；第二行：target。',
        sample_in='[5,7,7,8,8,10]\n8\n',
        sample_out='[3, 4]\n',
    ),
    dict(
        num=33, func='search', params=[('nums', 'List[int]'), ('target', 'int')], ret='int',
        body='''    # 在这里写你的代码
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1''',
        main='''    nums = eval(input())
    target = int(input())
    print(search(nums, target))''',
        inp='第一行：旋转后的升序整数列表（元素互不相同）；第二行：target。',
        sample_in='[4,5,6,7,0,1,2]\n0\n',
        sample_out='4\n',
    ),
    dict(
        num=153, func='find_min', params=[('nums', 'List[int]')], ret='int',
        body='''    # 在这里写你的代码
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]''',
        main='''    nums = eval(input())
    print(find_min(nums))''',
        inp='一行：旋转后的升序整数列表（元素互不相同），如 [3,4,5,1,2]。',
        sample_in='[3,4,5,1,2]\n',
        sample_out='1\n',
    ),
    dict(
        num=4, func='find_median_sorted_arrays',
        params=[('nums1', 'List[int]'), ('nums2', 'List[int]')], ret='float',
        body='''    # 在这里写你的代码（在较短数组上二分划分点）
    a, b = nums1, nums2
    if len(a) > len(b):
        a, b = b, a
    n, m = len(a), len(b)
    total = n + m
    half = (total + 1) // 2
    lo, hi = 0, n
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        left_a = a[i - 1] if i > 0 else float("-inf")
        right_a = a[i] if i < n else float("inf")
        left_b = b[j - 1] if j > 0 else float("-inf")
        right_b = b[j] if j < m else float("inf")
        if left_a > right_b:
            hi = i - 1
        elif left_b > right_a:
            lo = i + 1
        else:
            if total % 2:
                return float(max(left_a, left_b))
            return (max(left_a, left_b) + min(right_a, right_b)) / 2.0
    return 0.0''',
        main='''    nums1 = eval(input())
    nums2 = eval(input())
    print(find_median_sorted_arrays(nums1, nums2))''',
        inp='第一行：升序数组1；第二行：升序数组2。',
        sample_in='[1,3]\n[2]\n',
        sample_out='2.0\n',
    ),
]
