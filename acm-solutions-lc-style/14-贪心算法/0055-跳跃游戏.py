# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 55    标题: 跳跃游戏    难度: 中等    分类: 贪心算法
# 链接: https://leetcode.cn/problems/jump-game/
# 运行: python3 "0055-跳跃游戏.py"   （按提示输入，或重定向样例输入）

def can_jump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # 在这里写你的代码
    reach = 0
    for i, x in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + x)
    return True


def main():
    nums = eval(input())
    print(can_jump(nums))


if __name__ == "__main__":
    main()


# 55. 跳跃游戏  中等
#
# 【题目描述】
# 数组每个元素表示该位置能跳跃的最大长度，判断能否从第一个位置到达最后一个位置。
#
# 【示例】
# nums = [2,3,1,1,4]  →  true
#
# 【思路提示】
# 维护当前能到达的最远下标，若最远下标小于当前下标则说明卡住。
#
# 【输入格式】
# 一行：每格最大跳跃长度，如 [2,3,1,1,4]。
#
# 【样例输入】
# [2,3,1,1,4]
# 【样例输出】
# True
