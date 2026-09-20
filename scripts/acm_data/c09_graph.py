# -*- coding: utf-8 -*-
"""图论分类的 ACM 模式完整解题。"""

PROBLEMS = [
    dict(
        num=200, title='岛屿数量', difficulty='中等', category='图论', slug='number-of-islands',
        inp='第一行：m n；随后 m 行，每行 n 个以空格分隔的字符（0 或 1）。',
        outp='一行，岛屿（上下左右相连的 1）数量。',
        sample_in='2\n4 5\n1 1 1 1 0\n1 1 0 1 0\n1 1 0 0 0\n0 0 0 0 0\n3 3\n1 1 0\n1 0 0\n0 0 1\n',
        sample_out='1\n2\n',
        code=r'''
def solve(it):
    m = int(next(it))
    n = int(next(it))
    g = [[next(it) for _ in range(n)] for _ in range(m)]
    seen = [[False] * n for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == "1" and not seen[i][j]:
                cnt += 1
                seen[i][j] = True
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and g[nx][ny] == "1" and not seen[nx][ny]:
                            seen[nx][ny] = True
                            stack.append((nx, ny))
    return cnt
''',
    ),
    dict(
        num=994, title='腐烂的橘子', difficulty='中等', category='图论', slug='rotting-oranges',
        inp='第一行：m n；随后 m 行，每行 n 个整数（0 空格子 / 1 新鲜 / 2 腐烂）。',
        outp='一行，所有橘子腐烂所需的最少分钟数；不可能则输出 -1。',
        sample_in='3\n3 3\n2 1 1\n1 1 0\n0 1 1\n3 3\n2 1 1\n0 1 1\n1 0 1\n1 1\n0\n',
        sample_out='4\n-1\n0\n',
        code=r'''
from collections import deque


def solve(it):
    m = int(next(it))
    n = int(next(it))
    g = [[int(next(it)) for _ in range(n)] for _ in range(m)]
    dq = deque()
    fresh = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == 2:
                dq.append((i, j, 0))
            elif g[i][j] == 1:
                fresh += 1
    minutes = 0
    while dq:
        i, j, t = dq.popleft()
        if t > minutes:
            minutes = t
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and g[x][y] == 1:
                g[x][y] = 2
                fresh -= 1
                dq.append((x, y, t + 1))
    return minutes if fresh == 0 else -1
''',
    ),
    dict(
        num=207, title='课程表', difficulty='中等', category='图论', slug='course-schedule',
        inp='第一行：numCourses E；随后 E 行，每行 a b，表示 b 是 a 的先修课（先修 b 才能修 a）。',
        outp='一行，true 或 false，表示能否修完所有课程。',
        sample_in='3\n2 1\n1 0\n2 2\n1 0\n0 1\n3 2\n1 0\n2 1\n',
        sample_out='true\nfalse\ntrue\n',
        code=r'''
from collections import deque


def solve(it):
    nc = int(next(it))
    e = int(next(it))
    adj = [[] for _ in range(nc)]
    indeg = [0] * nc
    for _ in range(e):
        a = int(next(it))
        b = int(next(it))
        adj[b].append(a)
        indeg[a] += 1
    dq = deque(i for i in range(nc) if indeg[i] == 0)
    seen = 0
    while dq:
        u = dq.popleft()
        seen += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                dq.append(v)
    return "true" if seen == nc else "false"
''',
    ),
    dict(
        num=208, title='实现 Trie (前缀树)', difficulty='中等', category='图论', slug='implement-trie-prefix-tree',
        inp='第一行：q；随后 q 行，每行为 insert word / search word / startsWith prefix。',
        outp='一行，按顺序输出所有 search 与 startsWith 的结果（true/false，空格分隔）；若无查询输出 EMPTY。',
        sample_in='1\n8\ninsert apple\nsearch apple\nsearch app\nstartsWith app\ninsert app\nsearch app\nstartsWith app\nsearch banana\n',
        sample_out='true false true true true false\n',
        code=r'''
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node["#"] = True

    def _walk(self, s):
        node = self.root
        for c in s:
            if c not in node:
                return None
            node = node[c]
        return node

    def search(self, word):
        node = self._walk(word)
        return bool(node) and node.get("#", False)

    def startsWith(self, prefix):
        return self._walk(prefix) is not None


def solve(it):
    q = int(next(it))
    tr = Trie()
    out = []
    for _ in range(q):
        op = next(it)
        w = next(it)
        if op == "insert":
            tr.insert(w)
        elif op == "search":
            out.append("true" if tr.search(w) else "false")
        else:
            out.append("true" if tr.startsWith(w) else "false")
    return " ".join(out) if out else "EMPTY"
''',
    ),
]
