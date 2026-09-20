# -*- coding: utf-8 -*-
"""
生成 LeetCode 热题 HOT 100 的题目模板（按题型分类 + 统一批量命名）。

用法:
    python scripts/gen_hot100_templates.py

产出:
    hot100/
      README.md
      01-哈希/0001-两数之和.py
      01-哈希/0049-字母异位词分组.py
      ...

说明:
    - 本脚本只生成「题面骨架 + 解题入口」，不包含题解实现。
    - 原有 ACM-lc/ 目录不会被修改。
    - 如题目信息有更新，直接修改本文件中的 PROBLEMS 后重新运行即可。
"""

import os

# 生成目录（相对仓库根目录）
ROOT_DIR = 'hot100'

# 已在 ACM-lc 中练习过的题号，会在模板与 README 中标注
SOLVED_IN_ACM = {1, 3, 11, 15, 42, 49, 128, 283}

# META: 分类目录名 -> 分类展示名
CATEGORIES = [
    '哈希', '双指针', '滑动窗口', '子串', '普通数组', '矩阵', '链表',
    '二叉树', '图论', '回溯', '二分查找', '栈', '堆', '贪心算法',
    '动态规划', '多维动态规划', '技巧',
]

# 字段说明:
# (题号, slug, 标题, 难度, 分类, 方法名, 参数, 返回, 描述, 示例, 思路提示)
#   方法名/参数/返回 为 None 时表示「设计类」题目，使用自定义类骨架
PROBLEMS = [
    # ---------------- 哈希 ----------------
    (1, 'two-sum', '两数之和', '简单', '哈希', 'twoSum', 'nums: List[int], target: int', 'List[int]',
     '给定整数数组 nums 和整数目标值 target，在数组中找出和为 target 的两个整数，返回它们的数组下标（保证只有一组有效答案）。',
     'nums = [2,7,11,15], target = 9  →  [0,1]',
     '哈希表存「值 → 下标」，边遍历边查 target - n。'),
    (49, 'group-anagrams', '字母异位词分组', '中等', '哈希', 'groupAnagrams', 'strs: List[str]', 'List[List[str]]',
     '给定字符串数组，把字母异位词（字符组成相同、顺序不同）归到同一组，组内与组间顺序不限。',
     'strs = ["eat","tea","tan","ate","nat","bat"]  →  [["bat"],["nat","tan"],["ate","eat","tea"]]',
     '以「排序后的字符串」或「26 位字符计数元组」作为哈希键分组。'),
    (128, 'longest-consecutive-sequence', '最长连续序列', '中等', '哈希', 'longestConsecutive', 'nums: List[int]', 'int',
     '给定未排序整数数组 nums，找出数字连续的最长序列长度，要求算法时间复杂度 O(n)。',
     'nums = [100,4,200,1,3,2]  →  4   # 最长连续序列为 1,2,3,4',
     '全部放入集合，仅从「没有前驱 x-1」的数字开始向后计数，避免重复扫描。'),

    # ---------------- 双指针 ----------------
    (283, 'move-zeroes', '移动零', '简单', '双指针', 'moveZeroes', 'nums: List[int]', 'None',
     '把数组中所有 0 移动到末尾，同时保持非零元素的相对顺序，必须原地操作、不复制数组。',
     'nums = [0,1,0,3,12]  →  [1,3,12,0,0]',
     '快慢指针：快指针找非零元素，慢指针指向待写入位置，最后把剩余位置补 0。'),
    (11, 'container-with-most-water', '盛最多水的容器', '中等', '双指针', 'maxArea', 'height: List[int]', 'int',
     '给定高度数组 height，选出两条竖线，使它们与 x 轴围成的容器能盛最多的水。',
     'height = [1,8,6,2,5,4,8,3,7]  →  49',
     '左右双指针向中间收缩，每次移动较矮的一侧（面积由短板决定）。'),
    (15, '3sum', '三数之和', '中等', '双指针', 'threeSum', 'nums: List[int]', 'List[List[int]]',
     '找出数组中所有和为 0 且互不重复的三元组。',
     'nums = [-1,0,1,2,-1,-4]  →  [[-1,-1,2],[-1,0,1]]',
     '排序后固定第一个数，其余用左右双指针求解；注意跳过重复元素去重。'),
    (42, 'trapping-rain-water', '接雨水', '困难', '双指针', 'trap', 'height: List[int]', 'int',
     '给定柱子高度数组，计算下雨之后这些柱子之间能接住多少雨水。',
     'height = [0,1,0,2,1,0,1,3,2,1,2,1]  →  6',
     '每格存水量 = min(左侧最高, 右侧最高) - 当前高度；可用双指针或单调栈实现。'),

    # ---------------- 滑动窗口 ----------------
    (3, 'longest-substring-without-repeating-characters', '无重复字符的最长子串', '中等', '滑动窗口', 'lengthOfLongestSubstring', 's: str', 'int',
     '给定字符串 s，找出其中不含重复字符的最长子串，返回其长度。',
     's = "abcabcbb"  →  3   # 最长子串为 "abc"',
     '滑动窗口 + 哈希记录字符最近出现下标，遇到重复字符则收缩左边界。'),
    (438, 'find-all-anagrams-in-a-string', '找到字符串中所有字母异位词', '中等', '滑动窗口', 'findAnagrams', 's: str, p: str', 'List[int]',
     '给定字符串 s 和 p，找出 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。',
     's = "cbaebabacd", p = "abc"  →  [0,6]',
     '固定长度窗口滑动，比较窗口字符计数与 p 的字符计数。'),

    # ---------------- 子串 ----------------
    (560, 'subarray-sum-equals-k', '和为 K 的子数组', '中等', '子串', 'subarraySum', 'nums: List[int], k: int', 'int',
     '统计数组中和恰好为 k 的连续子数组的个数（元素可含负数）。',
     'nums = [1,1,1], k = 2  →  2',
     '前缀和 + 哈希表计数：遍历时累加前缀和，查询 (前缀和 - k) 出现过几次。'),
    (239, 'sliding-window-maximum', '滑动窗口最大值', '困难', '子串', 'maxSlidingWindow', 'nums: List[int], k: int', 'List[int]',
     '给定数组和窗口大小 k，窗口每次向右滑动一位，返回每个窗口中的最大值。',
     'nums = [1,3,-1,-3,5,3,6,7], k = 3  →  [3,3,5,5,6,7]',
     '单调递减的双端队列存下标，保证队首始终是当前窗口最大值。'),
    (76, 'minimum-window-substring', '最小覆盖子串', '困难', '子串', 'minWindow', 's: str, t: str', 'str',
     '在 s 中找出涵盖 t 中所有字符（含重复计数）的最短子串，不存在则返回空串。',
     's = "ADOBECODEBANC", t = "ABC"  →  "BANC"',
     '滑动窗口 + need/window 计数，窗口满足条件后不断收缩左边界取最优。'),

    # ---------------- 普通数组 ----------------
    (53, 'maximum-subarray', '最大子数组和', '中等', '普通数组', 'maxSubArray', 'nums: List[int]', 'int',
     '给定整数数组，找出和最大的连续子数组，返回其最大和。',
     'nums = [-2,1,-3,4,-1,2,1,-5,4]  →  6   # 子数组 [4,-1,2,1]',
     'Kadane 算法：cur = max(x, cur + x)，同时维护全局最大值。'),
    (56, 'merge-intervals', '合并区间', '中等', '普通数组', 'merge', 'intervals: List[List[int]]', 'List[List[int]]',
     '合并所有重叠的区间，返回互不重叠的区间数组。',
     'intervals = [[1,3],[2,6],[8,10],[15,18]]  →  [[1,6],[8,10],[15,18]]',
     '按左端点排序后一次遍历，判断当前区间是否与结果末尾重叠。'),
    (189, 'rotate-array', '轮转数组', '中等', '普通数组', 'rotate', 'nums: List[int], k: int', 'None',
     '把数组中的元素向右轮转 k 个位置，尽量使用原地算法。',
     'nums = [1,2,3,4,5,6,7], k = 3  →  [5,6,7,1,2,3,4]',
     '三次翻转：整体翻转 → 前 k 个翻转 → 后 n-k 个翻转（注意 k 先对 n 取模）。'),
    (238, 'product-of-array-except-self', '除自身以外数组的乘积', '中等', '普通数组', 'productExceptSelf', 'nums: List[int]', 'List[int]',
     '返回数组 answer，其中 answer[i] 是 nums 中除 nums[i] 外其余元素的乘积；不能使用除法，要求 O(n)。',
     'nums = [1,2,3,4]  →  [24,12,8,6]',
     '正反向各扫一遍，用前缀积与后缀积相乘得到结果。'),
    (41, 'first-missing-positive', '缺失的第一个正数', '困难', '普通数组', 'firstMissingPositive', 'nums: List[int]', 'int',
     '找出未在数组中出现的最小正整数，要求 O(n) 时间、O(1) 额外空间。',
     'nums = [3,4,-1,1]  →  2',
     '原地哈希：把数值 x 交换到下标 x-1 处，再找第一个 nums[i] != i+1 的位置。'),

    # ---------------- 矩阵 ----------------
    (73, 'set-matrix-zeroes', '矩阵置零', '中等', '矩阵', 'setZeroes', 'matrix: List[List[int]]', 'None',
     '若矩阵中某元素为 0，则把它所在的行和列全部置为 0，要求原地修改。',
     'matrix = [[1,1,1],[1,0,1],[1,1,1]]  →  [[1,0,1],[0,0,0],[1,0,1]]',
     '用首行、首列充当标记数组，并单独记录首行/首列本身是否需要置零。'),
    (54, 'spiral-matrix', '螺旋矩阵', '中等', '矩阵', 'spiralOrder', 'matrix: List[List[int]]', 'List[int]',
     '按顺时针螺旋顺序返回矩阵中的所有元素。',
     'matrix = [[1,2,3],[4,5,6],[7,8,9]]  →  [1,2,3,6,9,8,7,4,5]',
     '维护上、下、左、右四个边界，逐层向内收缩。'),
    (48, 'rotate-image', '旋转图像', '中等', '矩阵', 'rotate', 'matrix: List[List[int]]', 'None',
     '把 n×n 的二维矩阵顺时针旋转 90°，要求原地完成。',
     'matrix = [[1,2,3],[4,5,6],[7,8,9]]  →  [[7,4,1],[8,5,2],[9,6,3]]',
     '先沿主对角线做转置，再对每一行做左右翻转。'),
    (240, 'search-a-2d-matrix-ii', '搜索二维矩阵 II', '中等', '矩阵', 'searchMatrix', 'matrix: List[List[int]], target: int', 'bool',
     '在每行从左到右、每列从上到下均递增的矩阵中查找目标值是否存在。',
     'matrix = [[1,4,7],[2,5,8],[3,6,9]], target = 5  →  true',
     '从右上角出发：当前值大于目标则左移一列，小于目标则下移一行。'),

    # ---------------- 链表 ----------------
    (160, 'intersection-of-two-linked-lists', '相交链表', '简单', '链表', 'getIntersectionNode', 'headA: ListNode, headB: ListNode', 'Optional[ListNode]',
     '找出两个单链表相交的起始节点；若不相交则返回 None。',
     'intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]  →  值为 8 的节点',
     '双指针各自走完本链表后切换到对方头节点，两指针相遇处即为交点。'),
    (206, 'reverse-linked-list', '反转链表', '简单', '链表', 'reverseList', 'head: Optional[ListNode]', 'Optional[ListNode]',
     '反转一个单链表并返回新的头节点。',
     'head = [1,2,3,4,5]  →  [5,4,3,2,1]',
     '迭代：用 prev / curr 两个指针逐个改变指向；也可用递归。'),
    (234, 'palindrome-linked-list', '回文链表', '简单', '链表', 'isPalindrome', 'head: Optional[ListNode]', 'bool',
     '判断一个单链表是否为回文链表。',
     'head = [1,2,2,1]  →  true',
     '快慢指针找到中点，反转后半段，再逐节点比较。'),
    (141, 'linked-list-cycle', '环形链表', '简单', '链表', 'hasCycle', 'head: Optional[ListNode]', 'bool',
     '判断链表中是否存在环。',
     'head = [3,2,0,-4], pos = 1  →  true',
     '快慢指针，若两者相遇则存在环。'),
    (142, 'linked-list-cycle-ii', '环形链表 II', '中等', '链表', 'detectCycle', 'head: Optional[ListNode]', 'Optional[ListNode]',
     '若链表有环，返回入环的第一个节点；否则返回 None。',
     'head = [3,2,0,-4], pos = 1  →  值为 2 的节点',
     '快慢指针相遇后，把一个指针移回头节点，两指针同速前进再次相遇即为入环点。'),
    (21, 'merge-two-sorted-lists', '合并两个有序链表', '简单', '链表', 'mergeTwoLists', 'list1: Optional[ListNode], list2: Optional[ListNode]', 'Optional[ListNode]',
     '将两个升序链表合并为一个新的升序链表并返回。',
     '[1,2,4] + [1,3,4]  →  [1,1,2,3,4,4]',
     '哑结点 + 双指针逐个比较接入，最后接上未走完的链表。'),
    (2, 'add-two-numbers', '两数相加', '中等', '链表', 'addTwoNumbers', 'l1: Optional[ListNode], l2: Optional[ListNode]', 'Optional[ListNode]',
     '两个非负整数以逆序方式存储在链表中，求它们的和并以同样方式返回。',
     '[2,4,3] + [5,6,4]  →  [7,0,8]   # 342 + 465 = 807',
     '逐位相加并维护进位 carry，注意最后可能还剩一个进位节点。'),
    (19, 'remove-nth-node-from-end-of-list', '删除链表的倒数第 N 个结点', '中等', '链表', 'removeNthFromEnd', 'head: Optional[ListNode], n: int', 'Optional[ListNode]',
     '删除链表的倒数第 n 个节点，并返回头节点。',
     'head = [1,2,3,4,5], n = 2  →  [1,2,3,5]',
     '哑结点 + 快慢指针，快指针先走 n+1 步，再同步前进直到快指针到末尾。'),
    (24, 'swap-nodes-in-pairs', '两两交换链表中的节点', '中等', '链表', 'swapPairs', 'head: Optional[ListNode]', 'Optional[ListNode]',
     '两两交换相邻节点，并返回交换后的头节点；不能修改节点内部的值。',
     'head = [1,2,3,4]  →  [2,1,4,3]',
     '哑结点 + 三指针迭代完成局部换位；也可用递归。'),
    (25, 'reverse-nodes-in-k-group', 'K 个一组翻转链表', '困难', '链表', 'reverseKGroup', 'head: Optional[ListNode], k: int', 'Optional[ListNode]',
     '每 k 个节点为一组进行翻转；不足 k 个的尾部节点保持原有顺序。',
     'head = [1,2,3,4,5], k = 2  →  [2,1,4,3,5]',
     '先探测剩余是否够 k 个，再对这一段做局部反转并接回前后。'),
    (138, 'copy-list-with-random-pointer', '随机链表的复制', '中等', '链表', 'copyRandomList', 'head: Optional[Node]', 'Optional[Node]',
     '复制一个带有 random 随机指针的链表，返回其深拷贝。',
     'head = [[7,null],[13,0],[11,4],[10,2],[1,0]]  →  深拷贝后的等值链表',
     '哈希表映射「原节点 → 新节点」；也可用拼接-拆分的 O(1) 空间做法。'),
    (148, 'sort-list', '排序链表', '中等', '链表', 'sortList', 'head: Optional[ListNode]', 'Optional[ListNode]',
     '将链表按升序排序并返回，要求在 O(n log n) 时间内完成。',
     'head = [4,2,1,3]  →  [1,2,3,4]',
     '归并排序：快慢指针找中点，递归排序后合并两条有序链表。'),
    (23, 'merge-k-sorted-lists', '合并 K 个升序链表', '困难', '链表', 'mergeKLists', 'lists: List[Optional[ListNode]]', 'Optional[ListNode]',
     '合并 k 个升序链表为一个升序链表。',
     'lists = [[1,4,5],[1,3,4],[2,6]]  →  [1,1,2,3,4,4,5,6]',
     '分治法两两合并，或用最小堆维护 k 个当前头节点。'),
    (146, 'lru-cache', 'LRU 缓存', '中等', '链表', None, None, None,
     '设计 LRU（最近最少使用）缓存，支持 get 和 put，且两个操作都要求 O(1) 平均时间复杂度。',
     'capacity = 2: put(1,1), put(2,2), get(1) → 1, put(3,3), get(2) → -1',
     '哈希表 + 双向链表（Python 中也可直接用 collections.OrderedDict）。'),

    # ---------------- 二叉树 ----------------
    (94, 'binary-tree-inorder-traversal', '二叉树的中序遍历', '简单', '二叉树', 'inorderTraversal', 'root: Optional[TreeNode]', 'List[int]',
     '返回二叉树的中序遍历（左-根-右）结果。',
     'root = [1,null,2,3]  →  [1,3,2]',
     '递归或显式栈；进阶可用 Morris 遍历做到 O(1) 额外空间。'),
    (104, 'maximum-depth-of-binary-tree', '二叉树的最大深度', '简单', '二叉树', 'maxDepth', 'root: Optional[TreeNode]', 'int',
     '返回二叉树的最大深度（根到最远叶节点的节点数）。',
     'root = [3,9,20,null,null,15,7]  →  3',
     '递归 max(左子树, 右子树) + 1；也可用层序遍历统计层数。'),
    (226, 'invert-binary-tree', '翻转二叉树', '简单', '二叉树', 'invertTree', 'root: Optional[TreeNode]', 'Optional[TreeNode]',
     '翻转二叉树，使每个节点的左右子树互换，返回根节点。',
     'root = [4,2,7,1,3,6,9]  →  [4,7,2,9,6,3,1]',
     '递归交换每个节点的左右子树。'),
    (101, 'symmetric-tree', '对称二叉树', '简单', '二叉树', 'isSymmetric', 'root: Optional[TreeNode]', 'bool',
     '判断二叉树是否轴对称。',
     'root = [1,2,2,3,4,4,3]  →  true',
     '递归比较 (左.left, 右.right) 与 (左.right, 右.left)；也可用队列迭代。'),
    (543, 'diameter-of-binary-tree', '二叉树的直径', '简单', '二叉树', 'diameterOfBinaryTree', 'root: Optional[TreeNode]', 'int',
     '返回二叉树中任意两个节点之间最长路径的边数。',
     'root = [1,2,3,4,5]  →  3',
     '后序递归求深度，同时用「左深度 + 右深度」更新全局答案。'),
    (102, 'binary-tree-level-order-traversal', '二叉树的层序遍历', '中等', '二叉树', 'levelOrder', 'root: Optional[TreeNode]', 'List[List[int]]',
     '按层返回二叉树节点的值（从上到下、每层从左到右）。',
     'root = [3,9,20,null,null,15,7]  →  [[3],[9,20],[15,7]]',
     '队列 BFS，每轮先记录当前队列长度，即该层节点数。'),
    (108, 'convert-sorted-array-to-binary-search-tree', '将有序数组转换为二叉搜索树', '简单', '二叉树', 'sortedArrayToBST', 'nums: List[int]', 'Optional[TreeNode]',
     '把升序数组转换为高度平衡的二叉搜索树。',
     'nums = [-10,-3,0,5,9]  →  [0,-3,9,-10,null,5]',
     '每次取区间中点作为根，再递归构造左右子树。'),
    (98, 'validate-binary-search-tree', '验证二叉搜索树', '中等', '二叉树', 'isValidBST', 'root: Optional[TreeNode]', 'bool',
     '判断二叉树是否为有效的二叉搜索树（左 < 根 < 右，且子树同样满足）。',
     'root = [2,1,3]  →  true',
     '递归时向下传递上下界 (low, high)；或中序遍历检查是否严格递增。'),
    (230, 'kth-smallest-element-in-a-bst', '二叉搜索树中第 K 小的元素', '中等', '二叉树', 'kthSmallest', 'root: Optional[TreeNode], k: int', 'int',
     '返回二叉搜索树中第 k 小的元素值。',
     'root = [3,1,4,null,2], k = 1  →  1',
     '中序遍历，计数到第 k 个即返回（可提前剪枝）。'),
    (199, 'binary-tree-right-side-view', '二叉树的右视图', '中等', '二叉树', 'rightSideView', 'root: Optional[TreeNode]', 'List[int]',
     '按从上到下的顺序，返回从右侧能看到的节点值。',
     'root = [1,2,3,null,5,null,4]  →  [1,3,4]',
     '层序遍历，取每层的最后一个节点；也可用 DFS 按「先右后左」首次到达。'),
    (114, 'flatten-binary-tree-to-linked-list', '二叉树展开为链表', '中等', '二叉树', 'flatten', 'root: Optional[TreeNode]', 'None',
     '把二叉树原地展开为只有右子节点的单链表，顺序与前序遍历一致。',
     'root = [1,2,5,3,4,null,6]  →  [1,null,2,null,3,null,4,null,5,null,6]',
     '前序收集节点后重新连接；或用「寻找左子树最右节点」的原地拼接法。'),
    (105, 'construct-binary-tree-from-preorder-and-inorder-traversal', '从前序与中序遍历序列构造二叉树', '中等', '二叉树', 'buildTree', 'preorder: List[int], inorder: List[int]', 'Optional[TreeNode]',
     '根据前序遍历和中序遍历结果构造出原始二叉树（元素不重复）。',
     'preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]  →  [3,9,20,null,null,15,7]',
     '前序首元素为根，用哈希表定位它在中序中的下标以划分左右子树。'),
    (437, 'path-sum-iii', '路径总和 III', '中等', '二叉树', 'pathSum', 'root: Optional[TreeNode], targetSum: int', 'int',
     '统计二叉树中节点值之和等于 targetSum 的路径条数（路径方向只能向下，不必从根开始）。',
     'root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8  →  3',
     '前缀和 + 回溯：遍历时统计 (当前前缀和 - targetSum) 在哈希表中的出现次数。'),
    (236, 'lowest-common-ancestor-of-a-binary-tree', '二叉树的最近公共祖先', '中等', '二叉树', 'lowestCommonAncestor', 'root: TreeNode, p: TreeNode, q: TreeNode', 'TreeNode',
     '返回二叉树中两个指定节点的最近公共祖先。',
     'root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1  →  3',
     '后序递归：左右子树各找到一个目标则当前节点即为答案，否则返回非空的一侧。'),
    (124, 'binary-tree-maximum-path-sum', '二叉树中的最大路径和', '困难', '二叉树', 'maxPathSum', 'root: Optional[TreeNode]', 'int',
     '返回二叉树中任意一条路径的最大路径和（路径可不经过根，但同一节点最多出现一次）。',
     'root = [-10,9,20,null,null,15,7]  →  42',
     '后序递归返回「单边最大贡献」，同时用「左贡献 + 右贡献 + 根值」更新全局答案。'),

    # ---------------- 图论 ----------------
    (200, 'number-of-islands', '岛屿数量', '中等', '图论', 'numIslands', 'grid: List[List[str]]', 'int',
     '给定由 "1"（陆地）和 "0"（水）组成的二维网格，统计岛屿（上下左右相连的陆地）数量。',
     'grid = [["1","1","0"],["1","0","0"],["0","0","1"]]  →  2',
     'DFS / BFS 洪水填充，把访问过的陆地标记掉；也可用并查集。'),
    (994, 'rotting-oranges', '腐烂的橘子', '中等', '图论', 'orangesRotting', 'grid: List[List[int]]', 'int',
     '每分钟腐烂橘子会感染上下左右相邻的新鲜橘子，返回所有橘子腐烂所需的最少分钟数；不可能则返回 -1。',
     'grid = [[2,1,1],[1,1,0],[0,1,1]]  →  4',
     '多源 BFS：把所有腐烂橘子入队，按层扩展并计时。'),
    (207, 'course-schedule', '课程表', '中等', '图论', 'canFinish', 'numCourses: int, prerequisites: List[List[int]]', 'bool',
     '给定课程数与先修关系，判断能否修完所有课程（即依赖图是否存在环）。',
     'numCourses = 2, prerequisites = [[1,0]]  →  true',
     '拓扑排序（Kahn + 入度队列）；或 DFS 三色标记检测环。'),
    (208, 'implement-trie-prefix-tree', '实现 Trie (前缀树)', '中等', '图论', None, None, None,
     '实现前缀树 Trie，支持插入单词、查询完整单词、查询是否存在指定前缀。',
     'insert("apple"), search("apple") → true, search("app") → false, startsWith("app") → true',
     '每个节点用 dict / 定长数组保存子节点，并用布尔标记是否为单词结尾。'),

    # ---------------- 回溯 ----------------
    (46, 'permutations', '全排列', '中等', '回溯', 'permute', 'nums: List[int]', 'List[List[int]]',
     '给定不含重复数字的数组，返回其所有可能的全排列。',
     'nums = [1,2,3]  →  [[1,2,3],[1,3,2],[2,1,3],...]',
     '回溯 + used 标记已选元素；也可用「依次交换」的写法。'),
    (78, 'subsets', '子集', '中等', '回溯', 'subsets', 'nums: List[int]', 'List[List[int]]',
     '给定不含重复元素的数组，返回其所有可能的子集（幂集）。',
     'nums = [1,2,3]  →  [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]',
     '回溯：对每个位置做「选 / 不选」两个分支。'),
    (17, 'letter-combinations-of-a-phone-number', '电话号码的字母组合', '中等', '回溯', 'letterCombinations', 'digits: str', 'List[str]',
     '给定仅含数字 2-9 的字符串，返回它所有可能代表的字母组合。',
     'digits = "23"  →  ["ad","ae","af","bd","be","bf","cd","ce","cf"]',
     '回溯 + 电话键盘映射表，逐位枚举可选字母。'),
    (39, 'combination-sum', '组合总和', '中等', '回溯', 'combinationSum', 'candidates: List[int], target: int', 'List[List[int]]',
     '给定无重复元素的候选数组和目标值，找出所有和为目标的组合，每个数字可被重复选取。',
     'candidates = [2,3,6,7], target = 7  →  [[2,2,3],[7]]',
     '排序 + 回溯，用 start 下标保证组合不重复，剩余值小于当前数时剪枝。'),
    (22, 'generate-parentheses', '括号生成', '中等', '回溯', 'generateParenthesis', 'n: int', 'List[str]',
     '生成所有由 n 对括号组成的有效（正确闭合）组合。',
     'n = 3  →  ["((()))","(()())","(())()","()(())","()()()"]',
     '回溯：左括号数 < n 时可加左括号；右括号数 < 左括号数时可加右括号。'),
    (79, 'word-search', '单词搜索', '中等', '回溯', 'exist', 'board: List[List[str]], word: str', 'bool',
     '在二维字符网格中判断能否通过上下左右相邻的单元格按顺序拼出给定单词（同一格不可重复使用）。',
     'board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"  →  true',
     'DFS + 剪枝，把访问过的格子临时标记，回溯时恢复。'),
    (131, 'palindrome-partitioning', '分割回文串', '中等', '回溯', 'partition', 's: str', 'List[List[str]]',
     '把字符串分割成若干子串，使每个子串都是回文串，返回所有可能的分割方案。',
     's = "aab"  →  [["a","a","b"],["aa","b"]]',
     '回溯 + 剪枝：只有当当前子串是回文时才继续向下递归。'),
    (51, 'n-queens', 'N 皇后', '困难', '回溯', 'solveNQueens', 'n: int', 'List[List[str]]',
     '在 n×n 棋盘上放置 n 个皇后，使它们互不攻击，返回所有不同的解法。',
     'n = 4  →  [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]',
     '逐行放置 + 用集合记录已占用的列、主对角线、副对角线来判重。'),

    # ---------------- 二分查找 ----------------
    (35, 'search-insert-position', '搜索插入位置', '简单', '二分查找', 'searchInsert', 'nums: List[int], target: int', 'int',
     '在升序数组中查找目标值，存在则返回下标，不存在则返回它应被插入的位置。',
     'nums = [1,3,5,6], target = 5  →  2',
     '标准二分查找，循环结束时返回左边界 left。'),
    (74, 'search-a-2d-matrix', '搜索二维矩阵', '中等', '二分查找', 'searchMatrix', 'matrix: List[List[int]], target: int', 'bool',
     '在每行升序、且每行首元素大于上一行末元素的矩阵中查找目标值。',
     'matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3  →  true',
     '把二维矩阵视为一维有序数组做二分，通过 divmod 完成下标映射。'),
    (34, 'find-first-and-last-position-of-element-in-sorted-array', '在排序数组中查找元素的第一个和最后一个位置', '中等', '二分查找', 'searchRange', 'nums: List[int], target: int', 'List[int]',
     '返回目标值在升序数组中的起始与结束下标；不存在则返回 [-1,-1]。',
     'nums = [5,7,7,8,8,10], target = 8  →  [3,4]',
     '两次二分：一次求左边界（找第一个 >= target），一次求右边界（找最后一个 <= target）。'),
    (33, 'search-in-rotated-sorted-array', '搜索旋转排序数组', '中等', '二分查找', 'search', 'nums: List[int], target: int', 'int',
     '在某个位置旋转过的升序数组中查找目标值，返回下标，不存在返回 -1。',
     'nums = [4,5,6,7,0,1,2], target = 0  →  4',
     '二分时先判断 [left, mid] 与 [mid, right] 哪一段是有序的，再决定收缩方向。'),
    (153, 'find-minimum-in-rotated-sorted-array', '寻找旋转排序数组中的最小值', '中等', '二分查找', 'findMin', 'nums: List[int]', 'int',
     '返回旋转后的升序数组中的最小元素（数组元素互不相同）。',
     'nums = [3,4,5,1,2]  →  1',
     '二分比较 nums[mid] 与 nums[right]，据此判断最小值在左半段还是右半段。'),
    (4, 'median-of-two-sorted-arrays', '寻找两个正序数组的中位数', '困难', '二分查找', 'findMedianSortedArrays', 'nums1: List[int], nums2: List[int]', 'float',
     '给定两个正序数组，返回它们合并后的中位数，要求时间复杂度 O(log(m+n))。',
     'nums1 = [1,3], nums2 = [2]  →  2.0',
     '在较短数组上二分划分点，使左半部分元素总数正确且「左最大 ≤ 右最小」。'),

    # ---------------- 栈 ----------------
    (20, 'valid-parentheses', '有效的括号', '简单', '栈', 'isValid', 's: str', 'bool',
     '判断只含 ()[]{} 的字符串中的括号是否有效闭合。',
     's = "()[]{}"  →  true',
     '左括号入栈，遇到右括号时与栈顶匹配，最终栈必须为空。'),
    (155, 'min-stack', '最小栈', '中等', '栈', None, None, None,
     '设计一个支持 push、pop、top 操作，并能在常数时间内检索到最小元素的栈。',
     'push(-2), push(0), push(-3), getMin() → -3, pop(), getMin() → -2',
     '使用辅助栈与主栈同步记录「当前最小值」。'),
    (394, 'decode-string', '字符串解码', '中等', '栈', 'decodeString', 's: str', 'str',
     '解码形如 k[encoded_string] 的字符串，k 表示其后方括号内内容重复的次数，支持嵌套。',
     's = "3[a2[c]]"  →  "accaccacc"',
     '用数字栈与字符串栈模拟解析；也可写递归下降解析器。'),
    (739, 'daily-temperatures', '每日温度', '中等', '栈', 'dailyTemperatures', 'temperatures: List[int]', 'List[int]',
     '给定每日温度，返回每天需要等待多少天才会出现更高的温度；不会出现则记为 0。',
     'temperatures = [73,74,75,71,69,72,76,73]  →  [1,1,4,2,1,1,0,0]',
     '单调递减栈存下标，遇到更高温度时不断弹栈并结算答案。'),
    (84, 'largest-rectangle-in-histogram', '柱状图中最大的矩形', '困难', '栈', 'largestRectangleArea', 'heights: List[int]', 'int',
     '给定柱状图中各柱子的高度，求其中能勾勒出的最大矩形面积。',
     'heights = [2,1,5,6,2,3]  →  10',
     '单调递增栈（首尾各补一个 0），弹栈时以该柱高为矩形高计算面积。'),

    # ---------------- 堆 ----------------
    (215, 'kth-largest-element-in-an-array', '数组中的第K个最大元素', '中等', '堆', 'findKthLargest', 'nums: List[int], k: int', 'int',
     '返回数组中第 k 个最大的元素（按排序后的位置计，不去重）。',
     'nums = [3,2,1,5,6,4], k = 2  →  5',
     '维护大小为 k 的小顶堆；或用快速选择（平均 O(n)）。'),
    (347, 'top-k-frequent-elements', '前 K 个高频元素', '中等', '堆', 'topKFrequent', 'nums: List[int], k: int', 'List[int]',
     '返回数组中出现频率最高的 k 个元素，顺序不限。',
     'nums = [1,1,1,2,2,3], k = 2  →  [1,2]',
     '先用哈希计数，再用小顶堆或桶排序取前 k 个。'),
    (295, 'find-median-from-data-stream', '数据流的中位数', '困难', '堆', None, None, None,
     '设计一个数据结构，支持不断添加整数，并随时返回当前所有元素的中位数。',
     'addNum(1), addNum(2), findMedian() → 1.5, addNum(3), findMedian() → 2.0',
     '对顶堆：大顶堆存较小的一半，小顶堆存较大的一半，保持两堆大小平衡。'),

    # ---------------- 贪心算法 ----------------
    (121, 'best-time-to-buy-and-sell-stock', '买卖股票的最佳时机', '简单', '贪心算法', 'maxProfit', 'prices: List[int]', 'int',
     '给定每日股价，只允许一次买入和一次卖出（先买后卖），求最大利润；不能获利则返回 0。',
     'prices = [7,1,5,3,6,4]  →  5',
     '一次遍历，维护历史最低价，用当前价减最低价不断更新最大利润。'),
    (55, 'jump-game', '跳跃游戏', '中等', '贪心算法', 'canJump', 'nums: List[int]', 'bool',
     '数组每个元素表示该位置能跳跃的最大长度，判断能否从第一个位置到达最后一个位置。',
     'nums = [2,3,1,1,4]  →  true',
     '维护当前能到达的最远下标，若最远下标小于当前下标则说明卡住。'),
    (45, 'jump-game-ii', '跳跃游戏 II', '中等', '贪心算法', 'jump', 'nums: List[int]', 'int',
     '在保证能到达终点的前提下，求跳到最后一个位置所需的最少跳跃次数。',
     'nums = [2,3,1,1,4]  →  2',
     '贪心分层：在当前一步能覆盖的范围内，选择能跳到最远的位置作为下一步。'),
    (763, 'partition-labels', '划分字母区间', '中等', '贪心算法', 'partitionLabels', 's: str', 'List[int]',
     '把字符串划分为尽可能多的片段，使同一字母最多只出现在一个片段中，返回每个片段的长度。',
     's = "ababcbacadefegdehijhklij"  →  [9,7,8]',
     '先记录每个字符最后出现的位置，再遍历并不断扩张当前片段的右边界。'),

    # ---------------- 动态规划 ----------------
    (70, 'climbing-stairs', '爬楼梯', '简单', '动态规划', 'climbStairs', 'n: int', 'int',
     '每次可以爬 1 或 2 个台阶，求爬到第 n 阶有多少种不同的方法。',
     'n = 3  →  3   # 1+1+1 / 1+2 / 2+1',
     'dp[i] = dp[i-1] + dp[i-2]，可用两个滚动变量把空间优化到 O(1)。'),
    (118, 'pascals-triangle', '杨辉三角', '简单', '动态规划', 'generate', 'numRows: int', 'List[List[int]]',
     '生成杨辉三角的前 numRows 行。',
     'numRows = 5  →  [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]',
     '逐行构造：每行两端为 1，中间元素等于上一行相邻两数之和。'),
    (198, 'house-robber', '打家劫舍', '中等', '动态规划', 'rob', 'nums: List[int]', 'int',
     '相邻房屋不能在同一晚被偷，求在不触发报警的前提下能偷到的最大金额。',
     'nums = [2,7,9,3,1]  →  12',
     'dp[i] = max(dp[i-1], dp[i-2] + nums[i])，同样可滚动优化空间。'),
    (279, 'perfect-squares', '完全平方数', '中等', '动态规划', 'numSquares', 'n: int', 'int',
     '求把 n 表示为若干个完全平方数之和所需的最少个数。',
     'n = 12  →  3   # 12 = 4 + 4 + 4',
     '完全背包 / BFS：dp[i] = min(dp[i - j*j] + 1)。'),
    (322, 'coin-change', '零钱兑换', '中等', '动态规划', 'coinChange', 'coins: List[int], amount: int', 'int',
     '给定各种面额硬币（数量无限）和总金额，求凑出该金额所需的最少硬币数；无法凑出返回 -1。',
     'coins = [1,2,5], amount = 11  →  3   # 11 = 5 + 5 + 1',
     '完全背包：dp[j] = min(dp[j], dp[j - coin] + 1)，注意不可达状态用大数表示。'),
    (139, 'word-break', '单词拆分', '中等', '动态规划', 'wordBreak', 's: str, wordDict: List[str]', 'bool',
     '判断字符串能否被拆分成字典中出现的一个或多个单词。',
     's = "leetcode", wordDict = ["leet","code"]  →  true',
     'dp[i] 表示前 i 个字符可被拆分，枚举末尾单词并查表转移。'),
    (300, 'longest-increasing-subsequence', '最长递增子序列', '中等', '动态规划', 'lengthOfLIS', 'nums: List[int]', 'int',
     '求数组中最长严格递增子序列的长度（子序列不必连续）。',
     'nums = [10,9,2,5,3,7,101,18]  →  4   # [2,3,7,101]',
     'O(n²) 的 DP 定义；进阶用「贪心 + 二分」维护长度为 L 的最小结尾值，做到 O(n log n)。'),
    (152, 'maximum-product-subarray', '乘积最大子数组', '中等', '动态规划', 'maxProduct', 'nums: List[int]', 'int',
     '找出数组中乘积最大的连续子数组，返回该乘积。',
     'nums = [2,3,-2,4]  →  6   # [2,3]',
     '同时维护以 i 结尾的最大乘积与最小乘积，因为负数相乘会翻转大小关系。'),
    (416, 'partition-equal-subset-sum', '分割等和子集', '中等', '动态规划', 'canPartition', 'nums: List[int]', 'bool',
     '判断能否把数组分割成两个元素和相等的子集。',
     'nums = [1,5,11,5]  →  true   # [1,5,5] 与 [11]',
     '01 背包：目标和为 sum/2，dp[j] 表示能否恰好凑出 j（倒序枚举容量）。'),
    (32, 'longest-valid-parentheses', '最长有效括号', '困难', '动态规划', 'longestValidParentheses', 's: str', 'int',
     '找出字符串中最长的有效（正确闭合）括号子串，返回其长度。',
     's = "(()"  →  2',
     '栈存下标（先压入哨兵 -1）；或用 DP：dp[i] 表示以 i 结尾的最长有效长度。'),

    # ---------------- 多维动态规划 ----------------
    (62, 'unique-paths', '不同路径', '中等', '多维动态规划', 'uniquePaths', 'm: int, n: int', 'int',
     '机器人位于 m×n 网格左上角，每次只能向右或向下移动一步，求到达右下角的不同路径数。',
     'm = 3, n = 7  →  28',
     'dp[i][j] = dp[i-1][j] + dp[i][j-1]，可压缩为一维数组。'),
    (64, 'minimum-path-sum', '最小路径和', '中等', '多维动态规划', 'minPathSum', 'grid: List[List[int]]', 'int',
     '在只能向右或向下移动的前提下，求从网格左上角到右下角的最小路径数字总和。',
     'grid = [[1,3,1],[1,5,1],[4,2,1]]  →  7',
     '二维 DP，可直接原地更新网格，注意第一行与第一列的边界处理。'),
    (5, 'longest-palindromic-substring', '最长回文子串', '中等', '多维动态规划', 'longestPalindrome', 's: str', 'str',
     '给定字符串 s，找出其中最长的回文子串。',
     's = "babad"  →  "bab"（"aba" 也正确）',
     '中心扩展法最直观（O(n²) 时间、O(1) 空间）；也可用区间 DP 或 Manacher。'),
    (1143, 'longest-common-subsequence', '最长公共子序列', '中等', '多维动态规划', 'longestCommonSubsequence', 'text1: str, text2: str', 'int',
     '给定两个字符串，求它们的最长公共子序列的长度（子序列不必连续）。',
     'text1 = "abcde", text2 = "ace"  →  3   # "ace"',
     'dp[i][j]：字符相等则 dp[i-1][j-1] + 1，否则取 max(dp[i-1][j], dp[i][j-1])。'),
    (72, 'edit-distance', '编辑距离', '中等', '多维动态规划', 'minDistance', 'word1: str, word2: str', 'int',
     '求把 word1 转换成 word2 所需的最少操作次数，允许插入、删除、替换一个字符。',
     'word1 = "horse", word2 = "ros"  →  3',
     '二维 DP，注意边界初始化（dp[0][j] = j、dp[i][0] = i），字符不同时取三种操作的最小值 + 1。'),

    # ---------------- 技巧 ----------------
    (136, 'single-number', '只出现一次的数字', '简单', '技巧', 'singleNumber', 'nums: List[int]', 'int',
     '数组中除某个元素只出现一次外，其余元素都出现两次，找出这个只出现一次的元素；要求线性时间、常数空间。',
     'nums = [4,1,2,1,2]  →  4',
     '利用异或性质：x ^ x = 0、x ^ 0 = x，全部异或后结果即为答案。'),
    (169, 'majority-element', '多数元素', '简单', '技巧', 'majorityElement', 'nums: List[int]', 'int',
     '找出数组中出现次数大于 ⌊n/2⌋ 的元素，可以假设该元素一定存在。',
     'nums = [2,2,1,1,1,2,2]  →  2',
     'Boyer-Moore 投票算法：候选数相同时计数 +1，不同则 -1，计数归零时换候选。'),
    (75, 'sort-colors', '颜色分类', '中等', '技巧', 'sortColors', 'nums: List[int]', 'None',
     '给定只含 0、1、2 的数组，原地排序使相同元素相邻并按 0、1、2 顺序排列；不能使用库排序。',
     'nums = [2,0,2,1,1,0]  →  [0,0,1,1,2,2]',
     '荷兰国旗问题：用 p0、i、p2 三个指针一次遍历完成分区。'),
    (31, 'next-permutation', '下一个排列', '中等', '技巧', 'nextPermutation', 'nums: List[int]', 'None',
     '把数组原地变换为字典序中的下一个更大排列；若不存在更大排列，则变换为升序的最小排列。',
     'nums = [1,2,3]  →  [1,3,2]',
     '从右向左找第一个升序对 (i, i+1)，在右侧找比 nums[i] 大的最小数与它交换，再反转 i 之后的后缀。'),
    (287, 'find-the-duplicate-number', '寻找重复数', '中等', '技巧', 'findDuplicate', 'nums: List[int]', 'int',
     '长度为 n+1 的数组中数字都在 1..n 之间，只有一个数字重复，找出它；要求不修改数组且使用 O(1) 额外空间。',
     'nums = [1,3,4,2,2]  →  2',
     '把下标映射视为链表指针，用 Floyd 判圈法找环入口即为重复数；也可用二分 + 计数。'),
]

# ---------------------------------------------------------------- 模板与骨架

TREE_EXTRA = '''# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

LIST_EXTRA = '''# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''

RANDOM_LIST_EXTRA = '''# Definition for a Node.
class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
'''

DESIGN_STUBS = {
    146: '''class LRUCache:

    def __init__(self, capacity: int):
        # TODO: 初始化容量与数据结构
        pass

    def get(self, key: int) -> int:
        # TODO: 命中则返回并更新为最近使用，未命中返回 -1
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        # TODO: 写入或更新；超出容量时淘汰最久未使用项
        raise NotImplementedError
''',
    155: '''class MinStack:

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        raise NotImplementedError

    def pop(self) -> None:
        raise NotImplementedError

    def top(self) -> int:
        raise NotImplementedError

    def getMin(self) -> int:
        raise NotImplementedError
''',
    208: '''class Trie:

    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError

    def startsWith(self, prefix: str) -> bool:
        raise NotImplementedError
''',
    295: '''class MedianFinder:

    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        raise NotImplementedError

    def findMedian(self) -> float:
        raise NotImplementedError
''',
}

TEMPLATE = '''# -*- coding: utf-8 -*-
"""
LeetCode 热题 HOT 100 · 第 {idx:03d} / 100 题
{sep}
题号 : {num}
标题 : {title}
难度 : {difficulty}
分类 : {category}
链接 : https://leetcode.cn/problems/{slug}/
{sep}

【题目描述】
{desc}

【示例】
{example}

【思路提示】
{hint}
{note}
【说明】
本文件只提供题面与解题入口，具体实现请在下方 `Solution` 中完成，
并建议在 `if __name__ == "__main__":` 区域补充自测用例。
"""

from typing import List, Optional


{extra}{stub}

if __name__ == "__main__":
    # TODO: 在这里补充自测用例
{main_hint}
    pass
'''


def build_stub(num, func, params, ret):
    if num in DESIGN_STUBS:
        return DESIGN_STUBS[num]
    return (
        'class Solution:\n'
        '    def {func}(self, {params}) -> {ret}:\n'
        '        # TODO: 在这里实现你的解法\n'
        '        raise NotImplementedError("待完成")\n'
    ).format(func=func, params=params, ret=ret)


def build_extra(num, category):
    # 设计类题目使用自定义类骨架，不附带链表/树节点定义
    if num in DESIGN_STUBS:
        return ''
    if num == 138:
        return RANDOM_LIST_EXTRA + '\n\n'
    if category == '链表':
        return LIST_EXTRA + '\n\n'
    if category == '二叉树':
        return TREE_EXTRA + '\n\n'
    return ''


def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root = os.path.join(base, ROOT_DIR)

    # 校验分类完整性
    used = {p[4] for p in PROBLEMS}
    missing = used - set(CATEGORIES)
    if missing:
        raise SystemExit('PROBLEMS 中存在未登记的分类: %s' % missing)
    if len(PROBLEMS) != 100:
        raise SystemExit('题目数量应为 100，当前为 %d' % len(PROBLEMS))

    order = {c: i for i, c in enumerate(CATEGORIES)}

    # 按分类 + 题号排序，生成顺序编号
    entries = []
    for p in sorted(PROBLEMS, key=lambda x: (order[x[4]], x[0])):
        entries.append(p)

    written = []
    for idx, (num, slug, title, difficulty, category, func, params, ret, desc, example, hint) in enumerate(entries, 1):
        dir_name = '%02d-%s' % (order[category] + 1, category)
        target_dir = os.path.join(root, dir_name)
        os.makedirs(target_dir, exist_ok=True)

        note = ''
        if num in SOLVED_IN_ACM:
            note = '\n【备注】\nACM-lc 目录中已有本题题解，可作为对拍参考。\n'

        if num in DESIGN_STUBS:
            main_hint = '    # obj = <按题目要求实例化上面的类>\n'
        else:
            main_hint = '    # s = Solution()\n    # print(s.<方法名>(...))\n'

        content = TEMPLATE.format(
            idx=idx, num=num, title=title, difficulty=difficulty,
            category=category, slug=slug, desc=desc, example=example,
            hint=hint, note=note, sep='=' * 64, main_hint=main_hint,
            extra=build_extra(num, category),
            stub=build_stub(num, func, params, ret.rstrip() if ret else ''),
        )

        file_name = '%04d-%s.py' % (num, title)
        with open(os.path.join(target_dir, file_name), 'w', encoding='utf-8') as f:
            f.write(content)
        written.append((num, title, difficulty, category, dir_name, file_name))

    write_readme(root, written, order)
    print('生成完成: %d 个模板' % len(written))
    for c in CATEGORIES:
        d = '%02d-%s' % (order[c] + 1, c)
        n = sum(1 for w in written if w[3] == c)
        print('  %-16s %d 题' % (d, n))
    print('目录: %s' % os.path.relpath(root, base))


def write_readme(root, written, order):
    lines = []
    lines.append('# LeetCode 热题 HOT 100 · 模板仓库')
    lines.append('')
    lines.append('> 本目录只提供 **题面骨架 + 解题入口**，代码由你自己填写。')
    lines.append('> 仓库中原有的 `ACM-lc/` 目录保持不变，互不影响。')
    lines.append('')
    lines.append('## 命名规范')
    lines.append('')
    lines.append('- 分类目录：`NN-题型/`，`NN` 为两位顺序号，便于固定排序')
    lines.append('- 题目文件：`题号4位补零-中文标题.py`，例如 `0001-两数之和.py`')
    lines.append('- 每个文件包含：题号 / 标题 / 难度 / 分类 / 链接 / 题目描述 / 示例 / 思路提示 / 解题骨架')
    lines.append('')
    lines.append('## 进度总览')
    lines.append('')
    lines.append('共 100 题，覆盖 %d 个题型。' % len(CATEGORIES))
    lines.append('')

    # 分类统计表
    lines.append('| 分类 | 题量 | 目录 |')
    lines.append('| --- | --- | --- |')
    for i, c in enumerate(CATEGORIES):
        n = sum(1 for w in written if w[3] == c)
        lines.append('| %s | %d | `%02d-%s/` |' % (c, n, i + 1, c))
    lines.append('')

    # 明细表
    lines.append('## 题目清单')
    lines.append('')
    lines.append('| # | 题号 | 标题 | 难度 | 分类 | 文件 |')
    lines.append('| --- | --- | --- | --- | --- | --- |')
    for idx, (num, title, difficulty, category, dir_name, file_name) in enumerate(written, 1):
        mark = ' ✅' if num in SOLVED_IN_ACM else ''
        lines.append('| %d | %d | %s | %s | %s | `%s/%s`%s |' % (
            idx, num, title, difficulty, category, dir_name, file_name, mark))
    lines.append('')
    lines.append('> ✅ 表示 `ACM-lc/` 目录中已存在该题的本地题解。')
    lines.append('')
    lines.append('## 维护方式')
    lines.append('')
    lines.append('模板由脚本生成，如需增删题目或调整题面，请修改后重新运行：')
    lines.append('')
    lines.append('```bash')
    lines.append('python scripts/gen_hot100_templates.py')
    lines.append('```')
    lines.append('')

    with open(os.path.join(root, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


if __name__ == '__main__':
    main()
