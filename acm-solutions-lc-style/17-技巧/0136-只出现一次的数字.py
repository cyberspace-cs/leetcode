# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 136    标题: 只出现一次的数字    难度: 简单    分类: 技巧
# 链接: https://leetcode.cn/problems/single-number/
# 运行: python3 "0136-只出现一次的数字.py"   （按提示输入，或重定向样例输入）

def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 在这里写你的代码（异或）
    x = 0
    for v in nums:
        x ^= v
    return x


def main():
    nums = eval(input())
    print(single_number(nums))


if __name__ == "__main__":
    main()


# 136. 只出现一次的数字  简单
#
# 【题目描述】
# 数组中除某个元素只出现一次外，其余元素都出现两次，找出这个只出现一次的元素；要求线性时间、常数空间。
#
# 【示例】
# nums = [4,1,2,1,2]  →  4
#
# 【思路提示】
# 利用异或性质：x ^ x = 0、x ^ 0 = x，全部异或后结果即为答案。
#
# 【输入格式】
# 一行：整数列表（除一个数字外其余均出现两次），如 [4,1,2,1,2]。
#
# 【样例输入】
# [4,1,2,1,2]
# 【样例输出】
# 4
