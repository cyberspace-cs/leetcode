# -*- coding: utf-8 -*-
"""链表分类 · 个人模板风格（单组输入）。"""

LL_PRELUDE = '''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(nums):
    dummy = ListNode()
    cur = dummy
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


def list_to_vals(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals'''

CYCLE_PRELUDE = LL_PRELUDE + '''


def make_cycle(head, pos):
    """把链表的末节点指向下标 pos 处，构造环形链表；pos < 0 表示不构造。"""
    if pos < 0 or not head:
        return head
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    nodes[-1].next = nodes[pos]
    return head'''

INTERSECT_PRELUDE = LL_PRELUDE + '''


def build_intersect(a_vals, b_vals, k):
    """构造相交链表：两表末尾 k 个节点共享；k <= 0 表示不相交。返回 (headA, headB)。"""
    if k <= 0 or k > len(a_vals) or k > len(b_vals):
        return build_list(a_vals), build_list(b_vals)
    common = build_list(a_vals[len(a_vals) - k:])
    headA = build_list(a_vals[:len(a_vals) - k])
    headB = build_list(b_vals[:len(b_vals) - k])
    for head in (headA, headB):
        if head:
            cur = head
            while cur.next:
                cur = cur.next
            cur.next = common
    return (headA or common), (headB or common)'''

RANDOM_PRELUDE = '''class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def build_random_list(pairs):
    """pairs 形如 [[val, randIdx], ...]，randIdx 为 0-based 下标，-1 表示 None。"""
    nodes = [Node(v) for v, _ in pairs]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, (_, r) in enumerate(pairs):
        nodes[i].random = nodes[r] if r >= 0 else None
    return nodes[0] if nodes else None'''

PROBLEMS = [
    dict(
        num=160, func='get_intersection_node',
        params=[('headA', 'ListNode'), ('headB', 'ListNode')], ret='ListNode',
        prelude=INTERSECT_PRELUDE,
        body='''    # 在这里写你的代码
    p, q = headA, headB
    while p is not q:
        p = p.next if p else headB
        q = q.next if q else headA
    return p''',
        main='''    a = eval(input())
    b = eval(input())
    k = int(input())
    headA, headB = build_intersect(a, b, k)
    node = get_intersection_node(headA, headB)
    print(node.val if node else -1)''',
        inp='第一行：链表 a 的列表；第二行：链表 b 的列表；第三行：k（公共尾部长度，0 表示不相交）。',
        sample_in='[4,1,8,4,5]\n[5,6,1,8,4,5]\n3\n',
        sample_out='8\n',
    ),
    dict(
        num=206, func='reverse_list', params=[('head', 'ListNode')], ret='ListNode',
        prelude=LL_PRELUDE,
        body='''    # 在这里写你的代码
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev''',
        main='''    nums = eval(input())
    head = build_list(nums)
    print(list_to_vals(reverse_list(head)))''',
        inp='一行：链表元素列表，如 [1,2,3,4,5]。',
        sample_in='[1,2,3,4,5]\n',
        sample_out='[5, 4, 3, 2, 1]\n',
    ),
    dict(
        num=21, func='merge_two_lists',
        params=[('list1', 'ListNode'), ('list2', 'ListNode')], ret='ListNode',
        prelude=LL_PRELUDE,
        body='''    # 在这里写你的代码
    dummy = cur = ListNode()
    while list1 and list2:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    cur.next = list1 or list2
    return dummy.next''',
        main='''    a = eval(input())
    b = eval(input())
    head = merge_two_lists(build_list(a), build_list(b))
    print(list_to_vals(head))''',
        inp='第一行：链表1（升序）；第二行：链表2（升序）。',
        sample_in='[1,2,4]\n[1,3,4]\n',
        sample_out='[1, 1, 2, 3, 4, 4]\n',
    ),
    dict(
        num=2, func='add_two_numbers',
        params=[('l1', 'ListNode'), ('l2', 'ListNode')], ret='ListNode',
        prelude=LL_PRELUDE,
        body='''    # 在这里写你的代码（数字逆序存放，进位相加）
    dummy = cur = ListNode()
    carry = 0
    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        carry, digit = divmod(total, 10)
        cur.next = ListNode(digit)
        cur = cur.next
    return dummy.next''',
        main='''    a = eval(input())
    b = eval(input())
    head = add_two_numbers(build_list(a), build_list(b))
    print(list_to_vals(head))''',
        inp='第一行：链表1（低位在前）；第二行：链表2（低位在前）。',
        sample_in='[2,4,3]\n[5,6,4]\n',
        sample_out='[7, 0, 8]\n',
    ),
    dict(
        num=19, func='remove_nth_from_end',
        params=[('head', 'ListNode'), ('n', 'int')], ret='ListNode',
        prelude=LL_PRELUDE,
        body='''    # 在这里写你的代码
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next''',
        main='''    nums = eval(input())
    n = int(input())
    head = remove_nth_from_end(build_list(nums), n)
    print(list_to_vals(head))''',
        inp='第一行：链表元素列表；第二行：n（删除倒数第 n 个节点）。',
        sample_in='[1,2,3,4,5]\n2\n',
        sample_out='[1, 2, 3, 5]\n',
    ),
    dict(
        num=24, func='swap_pairs', params=[('head', 'ListNode')], ret='ListNode',
        prelude=LL_PRELUDE,
        body='''    # 在这里写你的代码
    dummy = prev = ListNode(0, head)
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return dummy.next''',
        main='''    nums = eval(input())
    head = swap_pairs(build_list(nums))
    print(list_to_vals(head))''',
        inp='一行：链表元素列表，如 [1,2,3,4]。',
        sample_in='[1,2,3,4]\n',
        sample_out='[2, 1, 4, 3]\n',
    ),
    dict(
        num=25, func='reverse_k_group',
        params=[('head', 'ListNode'), ('k', 'int')], ret='ListNode',
        prelude=LL_PRELUDE,
        body='''    # 在这里写你的代码
    if k <= 1:
        return head
    dummy = ListNode(0, head)
    group_prev = dummy
    while True:
        kth = group_prev
        ok = True
        for _ in range(k):
            kth = kth.next
            if not kth:
                ok = False
                break
        if not ok:
            break
        group_next = kth.next
        prev, cur = group_next, group_prev.next
        while cur is not group_next:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        start = group_prev.next
        group_prev.next = kth
        group_prev = start
    return dummy.next''',
        main='''    nums = eval(input())
    k = int(input())
    head = reverse_k_group(build_list(nums), k)
    print(list_to_vals(head))''',
        inp='第一行：链表元素列表；第二行：k。不足 k 个的尾部保持原样。',
        sample_in='[1,2,3,4,5]\n2\n',
        sample_out='[2, 1, 4, 3, 5]\n',
    ),
    dict(
        num=138, func='copy_random_list', params=[('head', 'Node')], ret='Node',
        prelude=RANDOM_PRELUDE,
        body='''    # 在这里写你的代码
    if not head:
        return None
    # 第一遍：哈希表建立 原节点 -> 新节点
    mapping = {}
    cur = head
    while cur:
        mapping[cur] = Node(cur.val)
        cur = cur.next
    # 第二遍：连接 next 与 random
    cur = head
    while cur:
        mapping[cur].next = mapping[cur.next] if cur.next else None
        mapping[cur].random = mapping[cur.random] if cur.random else None
        cur = cur.next
    return mapping[head]''',
        main='''    pairs = eval(input())
    head = build_random_list(pairs)
    copy = copy_random_list(head)
    # 建立「拷贝节点 -> 下标」映射，用于输出 random 指向
    copy_index = {}
    cur = copy
    i = 0
    while cur:
        copy_index[cur] = i
        cur = cur.next
        i += 1
    out = []
    cur = copy
    while cur:
        out.append((cur.val, copy_index[cur.random] if cur.random else -1))
        cur = cur.next
    print(out)''',
        inp='一行：[[val, randIdx], ...]，randIdx 为 0-based 下标，-1 表示 None。',
        sample_in='[[7,-1],[13,0],[11,4],[10,2],[1,0]]\n',
        sample_out='[(7, -1), (13, 0), (11, 4), (10, 2), (1, 0)]\n',
    ),
    dict(
        num=148, func='sort_list', params=[('head', 'ListNode')], ret='ListNode',
        prelude=LL_PRELUDE,
        body='''    # 在这里写你的代码（归并排序）
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = sort_list(head)
    right = sort_list(mid)
    dummy = cur = ListNode()
    while left and right:
        if left.val <= right.val:
            cur.next = left
            left = left.next
        else:
            cur.next = right
            right = right.next
        cur = cur.next
    cur.next = left or right
    return dummy.next''',
        main='''    nums = eval(input())
    head = sort_list(build_list(nums))
    print(list_to_vals(head))''',
        inp='一行：链表元素列表，如 [4,2,1,3]。',
        sample_in='[4,2,1,3]\n',
        sample_out='[1, 2, 3, 4]\n',
    ),
    dict(
        num=23, func='merge_k_lists',
        params=[('lists', 'List[ListNode]')], ret='ListNode',
        prelude=LL_PRELUDE,
        body='''    # 在这里写你的代码（分治两两合并）
    if not lists:
        return None
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            a = lists[i]
            b = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(_merge_two(a, b))
        lists = merged
    return lists[0]''',
        main='''    groups = eval(input())
    lists = [build_list(g) for g in groups]
    head = merge_k_lists(lists)
    print(list_to_vals(head))''',
        inp='一行：二维列表，每个子列表为一条升序链表，如 [[1,4,5],[1,3,4],[2,6]]。',
        sample_in='[[1,4,5],[1,3,4],[2,6]]\n',
        sample_out='[1, 1, 2, 3, 4, 4, 5, 6]\n',
    ),
    dict(
        num=234, func='is_palindrome', params=[('head', 'ListNode')], ret='bool',
        prelude=LL_PRELUDE,
        body='''    # 在这里写你的代码
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # 反转后半部分
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    p, q = head, prev
    while q:
        if p.val != q.val:
            return False
        p = p.next
        q = q.next
    return True''',
        main='''    nums = eval(input())
    print(is_palindrome(build_list(nums)))''',
        inp='一行：链表元素列表，如 [1,2,2,1]。',
        sample_in='[1,2,2,1]\n',
        sample_out='True\n',
    ),
    dict(
        num=141, func='has_cycle', params=[('head', 'ListNode')], ret='bool',
        prelude=CYCLE_PRELUDE,
        body='''    # 在这里写你的代码
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False''',
        main='''    nums = eval(input())
    pos = int(input())
    head = make_cycle(build_list(nums), pos)
    print(has_cycle(head))''',
        inp='第一行：链表元素列表；第二行：pos（入环位置 0-based，-1 表示无环）。',
        sample_in='[3,2,0,-4]\n1\n',
        sample_out='True\n',
    ),
    dict(
        num=142, func='detect_cycle', params=[('head', 'ListNode')], ret='ListNode',
        prelude=CYCLE_PRELUDE,
        body='''    # 在这里写你的代码
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            p = head
            while p is not slow:
                p = p.next
                slow = slow.next
            return p
    return None''',
        main='''    nums = eval(input())
    pos = int(input())
    head = make_cycle(build_list(nums), pos)
    node = detect_cycle(head)
    print(node.val if node else -1)''',
        inp='第一行：链表元素列表；第二行：pos（入环位置 0-based，-1 表示无环）。',
        sample_in='[3,2,0,-4]\n1\n',
        sample_out='2\n',
    ),
    dict(
        num=146, func=None, params=[], ret='None',
        code='''class LRUCache:
    """
    :rtype: None
    """

    def __init__(self, capacity: int):
        # 在这里写你的代码
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        # 在这里写你的代码
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        # 在这里写你的代码
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.pop(next(iter(self.cache)))''',
        main='''    capacity = int(input())
    ops = eval(input())
    lru = LRUCache(capacity)
    out = []
    for op in ops:
        if op[0] == "put":
            lru.put(op[1], op[2])
        else:
            out.append(lru.get(op[1]))
    print(out)''',
        inp='第一行：capacity；第二行：操作列表，如 [["put",1,1],["get",1]]。',
        sample_in='2\n[["put",1,1],["put",2,2],["get",1],["put",3,3],["get",2]]\n',
        sample_out='[1, -1]\n',
    ),
]

# 供 merge_k_lists 使用的内部合并函数，随 prelude 一同注入
PROBLEMS[9]['prelude'] = LL_PRELUDE + '''


def _merge_two(a, b):
    dummy = cur = ListNode()
    while a and b:
        if a.val <= b.val:
            cur.next = a
            a = a.next
        else:
            cur.next = b
            b = b.next
        cur = cur.next
    cur.next = a or b
    return dummy.next'''
