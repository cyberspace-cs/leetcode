# -*- coding: utf-8 -*-
"""二叉树分类的 ACM 模式完整解题。"""

COMMON = r'''
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def read_vals(it, n):
    vals = []
    for _ in range(n):
        tok = next(it)
        vals.append(None if tok == "null" else int(tok))
    return vals


def build_tree(vals):
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    dq = deque([root])
    i = 1
    while dq and i < len(vals):
        node = dq.popleft()
        if i < len(vals):
            v = vals[i]
            if v is not None:
                node.left = TreeNode(v)
                dq.append(node.left)
            i += 1
        if i < len(vals):
            v = vals[i]
            if v is not None:
                node.right = TreeNode(v)
                dq.append(node.right)
            i += 1
    return root


def tree_to_str(root):
    if not root:
        return "EMPTY"
    out = []
    dq = deque([root])
    while dq:
        node = dq.popleft()
        if node is None:
            out.append("null")
            continue
        out.append(str(node.val))
        dq.append(node.left)
        dq.append(node.right)
    while out and out[-1] == "null":
        out.pop()
    return " ".join(out)


def dump_list(vals):
    return " ".join(map(str, vals)) if vals else "EMPTY"

'''

TREE_IN = '第一行：n；第二行：n 个 token，每个为整数或 null，按层序（LeetCode 数组形式）描述二叉树。'

PROBLEMS = [
    dict(
        num=94, title='二叉树的中序遍历', difficulty='简单', category='二叉树', slug='binary-tree-inorder-traversal',
        inp=TREE_IN,
        outp='一行，中序遍历结果（空格分隔）；空树输出 EMPTY。',
        sample_in='2\n4\n1 null 2 3\n1\n1\n',
        sample_out='1 3 2\n1\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    root = build_tree(read_vals(it, n))
    res = []
    stack, cur = [], root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return dump_list(res)
''',
    ),
    dict(
        num=104, title='二叉树的最大深度', difficulty='简单', category='二叉树', slug='maximum-depth-of-binary-tree',
        inp=TREE_IN,
        outp='一行，最大深度。',
        sample_in='2\n7\n3 9 20 null null 15 7\n0\n',
        sample_out='3\n0\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    root = build_tree(read_vals(it, n))

    def dep(node):
        if not node:
            return 0
        return 1 + max(dep(node.left), dep(node.right))

    return dep(root)
''',
    ),
    dict(
        num=226, title='翻转二叉树', difficulty='简单', category='二叉树', slug='invert-binary-tree',
        inp=TREE_IN,
        outp='一行，翻转后的二叉树（层序数组形式，空格分隔，去掉尾部 null）。',
        sample_in='2\n7\n4 2 7 1 3 6 9\n1\n1\n',
        sample_out='4 7 2 9 6 3 1\n1\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    root = build_tree(read_vals(it, n))

    def inv(node):
        if not node:
            return None
        node.left, node.right = inv(node.right), inv(node.left)
        return node

    return tree_to_str(inv(root))
''',
    ),
    dict(
        num=101, title='对称二叉树', difficulty='简单', category='二叉树', slug='symmetric-tree',
        inp=TREE_IN,
        outp='一行，true 或 false。',
        sample_in='3\n7\n1 2 2 3 4 4 3\n7\n1 2 2 null 3 null 3\n1\n1\n',
        sample_out='true\nfalse\ntrue\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    root = build_tree(read_vals(it, n))

    def mir(a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return mir(a.left, b.right) and mir(a.right, b.left)

    return "true" if (not root or mir(root.left, root.right)) else "false"
''',
    ),
    dict(
        num=543, title='二叉树的直径', difficulty='简单', category='二叉树', slug='diameter-of-binary-tree',
        inp=TREE_IN,
        outp='一行，最长路径的边数。',
        sample_in='2\n5\n1 2 3 4 5\n1\n1\n',
        sample_out='3\n0\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    root = build_tree(read_vals(it, n))
    best = 0

    def dep(node):
        nonlocal best
        if not node:
            return 0
        l, r = dep(node.left), dep(node.right)
        if l + r > best:
            best = l + r
        return 1 + max(l, r)

    dep(root)
    return best
''',
    ),
    dict(
        num=102, title='二叉树的层序遍历', difficulty='中等', category='二叉树', slug='binary-tree-level-order-traversal',
        inp=TREE_IN,
        outp='每层一行，层内节点值空格分隔；空树输出 EMPTY。',
        sample_in='2\n7\n3 9 20 null null 15 7\n0\n',
        sample_out='3\n9 20\n15 7\nEMPTY\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    root = build_tree(read_vals(it, n))
    if not root:
        return "EMPTY"
    rows = []
    dq = deque([root])
    while dq:
        level = []
        for _ in range(len(dq)):
            node = dq.popleft()
            level.append(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        rows.append(" ".join(map(str, level)))
    return "\n".join(rows)
''',
    ),
    dict(
        num=108, title='将有序数组转换为二叉搜索树', difficulty='简单', category='二叉树',
        slug='convert-sorted-array-to-binary-search-tree',
        inp='第一行：n；第二行：n 个升序整数。',
        outp='一行，构造出的高度平衡 BST（层序数组形式）。每次取区间中点为根，答案可能不唯一。',
        sample_in='1\n5\n-10 -3 0 5 9\n',
        sample_out='0 -10 5 null -3 null 9\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    nums = [int(next(it)) for _ in range(n)]

    def build(lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        node = TreeNode(nums[mid])
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return tree_to_str(build(0, n - 1))
''',
    ),
    dict(
        num=98, title='验证二叉搜索树', difficulty='中等', category='二叉树', slug='validate-binary-search-tree',
        inp=TREE_IN,
        outp='一行，true 或 false。',
        sample_in='3\n3\n2 1 3\n7\n5 1 4 null null 3 6\n1\n1\n',
        sample_out='true\nfalse\ntrue\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    root = build_tree(read_vals(it, n))

    def ok(node, low, high):
        if not node:
            return True
        if low is not None and node.val <= low:
            return False
        if high is not None and node.val >= high:
            return False
        return ok(node.left, low, node.val) and ok(node.right, node.val, high)

    return "true" if ok(root, None, None) else "false"
''',
    ),
    dict(
        num=230, title='二叉搜索树中第 K 小的元素', difficulty='中等', category='二叉树',
        slug='kth-smallest-element-in-a-bst',
        inp='第一行：n k；第二行：n 个 token（层序数组，含 null）。',
        outp='一行，第 k 小的元素值。',
        sample_in='2\n5 1\n3 1 4 null 2\n3 3\n2 1 3\n',
        sample_out='1\n3\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    k = int(next(it))
    root = build_tree(read_vals(it, n))
    stack = []
    cur = root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val
        cur = cur.right
    return -1
''',
    ),
    dict(
        num=199, title='二叉树的右视图', difficulty='中等', category='二叉树', slug='binary-tree-right-side-view',
        inp=TREE_IN,
        outp='一行，从上到下各层最右侧节点的值（空格分隔）；空树输出 EMPTY。',
        sample_in='2\n7\n1 2 3 null 5 null 4\n1\n1\n',
        sample_out='1 3 4\n1\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    root = build_tree(read_vals(it, n))
    if not root:
        return "EMPTY"
    res = []
    dq = deque([root])
    while dq:
        size = len(dq)
        for i in range(size):
            node = dq.popleft()
            if i == size - 1:
                res.append(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
    return " ".join(map(str, res))
''',
    ),
    dict(
        num=114, title='二叉树展开为链表', difficulty='中等', category='二叉树',
        slug='flatten-binary-tree-to-linked-list',
        inp=TREE_IN,
        outp='一行，展开后沿右指针读出的节点值（即前序序列，空格分隔）。',
        sample_in='2\n7\n1 2 5 3 4 null 6\n0\n',
        sample_out='1 2 3 4 5 6\nEMPTY\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    root = build_tree(read_vals(it, n))
    if not root:
        return "EMPTY"
    res = []
    cur = root
    while cur:
        res.append(cur.val)
        if cur.left:
            rightmost = cur.left
            while rightmost.right:
                rightmost = rightmost.right
            rightmost.right = cur.right
            cur.right = cur.left
            cur.left = None
        cur = cur.right
    return " ".join(map(str, res))
''',
    ),
    dict(
        num=105, title='从前序与中序遍历序列构造二叉树', difficulty='中等', category='二叉树',
        slug='construct-binary-tree-from-preorder-and-inorder-traversal',
        inp='第一行：n；第二行：n 个整数（前序）；第三行：n 个整数（中序）。元素互不相同。',
        outp='一行，构造出的二叉树（层序数组形式，去掉尾部 null）。',
        sample_in='1\n5\n3 9 20 15 7\n9 3 15 20 7\n',
        sample_out='3 9 20 null null 15 7\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    preorder = [int(next(it)) for _ in range(n)]
    inorder = [int(next(it)) for _ in range(n)]
    pos = {v: i for i, v in enumerate(inorder)}
    idx = [0]

    def build(lo, hi):
        if lo > hi:
            return None
        val = preorder[idx[0]]
        idx[0] += 1
        node = TreeNode(val)
        mid = pos[val]
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return tree_to_str(build(0, n - 1))
''',
    ),
    dict(
        num=437, title='路径总和 III', difficulty='中等', category='二叉树', slug='path-sum-iii',
        inp='第一行：n targetSum；第二行：n 个 token（层序数组，含 null）。',
        outp='一行，路径和等于 targetSum 的路径条数。',
        sample_in='1\n11 8\n10 5 -3 3 2 null 11 3 -2 null 1\n',
        sample_out='3\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    target = int(next(it))
    root = build_tree(read_vals(it, n))
    cnt = {0: 1}
    ans = 0

    def dfs(node, pre):
        nonlocal ans
        if not node:
            return
        pre += node.val
        ans += cnt.get(pre - target, 0)
        cnt[pre] = cnt.get(pre, 0) + 1
        dfs(node.left, pre)
        dfs(node.right, pre)
        cnt[pre] -= 1

    dfs(root, 0)
    return ans
''',
    ),
    dict(
        num=236, title='二叉树的最近公共祖先', difficulty='中等', category='二叉树',
        slug='lowest-common-ancestor-of-a-binary-tree',
        inp='第一行：n p q；第二行：n 个 token（层序数组，含 null）。p、q 为节点值，保证存在。',
        outp='一行，最近公共祖先的节点值。',
        sample_in='2\n11 5 1\n3 5 1 6 2 0 8 null null 7 4\n3 1 2\n1 2 3\n',
        sample_out='3\n1\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    p = int(next(it))
    q = int(next(it))
    root = build_tree(read_vals(it, n))

    def lca(node):
        if not node:
            return None
        if node.val == p or node.val == q:
            return node
        l = lca(node.left)
        r = lca(node.right)
        if l and r:
            return node
        return l or r

    res = lca(root)
    return res.val if res else -1
''',
    ),
    dict(
        num=124, title='二叉树中的最大路径和', difficulty='困难', category='二叉树',
        slug='binary-tree-maximum-path-sum',
        inp=TREE_IN,
        outp='一行，最大路径和。',
        sample_in='2\n7\n-10 9 20 null null 15 7\n1\n-3\n',
        sample_out='42\n-3\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    root = build_tree(read_vals(it, n))
    best = [None]

    def gain(node):
        if not node:
            return 0
        l = max(gain(node.left), 0)
        r = max(gain(node.right), 0)
        total = node.val + l + r
        if best[0] is None or total > best[0]:
            best[0] = total
        return node.val + max(l, r)

    gain(root)
    return best[0]
''',
    ),
]
