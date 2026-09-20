# -*- coding: utf-8 -*-
"""图论分类 · 个人模板风格（单组输入）。"""

PROBLEMS = [
    dict(
        num=200, func='num_islands', params=[('grid', 'List[List[str]]')], ret='int',
        body='''    # 在这里写你的代码（DFS 洪水填充）
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    seen = [[False] * n for _ in range(m)]
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and not seen[i][j]:
                count += 1
                seen[i][j] = True
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1" and not seen[nx][ny]:
                            seen[nx][ny] = True
                            stack.append((nx, ny))
    return count''',
        main='''    grid = eval(input())
    print(num_islands(grid))''',
        inp='一行：二维字符网格，如 [["1","1","0"],["1","0","0"],["0","0","1"]]。',
        sample_in='[["1","1","0"],["1","0","0"],["0","0","1"]]\n',
        sample_out='2\n',
    ),
    dict(
        num=994, func='oranges_rotting', params=[('grid', 'List[List[int]]')], ret='int',
        body='''    # 在这里写你的代码（多源 BFS）
    from collections import deque
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    dq = deque()
    fresh = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                dq.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1
    minutes = 0
    while dq:
        i, j, t = dq.popleft()
        minutes = max(minutes, t)
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                grid[x][y] = 2
                fresh -= 1
                dq.append((x, y, t + 1))
    return minutes if fresh == 0 else -1''',
        main='''    grid = eval(input())
    print(oranges_rotting(grid))''',
        inp='一行：二维整数网格（0 空格 / 1 新鲜 / 2 腐烂）。',
        sample_in='[[2,1,1],[1,1,0],[0,1,1]]\n',
        sample_out='4\n',
    ),
    dict(
        num=207, func='can_finish',
        params=[('num_courses', 'int'), ('prerequisites', 'List[List[int]]')], ret='bool',
        body='''    # 在这里写你的代码（拓扑排序）
    from collections import deque
    adj = [[] for _ in range(num_courses)]
    indeg = [0] * num_courses
    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1
    dq = deque(i for i in range(num_courses) if indeg[i] == 0)
    seen = 0
    while dq:
        u = dq.popleft()
        seen += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                dq.append(v)
    return seen == num_courses''',
        main='''    num_courses = int(input())
    prerequisites = eval(input())
    print(can_finish(num_courses, prerequisites))''',
        inp='第一行：numCourses；第二行：先修关系列表，如 [[1,0]]（b 是 a 的先修课）。',
        sample_in='2\n[[1,0]]\n',
        sample_out='True\n',
    ),
    dict(
        num=208, func=None, params=[], ret='None',
        code='''class Trie:
    """
    :rtype: None
    """

    def __init__(self):
        # 在这里写你的代码
        self.root = {}

    def insert(self, word: str) -> None:
        # 在这里写你的代码
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["#"] = True

    def _walk(self, s):
        node = self.root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node

    def search(self, word: str) -> bool:
        # 在这里写你的代码
        node = self._walk(word)
        return bool(node) and node.get("#", False)

    def starts_with(self, prefix: str) -> bool:
        # 在这里写你的代码
        return self._walk(prefix) is not None''',
        main='''    ops = eval(input())
    trie = Trie()
    out = []
    for op, word in ops:
        if op == "insert":
            trie.insert(word)
        elif op == "search":
            out.append(trie.search(word))
        else:
            out.append(trie.starts_with(word))
    print(out)''',
        inp='一行：操作列表，如 [["insert","apple"],["search","apple"],["startsWith","app"]]。',
        sample_in='[["insert","apple"],["search","apple"],["search","app"],["startsWith","app"],["insert","app"],["search","app"]]\n',
        sample_out='[True, False, True, True]\n',
    ),
]
