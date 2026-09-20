# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 287    标题: 寻找重复数    难度: 中等    分类: 技巧
# 链接: https://leetcode.cn/problems/find-the-duplicate-number/
# 运行: python3 "0287-寻找重复数.py"   （按提示输入，或重定向样例输入）

def find_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 在这里写你的代码（Floyd 判圈找环入口）
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


def main():
    nums = eval(input())
    print(find_duplicate(nums))


if __name__ == "__main__":
    main()


# 287. 寻找重复数  中等
#
# 【题目描述】
# 长度为 n+1 的数组中数字都在 1..n 之间，只有一个数字重复，找出它；要求不修改数组且使用 O(1) 额外空间。
#
# 【示例】
# nums = [1,3,4,2,2]  →  2
#
# 【思路提示】
# 把下标映射视为链表指针，用 Floyd 判圈法找环入口即为重复数；也可用二分 + 计数。
#
# 【输入格式】
# 一行：整数列表（长度 n，取值 1..n-1，仅一个数字重复），如 [1,3,4,2,2]。
#
# 【样例输入】
# [1,3,4,2,2]
# 【样例输出】
# 2
