# -*- coding: utf-8 -*-
# LeetCode 热题 HOT 100 · ACM 单组输入解题（个人模板风格）
# 题号: 207    标题: 课程表    难度: 中等    分类: 图论
# 链接: https://leetcode.cn/problems/course-schedule/
# 运行: python3 "0207-课程表.py"   （按提示输入，或重定向样例输入）

def can_finish(num_courses, prerequisites):
    """
    :type num_courses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    # 在这里写你的代码（拓扑排序）
    from collections import deque
    adj = [[] for _ in range(num_courses)]
    indeg = [0] * num_courses
    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1
    dq = deque(i for i in range(num_courses) if indeg[i] == 0)
    seen = 0
    while dq:
        u = dq.popleft()
        seen += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                dq.append(v)
    return seen == num_courses


def main():
    num_courses = int(input())
    prerequisites = eval(input())
    print(can_finish(num_courses, prerequisites))


if __name__ == "__main__":
    main()


# 207. 课程表  中等
#
# 【题目描述】
# 给定课程数与先修关系，判断能否修完所有课程（即依赖图是否存在环）。
#
# 【示例】
# numCourses = 2, prerequisites = [[1,0]]  →  true
#
# 【思路提示】
# 拓扑排序（Kahn + 入度队列）；或 DFS 三色标记检测环。
#
# 【输入格式】
# 第一行：numCourses；第二行：先修关系列表，如 [[1,0]]（b 是 a 的先修课）。
#
# 【样例输入】
# 2
# [[1,0]]
# 【样例输出】
# True
