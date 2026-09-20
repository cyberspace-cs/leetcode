# -*- coding: utf-8 -*-
"""回溯分类 · 个人模板风格（单组输入）。"""

PROBLEMS = [
    dict(
        num=46, func='permute', params=[('nums', 'List[int]')], ret='List[List[int]]',
        body='''    # 在这里写你的代码
    res = []
    used = [False] * len(nums)
    path = []

    def backtrack():
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return res''',
        main='''    nums = eval(input())
    print(permute(nums))''',
        inp='一行：互不相同的整数列表，如 [1,2,3]。',
        sample_in='[1,2,3]\n',
        sample_out='[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]\n',
    ),
    dict(
        num=78, func='subsets', params=[('nums', 'List[int]')], ret='List[List[int]]',
        body='''    # 在这里写你的代码
    res = []
    path = []

    def backtrack(start):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return res''',
        main='''    nums = eval(input())
    print(subsets(nums))''',
        inp='一行：互不相同的整数列表，如 [1,2,3]。',
        sample_in='[1,2,3]\n',
        sample_out='[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]\n',
    ),
    dict(
        num=17, func='letter_combinations', params=[('digits', 'str')], ret='List[str]',
        body='''    # 在这里写你的代码
    if not digits:
        return []
    table = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
    }
    res = []

    def backtrack(i, cur):
        if i == len(digits):
            res.append(cur)
            return
        for ch in table[digits[i]]:
            backtrack(i + 1, cur + ch)

    backtrack(0, "")
    return res''',
        main='''    digits = input()
    print(letter_combinations(digits))''',
        inp='一行：数字字符串（仅含 2-9），如 23。',
        sample_in='23\n',
        sample_out="['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']\n",
    ),
    dict(
        num=39, func='combination_sum',
        params=[('candidates', 'List[int]'), ('target', 'int')], ret='List[List[int]]',
        body='''    # 在这里写你的代码
    candidates.sort()
    res = []
    path = []

    def backtrack(start, remain):
        if remain == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                break
            path.append(candidates[i])
            backtrack(i, remain - candidates[i])
            path.pop()

    backtrack(0, target)
    return res''',
        main='''    candidates = eval(input())
    target = int(input())
    print(combination_sum(candidates, target))''',
        inp='第一行：候选数字列表；第二行：target。数字可重复选取。',
        sample_in='[2,3,6,7]\n7\n',
        sample_out='[[2, 2, 3], [7]]\n',
    ),
    dict(
        num=22, func='generate_parenthesis', params=[('n', 'int')], ret='List[str]',
        body='''    # 在这里写你的代码
    res = []

    def backtrack(cur, left, right):
        if len(cur) == 2 * n:
            res.append(cur)
            return
        if left < n:
            backtrack(cur + "(", left + 1, right)
        if right < left:
            backtrack(cur + ")", left, right + 1)

    backtrack("", 0, 0)
    return res''',
        main='''    n = int(input())
    print(generate_parenthesis(n))''',
        inp='一行：n（括号对数）。',
        sample_in='3\n',
        sample_out="['((()))', '(()())', '(())()', '()(())', '()()()']\n",
    ),
    dict(
        num=79, func='exist',
        params=[('board', 'List[List[str]]'), ('word', 'str')], ret='bool',
        body='''    # 在这里写你的代码
    if not board:
        return False
    m, n = len(board), len(board[0])

    def dfs(i, j, k):
        if board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        tmp = board[i][j]
        board[i][j] = "#"
        found = False
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and dfs(x, y, k + 1):
                found = True
                break
        board[i][j] = tmp
        return found

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    return False''',
        main='''    board = eval(input())
    word = input()
    print(exist(board, word))''',
        inp='第一行：二维字符网格；第二行：单词 word。',
        sample_in='[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\nABCCED\n',
        sample_out='True\n',
    ),
    dict(
        num=131, func='partition', params=[('s', 'str')], ret='List[List[str]]',
        body='''    # 在这里写你的代码
    res = []
    path = []
    n = len(s)

    def is_palindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def backtrack(start):
        if start == n:
            res.append(path[:])
            return
        for end in range(start, n):
            if is_palindrome(start, end):
                path.append(s[start:end + 1])
                backtrack(end + 1)
                path.pop()

    backtrack(0)
    return res''',
        main='''    s = input()
    print(partition(s))''',
        inp='一行：字符串 s（仅含小写字母），如 aab。',
        sample_in='aab\n',
        sample_out="[['a', 'a', 'b'], ['aa', 'b']]\n",
    ),
    dict(
        num=51, func='solve_n_queens', params=[('n', 'int')], ret='List[List[str]]',
        body='''    # 在这里写你的代码
    res = []
    cols = set()
    diag1 = set()
    diag2 = set()
    board = [["."] * n for _ in range(n)]

    def backtrack(row):
        if row == n:
            res.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board[row][col] = "Q"
            backtrack(row + 1)
            cols.discard(col)
            diag1.discard(row - col)
            diag2.discard(row + col)
            board[row][col] = "."

    backtrack(0)
    return res''',
        main='''    n = int(input())
    print(solve_n_queens(n))''',
        inp='一行：n（棋盘大小）。',
        sample_in='4\n',
        sample_out="[['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]\n",
    ),
]
