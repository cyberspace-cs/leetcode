# -*- coding: utf-8 -*-
"""回溯分类的 ACM 模式完整解题。"""

PROBLEMS = [
    dict(
        num=46, title='全排列', difficulty='中等', category='回溯', slug='permutations',
        inp='第一行：n；第二行：n 个互不相同的整数。',
        outp='第一行：排列个数 g；随后 g 行，每行一个排列（空格分隔），按回溯顺序输出。',
        sample_in='2\n3\n1 2 3\n2\n0 1\n',
        sample_out='6\n1 2 3\n1 3 2\n2 1 3\n2 3 1\n3 1 2\n3 2 1\n2\n0 1\n1 0\n',
        code=r'''
def solve(it):
    n = int(next(it))
    nums = [int(next(it)) for _ in range(n)]
    res = []
    used = [False] * n
    path = []

    def bt():
        if len(path) == n:
            res.append(" ".join(map(str, path)))
            return
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            bt()
            path.pop()
            used[i] = False

    bt()
    return "\n".join([str(len(res))] + res)
''',
    ),
    dict(
        num=78, title='子集', difficulty='中等', category='回溯', slug='subsets',
        inp='第一行：n；第二行：n 个互不相同的整数。',
        outp='第一行：子集个数 g；随后 g 行，每行一个子集（空格分隔）。\n'
             '空子集输出为一个空行；整体按回溯顺序（依次选择 / 不选择）。',
        sample_in='1\n3\n1 2 3\n',
        sample_out='8\n\n1\n1 2\n1 2 3\n1 3\n2\n2 3\n3\n',
        code=r'''
def solve(it):
    n = int(next(it))
    nums = [int(next(it)) for _ in range(n)]
    res = []
    path = []

    def bt(start):
        res.append(" ".join(map(str, path)))
        for i in range(start, n):
            path.append(nums[i])
            bt(i + 1)
            path.pop()

    bt(0)
    return "\n".join([str(len(res))] + res)
''',
    ),
    dict(
        num=17, title='电话号码的字母组合', difficulty='中等', category='回溯',
        slug='letter-combinations-of-a-phone-number',
        inp='一行：数字字符串 digits（仅含 2-9）。',
        outp='第一行：组合个数 g；随后 g 行，每行一个字母组合；digits 为空时仅输出 0。',
        sample_in='2\n23\n9\n',
        sample_out='9\nad\nae\naf\nbd\nbe\nbf\ncd\nce\ncf\n4\nw\nx\ny\nz\n',
        code=r'''
def solve(it):
    digits = next(it)
    if not digits:
        return "0"
    table = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
    }
    res = []

    def bt(i, cur):
        if i == len(digits):
            res.append(cur)
            return
        for c in table[digits[i]]:
            bt(i + 1, cur + c)

    bt(0, "")
    return "\n".join([str(len(res))] + res)
''',
    ),
    dict(
        num=39, title='组合总和', difficulty='中等', category='回溯', slug='combination-sum',
        inp='第一行：n target；第二行：n 个互不相同的正整数。',
        outp='第一行：方案数 g；随后 g 行，每行一个非递减组合（空格分隔）；无解时仅输出 0。',
        sample_in='2\n4 7\n2 3 6 7\n1 1\n2\n',
        sample_out='2\n2 2 3\n7\n0\n',
        code=r'''
def solve(it):
    n = int(next(it))
    target = int(next(it))
    cand = sorted(int(next(it)) for _ in range(n))
    res = []
    path = []

    def bt(start, remain):
        if remain == 0:
            res.append(" ".join(map(str, path)))
            return
        for i in range(start, n):
            if cand[i] > remain:
                break
            path.append(cand[i])
            bt(i, remain - cand[i])
            path.pop()

    bt(0, target)
    return "\n".join([str(len(res))] + res)
''',
    ),
    dict(
        num=22, title='括号生成', difficulty='中等', category='回溯', slug='generate-parentheses',
        inp='一行：n，表示括号对数。',
        outp='第一行：方案数 g；随后 g 行，每行一个合法括号串。',
        sample_in='2\n3\n1\n',
        sample_out='5\n((()))\n(()())\n(())()\n()(())\n()()()\n1\n()\n',
        code=r'''
def solve(it):
    n = int(next(it))
    res = []

    def bt(cur, left, right):
        if len(cur) == 2 * n:
            res.append(cur)
            return
        if left < n:
            bt(cur + "(", left + 1, right)
        if right < left:
            bt(cur + ")", left, right + 1)

    bt("", 0, 0)
    return "\n".join([str(len(res))] + res)
''',
    ),
    dict(
        num=79, title='单词搜索', difficulty='中等', category='回溯', slug='word-search',
        inp='第一行：m n；随后 m 行，每行 n 个字符；最后一行：word。',
        outp='一行，true 或 false。',
        sample_in='3\n3 4\nA B C E\nS F C S\nA D E E\nABCCED\n3 4\nA B C E\nS F C S\nA D E E\nABCB\n3 4\nA B C E\nS F C S\nA D E E\nSEE\n',
        sample_out='true\nfalse\ntrue\n',
        code=r'''
def solve(it):
    m = int(next(it))
    n = int(next(it))
    board = [[next(it) for _ in range(n)] for _ in range(m)]
    word = next(it)

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
                return "true"
    return "false"
''',
    ),
    dict(
        num=131, title='分割回文串', difficulty='中等', category='回溯', slug='palindrome-partitioning',
        inp='一行：字符串 s（仅含小写字母）。',
        outp='第一行：方案数 g；随后 g 行，每行若干回文子串（空格分隔）。',
        sample_in='2\naab\na\n',
        sample_out='2\na a b\naa b\n1\na\n',
        code=r'''
def solve(it):
    s = next(it)
    n = len(s)
    res = []
    path = []

    def is_pal(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def bt(start):
        if start == n:
            res.append(" ".join(path))
            return
        for end in range(start, n):
            if is_pal(start, end):
                path.append(s[start:end + 1])
                bt(end + 1)
                path.pop()

    bt(0)
    return "\n".join([str(len(res))] + res)
''',
    ),
    dict(
        num=51, title='N 皇后', difficulty='困难', category='回溯', slug='n-queens',
        inp='一行：n，表示棋盘大小。',
        outp='第一行：方案数 g；随后依次输出每个方案，每个方案占 n 行（Q 表示皇后，. 表示空位）。',
        sample_in='1\n4\n',
        sample_out='2\n.Q..\n...Q\nQ...\n..Q.\n..Q.\nQ...\n...Q\n.Q..\n',
        code=r'''
def solve(it):
    n = int(next(it))
    res = []
    cols = set()
    d1 = set()
    d2 = set()
    board = [["."] * n for _ in range(n)]

    def bt(r):
        if r == n:
            res.append("\n".join("".join(row) for row in board))
            return
        for c in range(n):
            if c in cols or (r - c) in d1 or (r + c) in d2:
                continue
            cols.add(c)
            d1.add(r - c)
            d2.add(r + c)
            board[r][c] = "Q"
            bt(r + 1)
            cols.discard(c)
            d1.discard(r - c)
            d2.discard(r + c)
            board[r][c] = "."

    bt(0)
    return "\n".join([str(len(res))] + res)
''',
    ),
]
