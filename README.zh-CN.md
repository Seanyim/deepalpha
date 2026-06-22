# deepalpha

**[English](README.md) | 简体中文**

> **面向 Claude 的股票、加密与宏观研究路由器 —— 以一手 SEC 数据为依托(免费、无需 API key)。**

deepalpha 是一个 [Claude skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview):一个自包含的指令 + 参考文档 + Python 计算引擎的组合,把 Claude 变成一名投资研究分析师。你可以提出任何投资问题 —— 单只股票、ETF、某个板块、比特币、宏观环境,或你的整个组合 —— deepalpha 会自动判别意图、只触发相关分析模块、拉取一手数据、运行各自的框架,最后汇总成一个仪表盘外加一个统一的 **投资信号块(Investment Signal Block)**。

> ⚠️ **仅供研究参考。** deepalpha 产出的是分析草稿 —— 评分、论点、仓位测算 —— 供你审阅。它**不会**执行交易、转移资金,也不保证收益。最终的买卖决定由你做出。**本工具不构成投资建议。**

---

## 它能做什么

deepalpha 的核心是一个**路由器 + 十一个自包含模块**,运行在一套**一手数据底座**(通过 MCP 接入 SEC EDGAR)之上。每次提问,路由器会把意图归类到一个或多个领域,只运行相关模块,并按「风险优先」的固定顺序执行:

| # | 模块 | 回答的问题 |
|---|------|-----------|
| 1 | **LIQUIDITY 流动性** | 宏观资金面是否安全?(美联储净流动性、SOFR、MOVE、日元套息) |
| 2 | **SENTIMENT 情绪** | 人群/广度是否过热或过冷?(NAAIM、对冲基金杠杆、市场广度、泡沫评分) |
| 3 | **THEME 主题** | 是不是产业链里正确的那一环?(瓶颈/卡脖子环节评分) |
| 4 | **SCREENER 筛选** | 哪些标的通过了筛选?(CANSLIM、VCP、价值-股息、PEAD) |
| 5 | **VALUE 价值** | 这门生意是否稳健且诚信?(ROIC、Piotroski、财务红旗、护城河、股息安全) |
| 6 | **VALUATION 估值** | 相对价格它值多少?(DCF、反向 DCF、可比公司、分部估值 SOTP、合理价区间) |
| 7 | **EARNINGS 财报** | 这个季度财报到底说了什么?(超预期/不及预期、指引、NDR、40 法则) |
| 8 | **FLOW 资金流** | 聪明钱/内部人是否在确认?(13F、超级投资者、Form 4) |
| 9 | **TECHNICAL 技术面** | 图形/时机是否吻合?(趋势模板、广度、派发日、跟随日 FTD、VCP) |
| 10 | **BTC 比特币** | 处在加密周期的什么位置?(MVRV、NUPL、SOPR、资金费率) |
| 11 | **POSITION 仓位** | 结合优势 + 实时组合,该买多少?(Kelly、ATR 止损、敞口上限) |

针对单只标的的问题,还会织入一层 **research-extras 证据层**(分析师目标价、晨星/大行/Seeking Alpha 研究、investing-master 综合评分,以及 QGpro 成长质量评分)。

每次分析最后都会给出一个带颜色编码的 **投资信号块**(信号 · 信心 · 周期 · 评分 · 操作 · 信念强度),让结论保持一致、可比较。

---

## 为什么它更准确

deepalpha 优先采用**一手 SEC 数据,而非网页抓取**。对任何美股公司的基本面、申报文件、持仓或内部人数据,它都会**先调用 SEC EDGAR MCP**(免费、无需 key),只有在 SEC 拿不到的数据(实时价格、分析师目标价、情绪调查、新闻)时才回退到网页搜索 —— 且都会标注日期。如果没有接入 SEC MCP,它会明确说明、回退到网页,并提示「基本面为抓取所得,非一手数据」。它绝不会编造申报文件中的数据。

---

## 仓库结构

```
deepalpha/
├── SKILL.md                  # 路由器 —— Claude 首先加载这个文件
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件(中文说明)
├── MERGE_NOTES.md            # 本 skill 如何由多个源项目合并而来
├── CREDITS.md                # 完整来源署名 + 许可证
├── LICENSE                   # MIT
├── references/               # 每个模块一份 markdown 框架,按需加载
│   ├── data-layer.md         # 工具目录 + 回退阶梯(需要数据时首先加载)
│   ├── liquidity.md  sentiment.md  value.md  valuation.md  earnings.md
│   ├── technical.md  flow.md  theme.md  screener.md  btc.md  position.md
│   ├── research-extras.md  investing-philosophies.md  bias-checklist.md
│   ├── output-formats.md  dashboard.md  index-glossary.md
│   └── serenity/             # 产业链方法论的权威文档
├── scripts/                  # 内置的确定性计算引擎(Python)
│   ├── position_sizer.py     # Kelly / ATR / 固定比例 仓位
│   ├── serenity_scorecard.py # 产业链瓶颈评分
│   ├── screener_vcp/  screener_canslim/
│   ├── earnings_pead/  earnings_trade/
│   ├── technical_breadth/  technical_market_top/  technical_ftd/
│   ├── technical_macro_regime/  technical_uptrend/
│   ├── theme_detector/  flow_institutional/
│   └── README.md             # 哪个引擎对应哪个模块
└── assets/                   # 评分卡 JSON、研究提示词包、论点模板
```

运行时只有 `SKILL.md` 及它按需拉取的 `references/` 会进入 Claude 的上下文 —— `scripts/` 用于确定性评分,而 README / MERGE_NOTES / CREDITS 是给人看的。

---

## 安装

### 作为 Claude skill 安装(推荐)

把整个 `deepalpha/` 文件夹放进你的 skills 目录即可:

- **Claude Code / Cowork:** 放到你的 skills 文件夹,例如:
  - Windows:`%USERPROFILE%\.claude\skills\deepalpha\`
  - macOS / Linux:`~/.claude/skills/deepalpha/`
- **claude.ai(设置 → Capabilities → Skills):** 把文件夹压缩成 zip 后上传,或上传提供的 `.skill` 压缩包。

安装完成后,直接提问投资相关的问题,这个 skill 就会自动触发。

**从 GitHub 安装的最简方式:**

```bash
# 进入 skills 目录(若不存在先创建)
cd ~/.claude/skills            # Windows PowerShell: cd $HOME\.claude\skills

# 克隆仓库
git clone https://github.com/Seanyim/deepalpha.git
```

> Windows 提示:如果 git 报「The directory name is invalid」,说明你处在受限的沙箱路径下。先 `cd $HOME` 切换到普通目录,再执行 clone。

### 数据底座(可选,但显著提升准确度)

deepalpha 在纯网页模式下也能用,但接入 SEC MCP 后准确度会大幅提升。**免费、无需 key** 的方案(Python,`edgartools`):

```jsonc
{
  "mcpServers": {
    "edgartools": {
      "command": "uvx",
      "args": ["--from", "edgartools[ai]", "edgartools-mcp"],
      "env": { "EDGAR_IDENTITY": "你的名字 your@email.com" }
    }
  }
}
```

其他选择:`cyanheads/secedgar-mcp`(TypeScript,需设置 `EDGAR_USER_AGENT`),或零配置的 `npx -y stockscope-mcp`。Notion 连接器(POSITION 模块的实时组合)和 Crypto.com 连接器(BTC)是可选的附加项。

---

## 使用示例

| 你问 | 触发的模块 |
|------|-----------|
| “要不要加仓 NVDA?” | 情绪 → 价值 → 估值 → 仓位 |
| “现在市场有风险吗?” | 流动性 → 情绪 → 技术面(广度) |
| “CRWD 这个季度财报怎么样?” | 财报 |
| “AI 电力产业链里我该研究哪一环?” | 主题 → 筛选 → 价值 |
| “谁在吸筹这只票?” | 资金流(13F + 内部人) |
| “这只票我该买多大仓位?” | 仓位(Kelly + 实时组合) |
| “BTC 处在周期什么位置?” | 比特币 → 流动性 |

deepalpha 会匹配你的输入语言(英文 → 英文,中文 → 中文,混合 → 混合)。

---

## 单独运行计算引擎

`scripts/` 下的引擎都是纯 Python,可离线运行,只需你喂入数据:

```bash
python3 scripts/technical_ftd/ftd_calculator.py     # 跟随日(FTD)演示
python3 scripts/position_sizer.py                    # Kelly / ATR 仓位测算
```

完整的「引擎 → 模块」对应表,以及哪些引擎需要实时数据层,见 `scripts/README.md`。

---

## 来源与许可证

deepalpha 融合了多个宽松许可证项目的方法与代码(tradermonty/claude-trading-skills、muxuuu/serenity-skill、yennanliu/InvestSkill、himself65/finance-skills、anthropics/financial-services、OctagonAI/skills、dgunning/edgartools 等)。完整署名与上游许可证见 [`CREDITS.md`](CREDITS.md);合并过程见 [`MERGE_NOTES.md`](MERGE_NOTES.md)。

本仓库以 [MIT 许可证](LICENSE) 发布。内置组件保留各自原始许可证 —— 再分发前请逐一核对上游许可证。

---

## 免责声明

deepalpha 是一个研究辅助工具。它产出的是供你审阅的草稿与分析,**不构成投资建议**,也不会执行交易或转移资金。市场有风险,你需对自己的投资决定负全部责任。在据此行动前,请核实所有数据 —— 尤其是任何来自网页回退的数据。
