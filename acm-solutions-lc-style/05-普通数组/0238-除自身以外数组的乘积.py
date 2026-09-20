# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 238    标题: 除自身以外数组的乘积    难度: 中等    分类: 普通数组
# 链接: https://leetcode.cn/problems/product-of-array-except-self/
# 运行: python3 "0238-除自身以外数组的乘积.py"   （按提示输入，或重定向样例输入）

def product_except_self(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # 在这里写你的代码
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res


def main():
    nums = eval(input())
    print(product_except_self(nums))


if __name__ == "__main__":
    main()


# 238. 除自身以外数组的乘积  中等
#
# 【题目描述】
# 返回数组 answer，其中 answer[i] 是 nums 中除 nums[i] 外其余元素的乘积；不能使用除法，要求 O(n)。
#
# 【示例】
# nums = [1,2,3,4]  →  [24,12,8,6]
#
# 【思路提示】
# 正反向各扫一遍，用前缀积与后缀积相乘得到结果。
#
# 【输入格式】
# 一行：整数列表，如 [1,2,3,4]。
#
# 【样例输入】
# [1,2,3,4]
# 【样例输出】
# [24, 12, 8, 6]
