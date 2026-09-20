# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 347    标题: 前 K 个高频元素    难度: 中等    分类: 堆
# 链接: https://leetcode.cn/problems/top-k-frequent-elements/
# 运行: python3 "0347-前 K 个高频元素.py"   （按提示输入，或重定向样例输入）

def top_k_frequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # 在这里写你的代码（计数 + 排序 / 堆）
    count = {}
    for x in nums:
        count[x] = count.get(x, 0) + 1
    items = sorted(count.items(), key=lambda kv: (-kv[1], kv[0]))
    return [v for v, _ in items[:k]]


def main():
    nums = eval(input())
    k = int(input())
    print(top_k_frequent(nums, k))


if __name__ == "__main__":
    main()


# 347. 前 K 个高频元素  中等
#
# 【题目描述】
# 返回数组中出现频率最高的 k 个元素，顺序不限。
#
# 【示例】
# nums = [1,1,1,2,2,3], k = 2  →  [1,2]
#
# 【思路提示】
# 先用哈希计数，再用小顶堆或桶排序取前 k 个。
#
# 【输入格式】
# 第一行：整数列表；第二行：k。
#
# 【样例输入】
# [1,1,1,2,2,3]
# 2
# 【样例输出】
# [1, 2]
