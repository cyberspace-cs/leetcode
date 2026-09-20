# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 283    标题: 移动零    难度: 简单    分类: 双指针
# 链接: https://leetcode.cn/problems/move-zeroes/
# 运行: python3 "0283-移动零.py"   （按提示输入，或重定向样例输入）

def move_zeroes(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # 在这里写你的代码（原地修改 nums 后返回）
    non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero] = nums[i]
            non_zero += 1
    for i in range(non_zero, len(nums)):
        nums[i] = 0
    return nums


def main():
    nums = eval(input())
    print(move_zeroes(nums))


if __name__ == "__main__":
    main()


# 283. 移动零  简单
#
# 【题目描述】
# 把数组中所有 0 移动到末尾，同时保持非零元素的相对顺序，必须原地操作、不复制数组。
#
# 【示例】
# nums = [0,1,0,3,12]  →  [1,3,12,0,0]
#
# 【思路提示】
# 快慢指针：快指针找非零元素，慢指针指向待写入位置，最后把剩余位置补 0。
#
# 【输入格式】
# 一行：整数列表，如 [0,1,0,3,12]。
#
# 【样例输入】
# [0,1,0,3,12]
# 【样例输出】
# [1, 3, 12, 0, 0]
