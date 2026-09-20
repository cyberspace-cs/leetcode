# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 208    标题: 实现 Trie (前缀树)    难度: 中等    分类: 图论
# 链接: https://leetcode.cn/problems/implement-trie-prefix-tree/
# 运行: python3 "0208-实现 Trie (前缀树).py"   （按提示输入，或重定向样例输入）

class Trie:
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
        return self._walk(prefix) is not None


def main():
    ops = eval(input())
    trie = Trie()
    out = []
    for op, word in ops:
        if op == "insert":
            trie.insert(word)
        elif op == "search":
            out.append(trie.search(word))
        else:
            out.append(trie.starts_with(word))
    print(out)


if __name__ == "__main__":
    main()


# 208. 实现 Trie (前缀树)  中等
#
# 【题目描述】
# 实现前缀树 Trie，支持插入单词、查询完整单词、查询是否存在指定前缀。
#
# 【示例】
# insert("apple"), search("apple") → true, search("app") → false, startsWith("app") → true
#
# 【思路提示】
# 每个节点用 dict / 定长数组保存子节点，并用布尔标记是否为单词结尾。
#
# 【输入格式】
# 一行：操作列表，如 [["insert","apple"],["search","apple"],["startsWith","app"]]。
#
# 【样例输入】
# [["insert","apple"],["search","apple"],["search","app"],["startsWith","app"],["insert","app"],["search","app"]]
# 【样例输出】
# [True, False, True, True]
