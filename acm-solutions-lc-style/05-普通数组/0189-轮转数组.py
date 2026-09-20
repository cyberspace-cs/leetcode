# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 189    标题: 轮转数组    难度: 中等    分类: 普通数组
# 链接: https://leetcode.cn/problems/rotate-array/
# 运行: python3 "0189-轮转数组.py"   （按提示输入，或重定向样例输入）

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # 在这里写你的代码（原地修改 nums 后返回）
    n = len(nums)
    if n:
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
    return nums


def main():
    nums = eval(input())
    k = int(input())
    print(rotate(nums, k))


if __name__ == "__main__":
    main()


# 189. 轮转数组  中等
#
# 【题目描述】
# 把数组中的元素向右轮转 k 个位置，尽量使用原地算法。
#
# 【示例】
# nums = [1,2,3,4,5,6,7], k = 3  →  [5,6,7,1,2,3,4]
#
# 【思路提示】
# 三次翻转：整体翻转 → 前 k 个翻转 → 后 n-k 个翻转（注意 k 先对 n 取模）。
#
# 【输入格式】
# 第一行：整数列表；第二行：k（向右轮转步数）。
#
# 【样例输入】
# [1,2,3,4,5,6,7]
# 3
# 【样例输出】
# [5, 6, 7, 1, 2, 3, 4]
