# -*- coding: utf-8 -*-
"""二叉树分类 · 个人模板风格（单组输入）。"""

TREE_PRELUDE = '''from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals):
    """按层序数组（LeetCode 形式，None 表示空）构造二叉树。"""
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


def tree_to_vals(root):
    """按层序输出为数组（去掉尾部 None），与 build_tree 互逆。"""
    if not root:
        return []
    out = []
    dq = deque([root])
    while dq:
        node = dq.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        dq.append(node.left)
        dq.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def right_chain_vals(root):
    """沿右指针读出节点值（用于「展开为链表」的输出）。"""
    vals = []
    cur = root
    while cur:
        vals.append(cur.val)
        cur = cur.right
    return vals'''

TREE_IN = '一行：层序数组（LeetCode 形式，空节点写 None），如 [3,9,20,None,None,15,7]。'

PROBLEMS = [
    dict(
        num=94, func='inorder_traversal', params=[('root', 'TreeNode')], ret='List[int]',
        prelude=TREE_PRELUDE,
        body='''    # 在这里写你的代码（迭代写法）
    res = []
    stack, cur = [], root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res''',
        main='''    nums = eval(input())
    print(inorder_traversal(build_tree(nums)))''',
        inp=TREE_IN,
        sample_in='[1,None,2,3]\n',
        sample_out='[1, 3, 2]\n',
    ),
    dict(
        num=104, func='max_depth', params=[('root', 'TreeNode')], ret='int',
        prelude=TREE_PRELUDE,
        body='''    # 在这里写你的代码
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))''',
        main='''    nums = eval(input())
    print(max_depth(build_tree(nums)))''',
        inp=TREE_IN,
        sample_in='[3,9,20,None,None,15,7]\n',
        sample_out='3\n',
    ),
    dict(
        num=226, func='invert_tree', params=[('root', 'TreeNode')], ret='TreeNode',
        prelude=TREE_PRELUDE,
        body='''    # 在这里写你的代码
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root''',
        main='''    nums = eval(input())
    print(tree_to_vals(invert_tree(build_tree(nums))))''',
        inp=TREE_IN,
        sample_in='[4,2,7,1,3,6,9]\n',
        sample_out='[4, 7, 2, 9, 6, 3, 1]\n',
    ),
    dict(
        num=101, func='is_symmetric', params=[('root', 'TreeNode')], ret='bool',
        prelude=TREE_PRELUDE,
        body='''    # 在这里写你的代码
    def mirror(a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return mirror(a.left, b.right) and mirror(a.right, b.left)

    return not root or mirror(root.left, root.right)''',
        main='''    nums = eval(input())
    print(is_symmetric(build_tree(nums)))''',
        inp=TREE_IN,
        sample_in='[1,2,2,3,4,4,3]\n',
        sample_out='True\n',
    ),
    dict(
        num=543, func='diameter_of_binary_tree', params=[('root', 'TreeNode')], ret='int',
        prelude=TREE_PRELUDE,
        body='''    # 在这里写你的代码
    best = 0

    def depth(node):
        nonlocal best
        if not node:
            return 0
        l = depth(node.left)
        r = depth(node.right)
        best = max(best, l + r)
        return 1 + max(l, r)

    depth(root)
    return best''',
        main='''    nums = eval(input())
    print(diameter_of_binary_tree(build_tree(nums)))''',
        inp=TREE_IN,
        sample_in='[1,2,3,4,5]\n',
        sample_out='3\n',
    ),
    dict(
        num=102, func='level_order', params=[('root', 'TreeNode')], ret='List[List[int]]',
        prelude=TREE_PRELUDE,
        body='''    # 在这里写你的代码
    if not root:
        return []
    res = []
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
        res.append(level)
    return res''',
        main='''    nums = eval(input())
    print(level_order(build_tree(nums)))''',
        inp=TREE_IN,
        sample_in='[3,9,20,None,None,15,7]\n',
        sample_out='[[3], [9, 20], [15, 7]]\n',
    ),
    dict(
        num=108, func='sorted_array_to_bst', params=[('nums', 'List[int]')], ret='TreeNode',
        prelude=TREE_PRELUDE,
        body='''    # 在这里写你的代码（每次取区间中点为根）
    def build(lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        node = TreeNode(nums[mid])
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return build(0, len(nums) - 1)''',
        main='''    nums = eval(input())
    print(tree_to_vals(sorted_array_to_bst(nums)))''',
        inp='一行：升序整数列表，如 [-10,-3,0,5,9]。',
        sample_in='[-10,-3,0,5,9]\n',
        sample_out='[0, -10, 5, None, -3, None, 9]\n',
    ),
    dict(
        num=98, func='is_valid_bst', params=[('root', 'TreeNode')], ret='bool',
        prelude=TREE_PRELUDE,
        body='''    # 在这里写你的代码（递归传上下界）
    def check(node, low, high):
        if not node:
            return True
        if low is not None and node.val <= low:
            return False
        if high is not None and node.val >= high:
            return False
        return check(node.left, low, node.val) and check(node.right, node.val, high)

    return check(root, None, None)''',
        main='''    nums = eval(input())
    print(is_valid_bst(build_tree(nums)))''',
        inp=TREE_IN,
        sample_in='[2,1,3]\n',
        sample_out='True\n',
    ),
    dict(
        num=230, func='kth_smallest', params=[('root', 'TreeNode'), ('k', 'int')], ret='int',
        prelude=TREE_PRELUDE,
        body='''    # 在这里写你的代码（中序遍历计数）
    stack, cur = [], root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val
        cur = cur.right
    return -1''',
        main='''    nums = eval(input())
    k = int(input())
    print(kth_smallest(build_tree(nums), k))''',
        inp='第一行：层序数组；第二行：k。',
        sample_in='[3,1,4,None,2]\n1\n',
        sample_out='1\n',
    ),
    dict(
        num=199, func='right_side_view', params=[('root', 'TreeNode')], ret='List[int]',
        prelude=TREE_PRELUDE,
        body='''    # 在这里写你的代码
    if not root:
        return []
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
    return res''',
        main='''    nums = eval(input())
    print(right_side_view(build_tree(nums)))''',
        inp=TREE_IN,
        sample_in='[1,2,3,None,5,None,4]\n',
        sample_out='[1, 3, 4]\n',
    ),
    dict(
        num=114, func='flatten', params=[('root', 'TreeNode')], ret='None',
        prelude=TREE_PRELUDE,
        body='''    # 在这里写你的代码（原地展开为只有右子节点的单链表）
    cur = root
    while cur:
        if cur.left:
            rightmost = cur.left
            while rightmost.right:
                rightmost = rightmost.right
            rightmost.right = cur.right
            cur.right = cur.left
            cur.left = None
        cur = cur.right''',
        main='''    nums = eval(input())
    root = build_tree(nums)
    flatten(root)
    print(right_chain_vals(root))''',
        inp=TREE_IN,
        sample_in='[1,2,5,3,4,None,6]\n',
        sample_out='[1, 2, 3, 4, 5, 6]\n',
    ),
    dict(
        num=105, func='build_tree_from_pre_in',
        params=[('preorder', 'List[int]'), ('inorder', 'List[int]')], ret='TreeNode',
        prelude=TREE_PRELUDE,
        body='''    # 在这里写你的代码
    pos = {v: i for i, v in enumerate(inorder)}
    idx = 0

    def build(lo, hi):
        nonlocal idx
        if lo > hi:
            return None
        val = preorder[idx]
        idx += 1
        node = TreeNode(val)
        mid = pos[val]
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return build(0, len(preorder) - 1)''',
        main='''    preorder = eval(input())
    inorder = eval(input())
    print(tree_to_vals(build_tree_from_pre_in(preorder, inorder)))''',
        inp='第一行：前序遍历列表；第二行：中序遍历列表（元素互不相同）。',
        sample_in='[3,9,20,15,7]\n[9,3,15,20,7]\n',
        sample_out='[3, 9, 20, None, None, 15, 7]\n',
    ),
    dict(
        num=437, func='path_sum', params=[('root', 'TreeNode'), ('target_sum', 'int')], ret='int',
        prelude=TREE_PRELUDE,
        body='''    # 在这里写你的代码（前缀和 + 回溯）
    count = {0: 1}
    res = 0

    def dfs(node, prefix):
        nonlocal res
        if not node:
            return
        prefix += node.val
        res += count.get(prefix - target_sum, 0)
        count[prefix] = count.get(prefix, 0) + 1
        dfs(node.left, prefix)
        dfs(node.right, prefix)
        count[prefix] -= 1

    dfs(root, 0)
    return res''',
        main='''    nums = eval(input())
    target_sum = int(input())
    print(path_sum(build_tree(nums), target_sum))''',
        inp='第一行：层序数组；第二行：targetSum。',
        sample_in='[10,5,-3,3,2,None,11,3,-2,None,1]\n8\n',
        sample_out='3\n',
    ),
    dict(
        num=236, func='lowest_common_ancestor',
        params=[('root', 'TreeNode'), ('p', 'int'), ('q', 'int')], ret='TreeNode',
        prelude=TREE_PRELUDE,
        body='''    # 在这里写你的代码（p、q 用节点值表示，保证存在且互不相同）
    def lca(node):
        if not node:
            return None
        if node.val == p or node.val == q:
            return node
        left = lca(node.left)
        right = lca(node.right)
        if left and right:
            return node
        return left or right

    return lca(root)''',
        main='''    nums = eval(input())
    p = int(input())
    q = int(input())
    node = lowest_common_ancestor(build_tree(nums), p, q)
    print(node.val if node else -1)''',
        inp='第一行：层序数组；第二行：p（节点值）；第三行：q（节点值）。',
        sample_in='[3,5,1,6,2,0,8,None,None,7,4]\n5\n1\n',
        sample_out='3\n',
    ),
    dict(
        num=124, func='max_path_sum', params=[('root', 'TreeNode')], ret='int',
        prelude=TREE_PRELUDE,
        body='''    # 在这里写你的代码
    best = [None]

    def gain(node):
        if not node:
            return 0
        left = max(gain(node.left), 0)
        right = max(gain(node.right), 0)
        total = node.val + left + right
        if best[0] is None or total > best[0]:
            best[0] = total
        return node.val + max(left, right)

    gain(root)
    return best[0]''',
        main='''    nums = eval(input())
    print(max_path_sum(build_tree(nums)))''',
        inp=TREE_IN,
        sample_in='[-10,9,20,None,None,15,7]\n',
        sample_out='42\n',
    ),
]
