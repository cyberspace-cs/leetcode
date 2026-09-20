# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 560    标题: 和为 K 的子数组    难度: 中等    分类: 子串
# 链接: https://leetcode.cn/problems/subarray-sum-equals-k/
# 运行: python3 "0560-和为 K 的子数组.py"   （按提示输入，或重定向样例输入）

def subarray_sum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # 在这里写你的代码
    count = {0: 1}
    prefix = 0
    res = 0
    for x in nums:
        prefix += x
        res += count.get(prefix - k, 0)
        count[prefix] = count.get(prefix, 0) + 1
    return res


def main():
    nums = eval(input())
    k = int(input())
    print(subarray_sum(nums, k))


if __name__ == "__main__":
    main()


# 560. 和为 K 的子数组  中等
#
# 【题目描述】
# 统计数组中和恰好为 k 的连续子数组的个数（元素可含负数）。
#
# 【示例】
# nums = [1,1,1], k = 2  →  2
#
# 【思路提示】
# 前缀和 + 哈希表计数：遍历时累加前缀和，查询 (前缀和 - k) 出现过几次。
#
# 【输入格式】
# 第一行：整数列表；第二行：k。
#
# 【样例输入】
# [1,1,1]
# 2
# 【样例输出】
# 2
