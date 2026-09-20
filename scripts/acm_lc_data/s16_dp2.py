# -*- coding: utf-8 -*-
"""多维动态规划分类 · 个人模板风格（单组输入）。"""

PROBLEMS = [
    dict(
        num=62, func='unique_paths', params=[('m', 'int'), ('n', 'int')], ret='int',
        body='''    # 在这里写你的代码（一维滚动）
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[n - 1]''',
        main='''    m = int(input())
    n = int(input())
    print(unique_paths(m, n))''',
        inp='第一行：m；第二行：n。',
        sample_in='3\n7\n',
        sample_out='28\n',
    ),
    dict(
        num=64, func='min_path_sum', params=[('grid', 'List[List[int]]')], ret='int',
        body='''    # 在这里写你的代码（原地更新）
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i == 0:
                grid[i][j] += grid[i][j - 1]
            elif j == 0:
                grid[i][j] += grid[i - 1][j]
            else:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    return grid[m - 1][n - 1]''',
        main='''    grid = eval(input())
    print(min_path_sum(grid))''',
        inp='一行：二维非负整数列表，如 [[1,3,1],[1,5,1],[4,2,1]]。',
        sample_in='[[1,3,1],[1,5,1],[4,2,1]]\n',
        sample_out='7\n',
    ),
    dict(
        num=5, func='longest_palindrome', params=[('s', 'str')], ret='str',
        body='''    # 在这里写你的代码（中心扩展）
    n = len(s)
    if n == 0:
        return ""
    start, best = 0, 1
    for i in range(n):
        for l, r in ((i, i), (i, i + 1)):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            length = r - l - 1
            if length > best:
                best = length
                start = l + 1
    return s[start:start + best]''',
        main='''    s = input()
    print(longest_palindrome(s))''',
        inp='一行：字符串 s，如 babad。',
        sample_in='babad\n',
        sample_out='bab\n',
    ),
    dict(
        num=1143, func='longest_common_subsequence',
        params=[('text1', 'str'), ('text2', 'str')], ret='int',
        body='''    # 在这里写你的代码（一维滚动）
    n, m = len(text1), len(text2)
    dp = [0] * (m + 1)
    for i in range(1, n + 1):
        prev = 0
        for j in range(1, m + 1):
            tmp = dp[j]
            if text1[i - 1] == text2[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = tmp
    return dp[m]''',
        main='''    text1 = input()
    text2 = input()
    print(longest_common_subsequence(text1, text2))''',
        inp='第一行：字符串 text1；第二行：字符串 text2。',
        sample_in='abcde\nace\n',
        sample_out='3\n',
    ),
    dict(
        num=72, func='min_distance',
        params=[('word1', 'str'), ('word2', 'str')], ret='int',
        body='''    # 在这里写你的代码（一维滚动）
    n, m = len(word1), len(word2)
    dp = list(range(m + 1))
    for i in range(1, n + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, m + 1):
            tmp = dp[j]
            if word1[i - 1] == word2[j - 1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(prev, dp[j], dp[j - 1])
            prev = tmp
    return dp[m]''',
        main='''    word1 = input()
    word2 = input()
    print(min_distance(word1, word2))''',
        inp='第一行：word1；第二行：word2。',
        sample_in='horse\nros\n',
        sample_out='3\n',
    ),
]
