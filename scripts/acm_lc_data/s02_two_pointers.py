# -*- coding: utf-8 -*-
"""双指针分类 · 个人模板风格（单组输入）。"""

PROBLEMS = [
    dict(
        num=283, func='move_zeroes', params=[('nums', 'List[int]')], ret='List[int]',
        body='''    # 在这里写你的代码（原地修改 nums 后返回）
    non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero] = nums[i]
            non_zero += 1
    for i in range(non_zero, len(nums)):
        nums[i] = 0
    return nums''',
        main='''    nums = eval(input())
    print(move_zeroes(nums))''',
        inp='一行：整数列表，如 [0,1,0,3,12]。',
        sample_in='[0,1,0,3,12]\n',
        sample_out='[1, 3, 12, 0, 0]\n',
    ),
    dict(
        num=11, func='max_area', params=[('height', 'List[int]')], ret='int',
        body='''    # 在这里写你的代码
    ans = 0
    left, right = 0, len(height) - 1
    while left < right:
        h = min(height[left], height[right])
        ans = max(ans, h * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return ans''',
        main='''    height = eval(input())
    print(max_area(height))''',
        inp='一行：高度列表，如 [1,8,6,2,5,4,8,3,7]。',
        sample_in='[1,8,6,2,5,4,8,3,7]\n',
        sample_out='49\n',
    ),
    dict(
        num=15, func='three_sum', params=[('nums', 'List[int]')], ret='List[List[int]]',
        body='''    # 在这里写你的代码
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return res''',
        main='''    nums = eval(input())
    print(three_sum(nums))''',
        inp='一行：整数列表，如 [-1,0,1,2,-1,-4]。',
        sample_in='[-1,0,1,2,-1,-4]\n',
        sample_out='[[-1, -1, 2], [-1, 0, 1]]\n',
    ),
    dict(
        num=42, func='trap', params=[('height', 'List[int]')], ret='int',
        body='''    # 在这里写你的代码
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    result = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            result += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            result += right_max - height[right]
            right -= 1
    return result''',
        main='''    height = eval(input())
    print(trap(height))''',
        inp='一行：柱高列表，如 [0,1,0,2,1,0,1,3,2,1,2,1]。',
        sample_in='[0,1,0,2,1,0,1,3,2,1,2,1]\n',
        sample_out='6\n',
    ),
]
