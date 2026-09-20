# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 153    标题: 寻找旋转排序数组中的最小值    难度: 中等    分类: 二分查找
# 链接: https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/
# 运行: python3 "0153-寻找旋转排序数组中的最小值.py"   （按提示输入，或重定向样例输入）

def find_min(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 在这里写你的代码
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]


def main():
    nums = eval(input())
    print(find_min(nums))


if __name__ == "__main__":
    main()


# 153. 寻找旋转排序数组中的最小值  中等
#
# 【题目描述】
# 返回旋转后的升序数组中的最小元素（数组元素互不相同）。
#
# 【示例】
# nums = [3,4,5,1,2]  →  1
#
# 【思路提示】
# 二分比较 nums[mid] 与 nums[right]，据此判断最小值在左半段还是右半段。
#
# 【输入格式】
# 一行：旋转后的升序整数列表（元素互不相同），如 [3,4,5,1,2]。
#
# 【样例输入】
# [3,4,5,1,2]
# 【样例输出】
# 1
