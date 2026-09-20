# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 33    标题: 搜索旋转排序数组    难度: 中等    分类: 二分查找
# 链接: https://leetcode.cn/problems/search-in-rotated-sorted-array/
# 运行: python3 "0033-搜索旋转排序数组.py"   （按提示输入，或重定向样例输入）

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # 在这里写你的代码
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def main():
    nums = eval(input())
    target = int(input())
    print(search(nums, target))


if __name__ == "__main__":
    main()


# 33. 搜索旋转排序数组  中等
#
# 【题目描述】
# 在某个位置旋转过的升序数组中查找目标值，返回下标，不存在返回 -1。
#
# 【示例】
# nums = [4,5,6,7,0,1,2], target = 0  →  4
#
# 【思路提示】
# 二分时先判断 [left, mid] 与 [mid, right] 哪一段是有序的，再决定收缩方向。
#
# 【输入格式】
# 第一行：旋转后的升序整数列表（元素互不相同）；第二行：target。
#
# 【样例输入】
# [4,5,6,7,0,1,2]
# 0
# 【样例输出】
# 4
