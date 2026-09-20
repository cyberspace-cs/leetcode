# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 239    标题: 滑动窗口最大值    难度: 困难    分类: 子串
# 链接: https://leetcode.cn/problems/sliding-window-maximum/
# 运行: python3 "0239-滑动窗口最大值.py"   （按提示输入，或重定向样例输入）

def max_sliding_window(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # 在这里写你的代码
    from collections import deque
    dq = deque()
    res = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res


def main():
    nums = eval(input())
    k = int(input())
    print(max_sliding_window(nums, k))


if __name__ == "__main__":
    main()


# 239. 滑动窗口最大值  困难
#
# 【题目描述】
# 给定数组和窗口大小 k，窗口每次向右滑动一位，返回每个窗口中的最大值。
#
# 【示例】
# nums = [1,3,-1,-3,5,3,6,7], k = 3  →  [3,3,5,5,6,7]
#
# 【思路提示】
# 单调递减的双端队列存下标，保证队首始终是当前窗口最大值。
#
# 【输入格式】
# 第一行：整数列表；第二行：窗口大小 k。
#
# 【样例输入】
# [1,3,-1,-3,5,3,6,7]
# 3
# 【样例输出】
# [3, 3, 5, 5, 6, 7]
