# -*- coding: utf-8 -*-
"""动态规划分类 · 个人模板风格（单组输入）。"""

PROBLEMS = [
    dict(
        num=70, func='climb_stairs', params=[('n', 'int')], ret='int',
        body='''    # 在这里写你的代码
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a''',
        main='''    n = int(input())
    print(climb_stairs(n))''',
        inp='一行：n（台阶数）。',
        sample_in='3\n',
        sample_out='3\n',
    ),
    dict(
        num=118, func='generate', params=[('num_rows', 'int')], ret='List[List[int]]',
        body='''    # 在这里写你的代码
    res = []
    row = []
    for _ in range(num_rows):
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1] if row else [1]
        res.append(row)
    return res''',
        main='''    num_rows = int(input())
    print(generate(num_rows))''',
        inp='一行：numRows（行数）。',
        sample_in='5\n',
        sample_out='[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]\n',
    ),
    dict(
        num=198, func='rob', params=[('nums', 'List[int]')], ret='int',
        body='''    # 在这里写你的代码
    prev = cur = 0
    for x in nums:
        prev, cur = cur, max(cur, prev + x)
    return cur''',
        main='''    nums = eval(input())
    print(rob(nums))''',
        inp='一行：每栋房屋金额，如 [2,7,9,3,1]。',
        sample_in='[2,7,9,3,1]\n',
        sample_out='12\n',
    ),
    dict(
        num=279, func='num_squares', params=[('n', 'int')], ret='int',
        body='''    # 在这里写你的代码（完全背包）
    dp = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        sq = i * i
        for j in range(sq, n + 1):
            dp[j] = min(dp[j], dp[j - sq] + 1)
    return dp[n]''',
        main='''    n = int(input())
    print(num_squares(n))''',
        inp='一行：n。',
        sample_in='12\n',
        sample_out='3\n',
    ),
    dict(
        num=322, func='coin_change',
        params=[('coins', 'List[int]'), ('amount', 'int')], ret='int',
        body='''    # 在这里写你的代码
    INF = float("inf")
    dp = [0] + [INF] * amount
    for j in range(1, amount + 1):
        for c in coins:
            if c <= j and dp[j - c] + 1 < dp[j]:
                dp[j] = dp[j - c] + 1
    return dp[amount] if dp[amount] != INF else -1''',
        main='''    coins = eval(input())
    amount = int(input())
    print(coin_change(coins, amount))''',
        inp='第一行：硬币面额列表；第二行：amount。',
        sample_in='[1,2,5]\n11\n',
        sample_out='3\n',
    ),
    dict(
        num=139, func='word_break',
        params=[('s', 'str'), ('word_dict', 'List[str]')], ret='bool',
        body='''    # 在这里写你的代码
    words = set(word_dict)
    max_len = max((len(w) for w in words), default=0)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(max(0, i - max_len), i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]''',
        main='''    s = input()
    word_dict = eval(input())
    print(word_break(s, word_dict))''',
        inp='第一行：字符串 s；第二行：单词列表，如 ["leet","code"]。',
        sample_in='leetcode\n["leet","code"]\n',
        sample_out='True\n',
    ),
    dict(
        num=300, func='length_of_lis', params=[('nums', 'List[int]')], ret='int',
        body='''    # 在这里写你的代码（贪心 + 二分）
    import bisect
    tails = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)''',
        main='''    nums = eval(input())
    print(length_of_lis(nums))''',
        inp='一行：整数列表，如 [10,9,2,5,3,7,101,18]。',
        sample_in='[10,9,2,5,3,7,101,18]\n',
        sample_out='4\n',
    ),
    dict(
        num=152, func='max_product', params=[('nums', 'List[int]')], ret='int',
        body='''    # 在这里写你的代码（同时维护最大 / 最小乘积）
    hi = lo = best = nums[0]
    for x in nums[1:]:
        if x < 0:
            hi, lo = lo, hi
        hi = max(x, hi * x)
        lo = min(x, lo * x)
        best = max(best, hi)
    return best''',
        main='''    nums = eval(input())
    print(max_product(nums))''',
        inp='一行：整数列表，如 [2,3,-2,4]。',
        sample_in='[2,3,-2,4]\n',
        sample_out='6\n',
    ),
    dict(
        num=416, func='can_partition', params=[('nums', 'List[int]')], ret='bool',
        body='''    # 在这里写你的代码（01 背包）
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for j in range(target, x - 1, -1):
            if dp[j - x]:
                dp[j] = True
    return dp[target]''',
        main='''    nums = eval(input())
    print(can_partition(nums))''',
        inp='一行：正整数列表，如 [1,5,11,5]。',
        sample_in='[1,5,11,5]\n',
        sample_out='True\n',
    ),
    dict(
        num=32, func='longest_valid_parentheses', params=[('s', 'str')], ret='int',
        body='''    # 在这里写你的代码（DP：dp[i] 表示以 i 结尾的最长有效长度）
    n = len(s)
    dp = [0] * n
    best = 0
    for i in range(1, n):
        if s[i] != ")":
            continue
        if s[i - 1] == "(":
            dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
        else:
            j = i - dp[i - 1] - 1
            if j >= 0 and s[j] == "(":
                dp[i] = dp[i - 1] + 2 + (dp[j - 1] if j >= 1 else 0)
        best = max(best, dp[i])
    return best''',
        main='''    s = input()
    print(longest_valid_parentheses(s))''',
        inp='一行：括号字符串，如 ()())。',
        sample_in=')()())\n',
        sample_out='4\n',
    ),
]
