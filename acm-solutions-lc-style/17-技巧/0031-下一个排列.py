# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 31    标题: 下一个排列    难度: 中等    分类: 技巧
# 链接: https://leetcode.cn/problems/next-permutation/
# 运行: python3 "0031-下一个排列.py"   （按提示输入，或重定向样例输入）

def next_permutation(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # 在这里写你的代码
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])
    return nums


def main():
    nums = eval(input())
    print(next_permutation(nums))


if __name__ == "__main__":
    main()


# 31. 下一个排列  中等
#
# 【题目描述】
# 把数组原地变换为字典序中的下一个更大排列；若不存在更大排列，则变换为升序的最小排列。
#
# 【示例】
# nums = [1,2,3]  →  [1,3,2]
#
# 【思路提示】
# 从右向左找第一个升序对 (i, i+1)，在右侧找比 nums[i] 大的最小数与它交换，再反转 i 之后的后缀。
#
# 【输入格式】
# 一行：整数列表，如 [1,2,3]。
#
# 【样例输入】
# [1,2,3]
# 【样例输出】
# [1, 3, 2]
