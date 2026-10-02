# Autumn-Recruit Algo Notes（秋招算法学习仓库）

> **一个可执行的算法 / 机器学习 / 大模型 / 强化学习 / 计算机视觉 / NLP / 时间序列面试备战体系**
>
> **11 大模块 · 114 篇中文教学 Notebook · 核心算法全部手写实现，附 sklearn/torch 数值对照**
>
> ⚠️ 原始 GitHub 仓库链接待补充：本仓库为 2026-10 初发布的新仓库，GitHub 搜索索引尚未收录，拿到原链接后即 fork 并补全。

---

## 📌 项目简介

面向**算法 / AI 岗位秋招**的一站式备战仓库：从公式推导 → 手写实现 → 数值对照 → 面试八股 → 复盘闭环全流程覆盖，内含：

- 数据结构与算法、机器学习、深度学习、LLM 大模型、八股与工程、强化学习、优化算法、计算机视觉、NLP、时间序列等 **11 大方向**
- **114 篇中文教学 Notebook**，每篇含公式推导、从零手写实现、可运行测试用例与自测清单
- **全量可验证**：114/114 本通过 nbclient 执行验证（含 sklearn/torch 数值对照断言，无需 GPU、无需联网）
- **面试向闭环**：高频题单 + 90 连问速答 + 手写三件套默写 + 面试复盘模板
- **进度可追踪**：ROADMAP.md 分阶段路线 + 每个模块自测清单，学一章勾一章

| 徽章 | 值 |
| --- | --- |
| License | MIT |
| Python | 3.9+ |
| Modules | 11 |
| Notebooks | 114 |
| 实现方式 | from scratch |
| 文档 | 中文教学 |
| 验证 | nbclient 114/114 |

---

## 🗂️ 模块总览（11 大模块）

| 模块 | 内容 | 教学 Notebook | 状态 |
| --- | --- | --- | --- |
| 01-数据结构与算法 | 排序/哈希/双指针/链表/二分/二叉树/回溯/DP/贪心/图/堆/位运算/字符串 | 14 篇教学 + 11 份模板 | ✅ |
| 02-机器学习 | 线性回归/逻辑回归/NB 与 K-Means/SVM/PCA/GBDT/决策树随机森林/KNN/AdaBoost/神经网络/HMM/CRF/特征工程 | 13 篇推导笔记 | ✅ |
| 03-深度学习 | BP/CNN/优化器/RNN-LSTM/BN/激活初始化/正则化 | 7 篇模型笔记 | ✅ |
| 04-LLM 大模型 | Transformer 从零手推 24 讲（架构/分词/训练/推理/RL 对齐） | 24 篇教学 notebook | ✅ |
| 05-八股与工程 | Python/OS/网络/数据库/Redis/分布式/工程工具/高频手撕 | 8 篇八股 notebook | ✅ |
| 06-面试复盘 | 复盘方法论 + 每场面试记录模板 | — | ✅ |
| 07-强化学习 | MDP/DP/MC-TD/Q 学习/DQN/策略梯度/PPO-GRPO/面试八股 | 8 篇教学 notebook（含 15 张推导图） | ✅ |
| 08-优化算法 | SGD/动量/Adam/AdamW/学习率调度/二阶优化/LLM 训练(FP16-BF16-ZeRO) + 经典优化(LP/IP/GA/SA/TS/PSO/ACO/KKT) | 13 篇优化笔记（推导+对照+自测） | ✅ |
| 09-计算机视觉 | 图像基础/边缘特征/CNN/经典架构/目标检测(R-CNN-YOLO v1-v11 全系列)/分割(FCN-U-Net 全家族-DeepLab)/度量学习/SAM 基础模型 | 11 篇视觉笔记（推导+对照+自测） | ✅ |
| 10-自然语言处理 | 文本表示/TF-IDF/n-gram 语言模型/词向量(Word2Vec-GloVe)/RNN-LSTM/Attention-Transformer/预训练(mini-BERT-mini-GPT)/分类与标注 | 8 篇 NLP 笔记（推导+对照+自测） | ✅ |
| 11-时间序列 | 平稳性/ADF/ACF-PACF/ARMA-ARIMA/指数平滑/分解/特征工程·ML/深度学习(LSTM-递归 vs 直接)/评估与异常检测 | 8 篇时序笔记（推导+对照+自测） | ✅ |

---

## ✨ 项目特色

1. **手写优先**：排序/DP/LR/SVM/PCA/GBDT/CNN/LSTM/DQN/PPO/Transformer 全部从零实现，附 sklearn/torch 数值对照（梯度一致、输出逐位一致）——"看一眼就知道公式怎么变成代码"
2. **推导 + 配图**：每篇含变种模型谱系表、逐步推导（面试手推模板）、matplotlib 过程图，打开 notebook 即可直接看到推导过程与结果图
3. **面试向**：高频题单 + 90 连问速答 + 手写三件套默写 + 面试复盘闭环
4. **可验证**：全仓 114 本 notebook 已全部通过 nbclient 全量执行验证（含 sklearn/torch 对照断言；无需 GPU、无需联网）
5. **进度可追踪**：ROADMAP 分阶段 + 每个模块自测清单，学一章勾一章

---

## 🚀 快速开始

```bash
# 克隆仓库（拿到原仓库链接后更新此命令）
# git clone <原仓库地址>
# cd autumn-recruit-algo-notes

# 环境自写、随机种子固定，可复现全部数值结果
pip install -r requirements.txt

# 按 ROADMAP.md 分阶段学习，每章学完勾选自测清单
```

---

## 🧭 学习路线（ROADMAP）

```
阶段一：算法基础
  01-数据结构与算法（排序/DP/图论高频题单）

阶段二：机器学习核心
  02-机器学习 → 03-深度学习 → 08-优化算法

阶段三：前沿方向
  04-LLM 大模型（Transformer 24 讲）→ 07-强化学习

阶段四：垂直领域
  09-计算机视觉 → 10-自然语言处理 → 11-时间序列

阶段五：面试冲刺
  05-八股与工程 → 06-面试复盘
```

---

## 🔗 相关链接

- 原始仓库：**待补充**（2026-10 新发布，GitHub 搜索未收录）
- 我们的算法仓库：[cyberspace-cs/leetcode](https://github.com/cyberspace-cs/leetcode)（LeetCode HOT100 题解）
- 竞赛雷达：[cyberspace-cs/contest-tracker](https://github.com/cyberspace-cs/contest-tracker)
