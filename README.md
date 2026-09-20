# LeetCode 力扣刷题仓库 · 热题 HOT 100

> 一个「**题面模板 + 完整解题 + 本地自测**」三合一的算法刷题仓库。
> 按 **17 个题型**分类，覆盖 **力扣热题 HOT 100 全部 100 题**，全部代码可直接运行、逐题带样例。

![problems](https://img.shields.io/badge/题目-100%20题-blue)
![categories](https://img.shields.io/badge/题型-17%20类-green)
![python](https://img.shields.io/badge/Python-3.8%2B-yellow)

---

## 这是什么

很多人刷力扣会遇到三个问题：

1. **题目散落**，做过的题过几天就找不到，也没法复盘；
2. **只会在力扣网页上写**，脱离网页就没有 `Solution` 类、没有测试用例，本地跑不起来；
3. **面试 / 笔试是 ACM 模式**（自己读标准输入、自己打印输出），和力扣的函数式写法完全不一样。

这个仓库就是来解决这三件事的：

| 你的需求 | 用哪个目录 |
| --- | --- |
| 按题型整理一套题面，自己动手写 | [`hot100/`](#1-hot100--题面模板自己动手写) |
| 想要能直接跑的完整答案，对拍 / 背模板 | [`acm-solutions/`](#2-acm-solutions--完整解题多组测试) |
| 面试笔试的 ACM 单组输入写法 | [`acm-solutions-lc-style/`](#3-acm-solutions-lc-style--完整解题单组输入个人模板风格) |
| 存放自己手写的题解 | [`ACM-lc/`](#4-acm-lc--你的手写题解区) |

---

## 适合谁

- **正在刷力扣 HOT 100** 的同学：可以直接按题型目录顺序推进，一题一文件；
- **准备笔试 / OJ / ACM 模式**的同学：`acm-solutions/` 和 `acm-solutions-lc-style/` 就是标准输入输出写法；
- **想背模板、复习套路**的同学：每个文件头部都有「思路提示」，代码即模板；
- **想自建题库**的同学：题面数据集中在 `scripts/` 里，改一处就能批量重生成。

---

## 目录一览

```
leetcode/
├── ACM-lc/                     # 你手写的题解（自由发挥区，生成器不会碰）
│   ├── HOT100/                 #   已写的 HOT100 题解
│   └── ...
├── hot100/                     # 100 题【题面模板】：只有骨架，等你填
├── acm-solutions/              # 100 题【完整解题】：ACM 多组测试格式（首行 T）
├── acm-solutions-lc-style/     # 100 题【完整解题】：ACM 单组输入 + 个人模板风格
├── core-lc/                    # 预留（核心题库）
└── scripts/                    # 生成器与校验器（题面/答案的数据源）
```

> 三个 `100 题` 目录**结构完全一致**（同样的 17 个分类、同样的文件命名），
> 唯一的区别是**文件内容形式**，可以按需挑一个用，也可以互相参照。

---

## 题型分布（17 类 / 100 题）

| # | 分类 | 题量 | # | 分类 | 题量 |
| --- | --- | --- | --- | --- | --- |
| 01 | 哈希 | 3 | 10 | 回溯 | 8 |
| 02 | 双指针 | 4 | 11 | 二分查找 | 6 |
| 03 | 滑动窗口 | 2 | 12 | 栈 | 5 |
| 04 | 子串 | 3 | 13 | 堆 | 3 |
| 05 | 普通数组 | 5 | 14 | 贪心算法 | 4 |
| 06 | 矩阵 | 4 | 15 | 动态规划 | 10 |
| 07 | 链表 | 14 | 16 | 多维动态规划 | 5 |
| 08 | 二叉树 | 15 | 17 | 技巧 | 5 |
| 09 | 图论 | 4 | | **合计** | **100** |

分类顺序与力扣官方「热题 HOT 100」的题型划分一致，方便按套路成组刷。

---

## 三条使用路线

### 路线 A：纯刷题（推荐新手）

1. 打开 `hot100/<分类>/<题号>-<题名>.py`；
2. 文件里已经写好题面、示例、思路提示和函数骨架；
3. 在 `raise NotImplementedError` 的位置写你的代码；
4. 用 `if __name__ == "__main__":` 里的位置补充自测用例。

### 路线 B：对答案 / 背模板

1. 打开 `acm-solutions/<分类>/<题号>-<题名>.py`；
2. 文件头部有完整的【输入格式】【样例输入】【样例输出】；
3. 直接跑样例，验证你对题意的理解；
4. 对照 `acm-solutions-lc-style/` 里同题的**单组输入**版本，看两种写法差异。

### 路线 C：面试 / 笔试突击

先看 `acm-solutions-lc-style/`（单组输入，最像现场手写），
再对照 `acm-solutions/`（多组测试，最像 OJ 出题），两种都能写说明真的掌握了。

---

## 各目录详解

### 1. `hot100/` — 题面模板（自己动手写）

每个文件只提供**骨架**，不包含答案：

```python
"""
LeetCode 热题 HOT 100 · 第 001 / 100 题
================================================================
题号 : 1
标题 : 两数之和
难度 : 简单
分类 : 哈希
链接 : https://leetcode.cn/problems/two-sum/
================================================================

【题目描述】...
【示例】...
【思路提示】...
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # TODO: 在这里实现你的解法
        raise NotImplementedError("待完成")
```

同题若在 `ACM-lc/` 里已有你的手写题解，文件里会额外标注「可对拍参考」。

### 2. `acm-solutions/` — 完整解题（多组测试）

标准 ACM 格式：**第 1 行为 `T`（测试组数）**，之后紧跟 T 组数据。

```bash
python3 "acm-solutions/01-哈希/0001-两数之和.py"
```

约定：

- 布尔值输出 `true` / `false`
- 空结果输出 `EMPTY`
- 二叉树用层序数组 + `null` 表示
- 链表题会真实构造节点（含环、相交、随机指针等场景）

### 3. `acm-solutions-lc-style/` — 完整解题（单组输入，个人模板风格）

最贴近**手写习惯**的版本：单组输入、`eval(input())` 直接读列表、`print()` 直接输出。

```python
def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # 在这里写你的代码
    hashmap = {}
    for i, x in enumerate(nums):
        if target - x in hashmap:
            return [hashmap[target - x], i]
        hashmap[x] = i
    return []


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())
    print(two_sum(nums, target))


if __name__ == "__main__":
    main()


# 题面 / 示例 / 思路 / 输入格式 / 样例（以 # 注释放在文件末尾）
```

输入约定：

| 数据类型 | 读法 |
| --- | --- |
| 整数数组 | `nums = eval(input())` |
| 标量 | `n = int(input())` |
| 字符串 | `s = input()` |
| 多个标量同一行 | `n, k = map(int, input().split())` |
| 树 / 嵌套结构 | `root = [3,9,20,None,None,15,7]` |

### 4. `ACM-lc/` — 你的手写题解区

**自由发挥区**：所有生成器都不会修改这个目录，放心写。
（其中的 `HOT100/` 是已手写的一部分题解。）

---

## 命名规范

三个 100 题目录统一使用：

- **分类目录**：`NN-题型/`，`NN` 为两位顺序号，保证排序稳定；
- **题目文件**：`题号4位补零-中文标题.py`，例如 `0001-两数之和.py`、`1143-最长公共子序列.py`。

这样做的目的：**按题号排序时不会错乱**，也方便脚本批量处理。

---

## 快速开始

### 1. 克隆

```bash
git clone https://gitee.com/buleboy8065/leetcode.git
cd leetcode
```

### 2. 环境

只需要 Python（无第三方依赖）：

```bash
python3 --version    # 建议 3.8+，本仓库在 3.11.9 下测试
```

### 3. 跑一题试试

```bash
# 单组输入版本
printf '4\n2 7 11 15\n9\n' | python3 "acm-solutions-lc-style/01-哈希/0001-两数之和.py"
# 输出: [0, 1]

# 多组测试版本（首行 2 表示两组数据）
printf '2\n4 9\n2 7 11 15\n3 6\n3 2 4\n' | python3 "acm-solutions/01-哈希/0001-两数之和.py"
# 输出:
# 0 1
# 1 2
```

### 4. 每题都自带样例

打开任意文件，文件末尾（单组输入版）或文件头部（多组测试版）都能找到
**可直接复制粘贴**的样例输入 / 样例输出，不用去力扣网页找。

---

## 脚本与维护

`scripts/` 目录同时充当**题库数据源**和**生成工具**：

| 脚本 | 作用 |
| --- | --- |
| `gen_hot100_templates.py` | 生成 `hot100/` 题面模板（内含题面/示例/思路提示数据） |
| `gen_acm_solutions.py` | 生成 `acm-solutions/`（数据在 `scripts/acm_data/`） |
| `check_acm_solutions.py` | **回归校验**：跑完 100 题的样例并比对输出 |
| `gen_acm_lc_style.py` | 生成 `acm-solutions-lc-style/`（数据在 `scripts/acm_lc_data/`） |
| `check_acm_lc_style.py` | **回归校验**：跑完 100 题的样例并比对输出 |

```bash
# 重新生成
python3 scripts/gen_hot100_templates.py
python3 scripts/gen_acm_solutions.py
python3 scripts/gen_acm_lc_style.py

# 全量校验（当前状态：100 / 100 通过）
python3 scripts/check_acm_solutions.py
python3 scripts/check_acm_lc_style.py
```

想批量改题面、加题目、换实现，改 `scripts/` 里的数据后重跑即可。

---

## 常见问题

**Q：三个目录我该用哪个？**
想自己写 → `hot100/`；想要完整答案 → `acm-solutions-lc-style/`（单组输入，好读）；
要练 OJ 多组测试 → `acm-solutions/`。

**Q：为什么 `acm-solutions/` 是 `true`/`false`，而 `acm-solutions-lc-style/` 是 `True`/`False`？**
前者模拟 OJ 的字符串输出规范，后者直接 `print` Python 对象，更贴近手写调试习惯。

**Q：我改了生成目录里的文件，重跑脚本会不会覆盖？**
**会覆盖。** 生成目录（`hot100/`、`acm-solutions/`、`acm-solutions-lc-style/`）都由脚本产出，
你的代码请写在 `ACM-lc/`，或修改 `scripts/` 下的数据源。

**Q：题目答案保证正确吗？**
`acm-solutions/` 与 `acm-solutions-lc-style/` 里的每题都跑了自带的样例并通过
（当前 100 / 100）。但样例覆盖有限，**建议以力扣官方判题为准**。

---

## 说明

- 题目描述、示例均整理自力扣（LeetCode 中国站）公开题目，版权归力扣及原出题方所有；
- 本仓库仅用于**个人学习与刷题记录**，请勿用于商业用途；
- 解题代码为学习过程中的实现，**不保证是最优解**，欢迎自行优化。

祝刷题顺利，早日上岸 🎉
