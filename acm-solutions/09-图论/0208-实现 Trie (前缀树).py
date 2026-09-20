# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · ACM 模式完整解题
================================================================
题号 : 208
标题 : 实现 Trie (前缀树)
难度 : 中等
分类 : 图论
链接 : https://leetcode.cn/problems/implement-trie-prefix-tree/
================================================================

【输入格式】
第 1 行：T，表示测试数据组数。以下共 T 组，每组格式如下：
第一行：q；随后 q 行，每行为 insert word / search word / startsWith prefix。

【输出格式】
一行，按顺序输出所有 search 与 startsWith 的结果（true/false，空格分隔）；若无查询输出 EMPTY。

【样例输入】
1
8
insert apple
search apple
search app
startsWith app
insert app
search app
startsWith app
search banana

【样例输出】
true false true true true false

"""

import sys


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

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        out.append(str(solve(it)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
