# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 169    标题: 多数元素    难度: 简单    分类: 技巧
# 链接: https://leetcode.cn/problems/majority-element/
# 运行: python3 "0169-多数元素.py"   （按提示输入，或重定向样例输入）

def majority_element(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 在这里写你的代码（Boyer-Moore 投票）
    cand = None
    count = 0
    for x in nums:
        if count == 0:
            cand = x
            count = 1
        elif x == cand:
            count += 1
        else:
            count -= 1
    return cand


def main():
    nums = eval(input())
    print(majority_element(nums))


if __name__ == "__main__":
    main()


# 169. 多数元素  简单
#
# 【题目描述】
# 找出数组中出现次数大于 ⌊n/2⌋ 的元素，可以假设该元素一定存在。
#
# 【示例】
# nums = [2,2,1,1,1,2,2]  →  2
#
# 【思路提示】
# Boyer-Moore 投票算法：候选数相同时计数 +1，不同则 -1，计数归零时换候选。
#
# 【输入格式】
# 一行：整数列表（保证存在出现次数 > n/2 的元素）。
#
# 【样例输入】
# [2,2,1,1,1,2,2]
# 【样例输出】
# 2
