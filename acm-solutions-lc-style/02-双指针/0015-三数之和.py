# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 15    标题: 三数之和    难度: 中等    分类: 双指针
# 链接: https://leetcode.cn/problems/3sum/
# 运行: python3 "0015-三数之和.py"   （按提示输入，或重定向样例输入）

def three_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # 在这里写你的代码
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return res


def main():
    nums = eval(input())
    print(three_sum(nums))


if __name__ == "__main__":
    main()


# 15. 三数之和  中等
#
# 【题目描述】
# 找出数组中所有和为 0 且互不重复的三元组。
#
# 【示例】
# nums = [-1,0,1,2,-1,-4]  →  [[-1,-1,2],[-1,0,1]]
#
# 【思路提示】
# 排序后固定第一个数，其余用左右双指针求解；注意跳过重复元素去重。
#
# 【输入格式】
# 一行：整数列表，如 [-1,0,1,2,-1,-4]。
#
# 【样例输入】
# [-1,0,1,2,-1,-4]
# 【样例输出】
# [[-1, -1, 2], [-1, 0, 1]]
