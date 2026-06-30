# CNN Fear & Greed Index for TradingView (Pine Script)

[![Daily Update](https://img.shields.io/badge/Daily%20Update-4:30%20PM%20EST-brightgreen.svg)]()
[![Pine Script](https://img.shields.io/badge/Pine%20Script-v6-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()
[![Author: Casual Study](https://img.shields.io/badge/Author-Casual%20Study-purple.svg)](https://casualstudy.site/)

**[🇺🇸 English](#english) | [🇨🇳 简体中文](#chinese)**

---

<a id="english"></a>
## 🇺🇸 English

### Overview
Welcome to the **CNN Fear & Greed Index for TradingView** repository by **Casual Study**! You can find more of my work on my official website: [casualstudy.site](https://casualstudy.site/).

TradingView's native environment is sandboxed, meaning Pine Script cannot automatically fetch data from external APIs or third-party web sources like the CNN Fear and Greed Index. To solve this limitation, this repository provides a **fully automated backend** that scrapes the latest CNN Fear and Greed Index data daily and injects it directly into a ready-to-use Pine Script file (`CNN.pine`).

By simply copying the code from `CNN.pine` into your TradingView Pine Editor, you can visualize the exact CNN Fear & Greed Index on your charts, perfectly synchronized with your stock or crypto analysis.

### Key Features
* **Daily Auto-Updates**: Our VPS runs a cron job that automatically updates the `CNN.pine` file every weekday at **4:30 PM EST** (shortly after the US stock market closes).
* **Plug & Play**: No coding or API keys required. Just copy and paste.
* **Accurate Historical Data**: Includes historical sentiment data dating back to 2020.
* **Optimized for TradingView**: Written in modern Pine Script (v6), fully compatible with all TradingView charts and timeframes.

### How to Use
Since TradingView cannot pull external data directly, you need to copy the code from this repository:
1. Open the [`CNN.pine`](CNN.pine) file in this repository.
2. Copy all the code.
3. Go to [TradingView](https://www.tradingview.com/), open a chart, and click on **Pine Editor** at the bottom.
4. Paste the code into the editor and click **Add to Chart**.
5. *Tip: Check back occasionally to copy the latest version if you want the most up-to-date daily data!*

---

<a id="chinese"></a>
## 🇨🇳 简体中文

### 简介
欢迎来到由 **Casual Study** 维护的 **TradingView CNN 恐惧与贪婪指数** 开源项目！想了解更多关于我的内容，欢迎访问我的官方网站：[casualstudy.site](https://casualstudy.site/)。

由于 TradingView 的 Pine Script 运行在严格的沙盒环境中，它无法自动从外部 API 或第三方网站提取数据。这就导致我们无法直接在 TradingView 中调用 CNN 官方的恐惧与贪婪指数 (Fear & Greed Index)。为了打破这个限制，本项目建立了一套**全自动的后台更新系统**。它每天会自动抓取 CNN 的最新数据，并将其直接硬编码（Hardcode）到 `CNN.pine` 文件中。

你只需要直接复制 `CNN.pine` 里面的代码，就可以在 TradingView 上完美呈现出 CNN 的市场情绪指数。

### 核心特性
* **每日定时更新**：部署在 VPS 上的更新程序会在每个交易日的 **美东时间下午 4:30**（美股收盘后）自动抓取最新数据并更新此仓库。
* **开箱即用**：无需任何编程基础或 API 密钥，纯手工复制粘贴即可使用。
* **完整的历史数据**：包含了自 2020 年以来的完整历史市场情绪数据。
* **TradingView 完美兼容**：使用最新的 Pine Script (v6) 编写，兼容所有图表和时间级别。

### 使用教程
因为 TradingView 无法直接同步外部数据，你需要手动复制代码来使用：
1. 打开本项目中的 [`CNN.pine`](CNN.pine) 文件。
2. 复制里面的所有代码。
3. 打开 [TradingView](https://www.tradingview.com/) 图表，点击下方的 **Pine Editor (Pine 脚本编辑器)**。
4. 将代码粘贴进去，然后点击 **添加到图表 (Add to Chart)**。
5. *提示：如果你想获取最新的每日数据，记得隔段时间来本仓库复制一次最新的代码！*
