# -*- coding: utf-8 -*-
"""堆分类 · 个人模板风格（单组输入）。"""

PROBLEMS = [
    dict(
        num=215, func='find_kth_largest',
        params=[('nums', 'List[int]'), ('k', 'int')], ret='int',
        body='''    # 在这里写你的代码（大小为 k 的小顶堆）
    import heapq
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]''',
        main='''    nums = eval(input())
    k = int(input())
    print(find_kth_largest(nums, k))''',
        inp='第一行：整数列表；第二行：k。',
        sample_in='[3,2,1,5,6,4]\n2\n',
        sample_out='5\n',
    ),
    dict(
        num=347, func='top_k_frequent',
        params=[('nums', 'List[int]'), ('k', 'int')], ret='List[int]',
        body='''    # 在这里写你的代码（计数 + 排序 / 堆）
    count = {}
    for x in nums:
        count[x] = count.get(x, 0) + 1
    items = sorted(count.items(), key=lambda kv: (-kv[1], kv[0]))
    return [v for v, _ in items[:k]]''',
        main='''    nums = eval(input())
    k = int(input())
    print(top_k_frequent(nums, k))''',
        inp='第一行：整数列表；第二行：k。',
        sample_in='[1,1,1,2,2,3]\n2\n',
        sample_out='[1, 2]\n',
    ),
    dict(
        num=295, func=None, params=[], ret='None',
        code='''class MedianFinder:
    """
    :rtype: None
    """

    def __init__(self):
        # 在这里写你的代码（对顶堆：大顶堆存较小一半，小顶堆存较大一半）
        import heapq
        self.heapq = heapq
        self.small = []
        self.large = []

    def add_num(self, num: int) -> None:
        # 在这里写你的代码
        self.heapq.heappush(self.small, -num)
        self.heapq.heappush(self.large, -self.heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            self.heapq.heappush(self.small, -self.heapq.heappop(self.large))

    def find_median(self) -> float:
        # 在这里写你的代码
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0''',
        main='''    ops = eval(input())
    mf = MedianFinder()
    out = []
    for op in ops:
        if op[0] == "addNum":
            mf.add_num(op[1])
        else:
            out.append(mf.find_median())
    print(out)''',
        inp='一行：操作列表，如 [["addNum",1],["addNum",2],["findMedian"]]。',
        sample_in='[["addNum",1],["addNum",2],["findMedian"],["addNum",3],["findMedian"]]\n',
        sample_out='[1.5, 2.0]\n',
    ),
]
