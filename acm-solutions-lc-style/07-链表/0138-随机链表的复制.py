# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 138    标题: 随机链表的复制    难度: 中等    分类: 链表
# 链接: https://leetcode.cn/problems/copy-list-with-random-pointer/
# 运行: python3 "0138-随机链表的复制.py"   （按提示输入，或重定向样例输入）

class Node:
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
    return nodes[0] if nodes else None


def copy_random_list(head):
    """
    :type head: Node
    :rtype: Node
    """
    # 在这里写你的代码
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
    return mapping[head]


def main():
    pairs = eval(input())
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
    print(out)


if __name__ == "__main__":
    main()


# 138. 随机链表的复制  中等
#
# 【题目描述】
# 复制一个带有 random 随机指针的链表，返回其深拷贝。
#
# 【示例】
# head = [[7,null],[13,0],[11,4],[10,2],[1,0]]  →  深拷贝后的等值链表
#
# 【思路提示】
# 哈希表映射「原节点 → 新节点」；也可用拼接-拆分的 O(1) 空间做法。
#
# 【输入格式】
# 一行：[[val, randIdx], ...]，randIdx 为 0-based 下标，-1 表示 None。
#
# 【样例输入】
# [[7,-1],[13,0],[11,4],[10,2],[1,0]]
# 【样例输出】
# [(7, -1), (13, 0), (11, 4), (10, 2), (1, 0)]
