# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 146    标题: LRU 缓存    难度: 中等    分类: 链表
# 链接: https://leetcode.cn/problems/lru-cache/
# 运行: python3 "0146-LRU 缓存.py"   （按提示输入，或重定向样例输入）

class LRUCache:
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
            self.cache.pop(next(iter(self.cache)))


def main():
    capacity = int(input())
    ops = eval(input())
    lru = LRUCache(capacity)
    out = []
    for op in ops:
        if op[0] == "put":
            lru.put(op[1], op[2])
        else:
            out.append(lru.get(op[1]))
    print(out)


if __name__ == "__main__":
    main()


# 146. LRU 缓存  中等
#
# 【题目描述】
# 设计 LRU（最近最少使用）缓存，支持 get 和 put，且两个操作都要求 O(1) 平均时间复杂度。
#
# 【示例】
# capacity = 2: put(1,1), put(2,2), get(1) → 1, put(3,3), get(2) → -1
#
# 【思路提示】
# 哈希表 + 双向链表（Python 中也可直接用 collections.OrderedDict）。
#
# 【输入格式】
# 第一行：capacity；第二行：操作列表，如 [["put",1,1],["get",1]]。
#
# 【样例输入】
# 2
# [["put",1,1],["put",2,2],["get",1],["put",3,3],["get",2]]
# 【样例输出】
# [1, -1]
