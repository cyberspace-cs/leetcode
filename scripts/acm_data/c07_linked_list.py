# -*- coding: utf-8 -*-
"""链表分类的 ACM 模式完整解题。"""

COMMON = r'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(vals):
    dummy = cur = ListNode()
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def dump(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return " ".join(map(str, out)) if out else "EMPTY"

'''

PROBLEMS = [
    dict(
        num=160, title='相交链表', difficulty='简单', category='链表', slug='intersection-of-two-linked-lists',
        inp='第一行：n；第二行：a 的 n 个整数；第三行：m；第四行：b 的 m 个整数；第五行：k。\n'
            'k 为两表公共尾部的长度（公共尾部取两表各自的末 k 个元素），k=0 表示不相交。',
        outp='一行，相交起始节点的值；不相交输出 -1。',
        sample_in='2\n5\n4 1 8 4 5\n6\n5 6 1 8 4 5\n3\n2\n1 2\n1\n3\n0\n',
        sample_out='8\n-1\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    m = int(next(it))
    b = [int(next(it)) for _ in range(m)]
    k = int(next(it))

    ha, hb = build(a), build(b)
    if 0 < k <= n and k <= m:
        na = []
        cur = ha
        while cur:
            na.append(cur)
            cur = cur.next
        tail = na[n - k]
        nb = []
        cur = hb
        while cur:
            nb.append(cur)
            cur = cur.next
        if m - k - 1 >= 0:
            nb[m - k - 1].next = tail
        else:
            hb = tail

    p, q = ha, hb
    while p is not q:
        p = p.next if p else hb
        q = q.next if q else ha
    return p.val if p else -1
''',
    ),
    dict(
        num=206, title='反转链表', difficulty='简单', category='链表', slug='reverse-linked-list',
        inp='第一行：n；第二行：n 个整数。',
        outp='一行，反转后的链表值（空格分隔）；空链表输出 EMPTY。',
        sample_in='2\n5\n1 2 3 4 5\n1\n7\n',
        sample_out='5 4 3 2 1\n7\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    head = build([int(next(it)) for _ in range(n)])
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return dump(prev)
''',
    ),
    dict(
        num=21, title='合并两个有序链表', difficulty='简单', category='链表', slug='merge-two-sorted-lists',
        inp='第一行：n；第二行：n 个整数；第三行：m；第四行：m 个整数（两链表均升序）。',
        outp='一行，合并后的升序链表值（空格分隔）。',
        sample_in='2\n3\n1 2 4\n3\n1 3 4\n1\n5\n1\n1\n',
        sample_out='1 1 2 3 4 4\n1 5\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    m = int(next(it))
    b = [int(next(it)) for _ in range(m)]
    h1, h2 = build(a), build(b)
    dummy = cur = ListNode()
    while h1 and h2:
        if h1.val <= h2.val:
            cur.next = h1
            h1 = h1.next
        else:
            cur.next = h2
            h2 = h2.next
        cur = cur.next
    cur.next = h1 or h2
    return dump(dummy.next)
''',
    ),
    dict(
        num=2, title='两数相加', difficulty='中等', category='链表', slug='add-two-numbers',
        inp='第一行：n；第二行：n 个整数（逆序存放的低位在前）；第三行：m；第四行：m 个整数。',
        outp='一行，和的链表值（同样低位在前，空格分隔）。',
        sample_in='2\n3\n2 4 3\n3\n5 6 4\n1\n0\n1\n0\n',
        sample_out='7 0 8\n0\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    m = int(next(it))
    b = [int(next(it)) for _ in range(m)]
    h1, h2 = build(a), build(b)
    dummy = cur = ListNode()
    carry = 0
    while h1 or h2 or carry:
        s = carry
        if h1:
            s += h1.val
            h1 = h1.next
        if h2:
            s += h2.val
            h2 = h2.next
        carry, d = divmod(s, 10)
        cur.next = ListNode(d)
        cur = cur.next
    return dump(dummy.next)
''',
    ),
    dict(
        num=19, title='删除链表的倒数第 N 个结点', difficulty='中等', category='链表',
        slug='remove-nth-node-from-end-of-list',
        inp='第一行：n k；第二行：n 个整数。删除倒数第 k 个节点。',
        outp='一行，删除后的链表值（空格分隔）；空链表输出 EMPTY。',
        sample_in='2\n5 2\n1 2 3 4 5\n1 1\n1\n',
        sample_out='1 2 3 5\nEMPTY\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    k = int(next(it))
    head = build([int(next(it)) for _ in range(n)])
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(k + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dump(dummy.next)
''',
    ),
    dict(
        num=24, title='两两交换链表中的节点', difficulty='中等', category='链表', slug='swap-nodes-in-pairs',
        inp='第一行：n；第二行：n 个整数。',
        outp='一行，两两交换后的链表值（空格分隔）。',
        sample_in='2\n4\n1 2 3 4\n3\n1 2 3\n',
        sample_out='2 1 4 3\n2 1 3\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    head = build([int(next(it)) for _ in range(n)])
    dummy = prev = ListNode(0, head)
    while prev.next and prev.next.next:
        a = prev.next
        b = a.next
        a.next = b.next
        b.next = a
        prev.next = b
        prev = a
    return dump(dummy.next)
''',
    ),
    dict(
        num=25, title='K 个一组翻转链表', difficulty='困难', category='链表', slug='reverse-nodes-in-k-group',
        inp='第一行：n k；第二行：n 个整数。每 k 个一组翻转，不足 k 个保持原样。',
        outp='一行，翻转后的链表值（空格分隔）。',
        sample_in='2\n5 2\n1 2 3 4 5\n5 3\n1 2 3 4 5\n',
        sample_out='2 1 4 3 5\n3 2 1 4 5\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    k = int(next(it))
    head = build([int(next(it)) for _ in range(n)])
    if k <= 1:
        return dump(head)
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
    return dump(dummy.next)
''',
    ),
    dict(
        num=138, title='随机链表的复制', difficulty='中等', category='链表', slug='copy-list-with-random-pointer',
        inp='第一行：n；随后 n 行，每行 val randIdx。randIdx 为 0-based 下标，-1 表示 null。',
        outp='第一行：n；随后 n 行，每行 val randIdx，为深拷贝后的链表。',
        sample_in='1\n5\n7 -1\n13 0\n11 4\n10 2\n1 0\n',
        sample_out='5\n7 -1\n13 0\n11 4\n10 2\n1 0\n',
        code=r'''
class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def solve(it):
    n = int(next(it))
    vals = []
    rnd = []
    for _ in range(n):
        vals.append(int(next(it)))
        rnd.append(int(next(it)))

    nodes = [Node(v) for v in vals]
    for i in range(n - 1):
        nodes[i].next = nodes[i + 1]
    for i in range(n):
        nodes[i].random = nodes[rnd[i]] if rnd[i] >= 0 else None

    mp = {nd: Node(nd.val) for nd in nodes}
    for nd in nodes:
        cp = mp[nd]
        cp.next = mp[nd.next] if nd.next else None
        cp.random = mp[nd.random] if nd.random else None

    idx = {mp[nodes[i]]: i for i in range(n)}
    rows = []
    cur = mp[nodes[0]] if n else None
    while cur:
        rows.append("%d %d" % (cur.val, idx[cur.random] if cur.random else -1))
        cur = cur.next
    return "\n".join([str(len(rows))] + rows)
''',
    ),
    dict(
        num=148, title='排序链表', difficulty='中等', category='链表', slug='sort-list',
        inp='第一行：n；第二行：n 个整数。',
        outp='一行，升序排序后的链表值（空格分隔）。',
        sample_in='2\n4\n4 2 1 3\n5\n-1 5 3 4 0\n',
        sample_out='1 2 3 4\n-1 0 3 4 5\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    head = build([int(next(it)) for _ in range(n)])

    def merge_sort(h):
        if not h or not h.next:
            return h
        slow, fast = h, h.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        l, r = merge_sort(h), merge_sort(mid)
        dummy = cur = ListNode()
        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next

    return dump(merge_sort(head))
''',
    ),
    dict(
        num=23, title='合并 K 个升序链表', difficulty='困难', category='链表', slug='merge-k-sorted-lists',
        inp='第一行：k；随后 k 组，每组第一行为该链表长度 len，第二行为 len 个升序整数。',
        outp='一行，合并后的升序链表值（空格分隔）；全空输出 EMPTY。',
        sample_in='1\n3\n3\n1 4 5\n3\n1 3 4\n2\n2 6\n',
        sample_out='1 1 2 3 4 4 5 6\n',
        code=r'''
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(vals):
    dummy = cur = ListNode()
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def solve(it):
    k = int(next(it))
    heap = []
    for i in range(k):
        L = int(next(it))
        head = build([int(next(it)) for _ in range(L)])
        if head:
            heapq.heappush(heap, (head.val, i, head))
    dummy = cur = ListNode()
    while heap:
        v, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    out = []
    head = dummy.next
    while head:
        out.append(head.val)
        head = head.next
    return " ".join(map(str, out)) if out else "EMPTY"
''',
    ),
    dict(
        num=234, title='回文链表', difficulty='简单', category='链表', slug='palindrome-linked-list',
        inp='第一行：n；第二行：n 个整数。',
        outp='一行，true 或 false。',
        sample_in='3\n4\n1 2 2 1\n2\n1 2\n1\n1\n',
        sample_out='true\nfalse\ntrue\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    head = build([int(next(it)) for _ in range(n)])
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    p, q = head, prev
    while q:
        if p.val != q.val:
            return "false"
        p = p.next
        q = q.next
    return "true"
''',
    ),
    dict(
        num=141, title='环形链表', difficulty='简单', category='链表', slug='linked-list-cycle',
        inp='第一行：n；第二行：n 个整数；第三行：pos。pos 为入环位置（0-based），-1 表示无环。',
        outp='一行，true 或 false。',
        sample_in='2\n4\n3 2 0 -4\n1\n3\n1 2 3\n-1\n',
        sample_out='true\nfalse\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    vals = [int(next(it)) for _ in range(n)]
    pos = int(next(it))
    head = build(vals)
    if pos >= 0 and n:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        nodes[-1].next = nodes[pos]
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return "true"
    return "false"
''',
    ),
    dict(
        num=142, title='环形链表 II', difficulty='中等', category='链表', slug='linked-list-cycle-ii',
        inp='第一行：n；第二行：n 个整数；第三行：pos。pos 为入环位置（0-based），-1 表示无环。',
        outp='一行，入环第一个节点的值；无环输出 -1。',
        sample_in='2\n4\n3 2 0 -4\n1\n3\n1 2 3\n-1\n',
        sample_out='2\n-1\n',
        code=COMMON + r'''
def solve(it):
    n = int(next(it))
    vals = [int(next(it)) for _ in range(n)]
    pos = int(next(it))
    head = build(vals)
    if pos >= 0 and n:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        nodes[-1].next = nodes[pos]
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            p = head
            while p is not slow:
                p = p.next
                slow = slow.next
            return p.val
    return -1
''',
    ),
    dict(
        num=146, title='LRU 缓存', difficulty='中等', category='链表', slug='lru-cache',
        inp='第一行：capacity q；随后 q 行，每行为 "get key" 或 "put key value"。',
        outp='一行，按顺序输出所有 get 的结果（空格分隔）；若没有 get 操作输出 EMPTY。\n'
             '为便于按行对齐，本题固定在每组输出恰好一行。',
        sample_in='2\n2 5\nget 1\nput 1 1\nput 2 2\nget 1\nput 3 3\n1 3\nput 1 1\nget 1\nget 2\n',
        sample_out='-1 1\n1 -1\n',
        code=r'''
def solve(it):
    cap = int(next(it))
    q = int(next(it))
    od = {}
    out = []
    for _ in range(q):
        op = next(it)
        if op == "get":
            k = int(next(it))
            if k in od:
                v = od.pop(k)
                od[k] = v
                out.append(str(v))
            else:
                out.append("-1")
        else:
            k = int(next(it))
            v = int(next(it))
            if k in od:
                od.pop(k)
            od[k] = v
            if len(od) > cap:
                od.pop(next(iter(od)))
    return " ".join(out) if out else "EMPTY"
''',
    ),
]
