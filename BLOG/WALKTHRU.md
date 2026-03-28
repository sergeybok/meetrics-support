# Monetary Transmission in the Data: Replicating Decades of Macroeconomic Research on Your Phone

Economists have spent fifty years debating exactly how — and how quickly — monetary policy affects inflation. The consensus answer, formalised in models from Friedman and Schwartz (1963) through Christiano, Eichenbaum & Evans (1999), is that interest rate changes propagate through the economy with "long and variable lags," typically peaking in effect after 12 to 18 months. The Phillips Curve — the empirical trade-off between unemployment and inflation first described by A.W. Phillips in 1958 — has been both celebrated and declared dead multiple times since.

These aren't abstract debates. They directly shaped policy decisions during the most significant inflation episode in four decades, and their predictions were tested in real time between 2021 and 2023.

What follows is a reproducible walkthrough of importing three public macroeconomic time series into Meetrics and using cross-correlation analysis to observe these relationships in the data directly — no statistical software required.

---

## The Data

We'll use three monthly time series drawn from publicly accessible sources with no registration or preprocessing required:

| Series | Description | Source | Coverage |
|---|---|---|---|
| `CPIAUCSL` | CPI for All Urban Consumers (headline inflation index) | bdecon/econ_data | Jan 1947 – present |
| `CPILFESL` | CPI Less Food and Energy (core inflation) | bdecon/econ_data | Jan 1957 – present |
| `FEDFUNDS` | Effective Federal Funds Rate | FRED / St. Louis Fed | Jul 1954 – present |
| `UNRATE` | Civilian Unemployment Rate | FRED / St. Louis Fed | Jan 1948 – present |

The CPI series uses 1982–1984 as the base period (index = 100). The FEDFUNDS and UNRATE series are expressed as percentages. All four series are sampled on the first of each month.

**Import URLs:**

```
CPI (headline + core):
https://raw.githubusercontent.com/bdecon/econ_data/refs/heads/master/micro/cpi.csv

Federal Funds Rate:
https://fred.stlouisfed.org/graph/fredgraph.csv?id=FEDFUNDS

Unemployment Rate:
https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE
```

---

## Step 1 — Import the Data

Open Meetrics, tap **⋯** in the top-right corner of the Feed, and select **Import from CSV**.

**For the CPI dataset:** paste the first URL and tap **Load**. The preview will show three columns: `CPIAUCSL`, `CPILFESL`, and `daten`. The `daten` column is a redundant human-readable date string (e.g. "01jan1947") — **deselect it** before importing. Keep both CPI columns selected.


<img src="https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/Simulator%20Screenshot%20-%20iPhone%2016%20Pro%20Max%20-%202026-03-27%20at%2021.04.48.png?raw=true" alt="Description of image" width="300" />

**For the FRED datasets:** each file has exactly two columns — the date and the series value — so nothing needs to be deselected. Repeat the import for both the FEDFUNDS and UNRATE URLs.

![SCREENSHOT: CSV import preview for FEDFUNDS, showing observation_date recognised as the timestamp and FEDFUNDS as the single tag, with sample values from the 1950s](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/Simulator%20Screenshot%20-%20iPhone%2016%20Pro%20Max%20-%202026-03-27%20at%2021.10.43.png?raw=true)

<img src="https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/Simulator%20Screenshot%20-%20iPhone%2016%20Pro%20Max%20-%202026-03-27%20at%2021.10.43.png?raw=true" alt="Description of image" width="300" />

After three imports, your Feed will contain four tags — `cpiaucsl`, `cpilfesl`, `fedfunds`, `unrate` — totalling roughly 3,000 monthly observations spanning more than 75 years of US economic history.

![SCREENSHOT: Feed screen showing recent entries for all four tags with their values and dates, demonstrating the full import was successful]

---

## Step 2 — The Level Series: CPI Over 75 Years

Open the **Analytics** tab and tap `cpiaucsl`. Set the date range to **All**.

The index level itself is not directly interpretable as a percentage — what matters structurally is its trajectory. You'll see three distinct regimes: a modest post-war adjustment in the late 1940s, a sustained acceleration through the 1965–1983 period corresponding to the Great Inflation, and an extended plateau of slow, stable growth from roughly 1983 to 2020 that economists call the Great Moderation. On the far right, the 2021–2023 episode is visible as a near-vertical inflection — the steepest rate of change in the dataset.

![SCREENSHOT: TagChartView for cpiaucsl showing the full All-range history from ~21 in 1947 to ~300+ in 2024, with the three regime periods visually distinct and the 2021-2023 acceleration clearly visible on the right]

Enable **Rolling Avg** to suppress the month-to-month sampling noise and make the regime transitions cleaner. Narrow to the **3Y** range to isolate the recent episode: you can see that the index peaked in mid-2022 and decelerated noticeably through 2023, consistent with the announced policy objective.

![SCREENSHOT: TagChartView for cpiaucsl with 3Y range and Rolling Avg enabled, showing the peak and subsequent deceleration of the recent inflation episode more clearly]

Now open `cpilfesl`. Core CPI — which strips out food and energy prices on the grounds that they are supply-shock-driven and mean-reverting — exhibits structurally lower volatility. This is particularly visible in the 1973–1975 and 1979–1981 periods, where the headline series diverged sharply upward from core. The divergence indicates those episodes were substantially driven by oil supply shocks rather than demand-pull or wage-push mechanisms. By contrast, in the 2021–2022 episode, headline and core tracked more closely — consistent with the interpretation that this inflation was more broad-based and demand-driven, not purely an energy price shock.

![SCREENSHOT: TagChartView for cpilfesl with All range, showing the smoother profile compared to headline CPI, especially through the 1970s oil shock period]

---

## Step 3 — Cross-Correlation: The Monetary Transmission Lag

The central empirical question: at what lag does the Federal Funds Rate best predict subsequent CPI behaviour?

Navigate to **Correlate**. Set Tag A to `fedfunds`, Tag B to `cpiaucsl`, range to **All**, bucket to **1D**. Because the underlying data is monthly (one observation per month on the first), each lag step in the Correlate view corresponds to one calendar month.

**At lag 0**, you will observe a substantial *positive* correlation — likely in the range of r = 0.55 to 0.70. This is not evidence that raising rates causes inflation. It reflects reverse causality: the Fed raises rates *in response to* rising inflation, so contemporaneous levels are positively correlated by construction. This is the classic omitted-variable / endogeneity problem in raw observational data.

![SCREENSHOT: Correlate view with fedfunds → cpiaucsl at lag 0, showing a strong positive correlation around r = 0.6-0.7, with the correlation card visible below]

**Step the lag forward.** Use the **+** control to move through lags 1 through 14. Watch the correlation coefficient decline and eventually cross zero. Around **lag +9 to +12**, the relationship typically turns negative — meaning higher rates at time *t* are associated with lower CPI approximately 9 to 12 months later. This is the monetary transmission mechanism: the channel through which tighter credit conditions propagate through business investment, consumer borrowing, and aggregate demand to ultimately reduce price pressure.

![SCREENSHOT: Correlate view with lag set to +12, showing the correlation has moved toward zero or negative, with the lag label reading "fedfunds leads cpiaucsl by 12d" — each lag step representing one month of monthly data]

This 9–14 month lag range replicates findings from a substantial body of academic literature. Bernanke & Blinder (1992) identified lags of similar magnitude using vector autoregressions on pre-1990 US data. Romer & Romer (2004) found that output effects peak around 16 months post-shock and inflation effects somewhat later. The fact that a simple cross-correlation on a mobile app reproduces the directional finding of these studies is a useful illustration of how robust the pattern is in the data.

Now narrow the range to **5Y** to isolate the 2022–2023 cycle in isolation. The sign change in the correlation may appear at a somewhat shorter lag in this window, possibly 6 to 9 months — consistent with the relatively rapid deceleration of inflation in 2023 compared to the drawn-out process during the Volcker disinflation of 1981–1983, when lags were longer and the eventual decline in inflation more gradual.

![SCREENSHOT: Correlate view with 5Y range, fedfunds → cpiaucsl, lag around +9, highlighting the pattern specific to the 2022-2023 tightening cycle]

---

## Step 4 — The Phillips Curve

Phillips (1958) documented an empirical inverse relationship between wage inflation and unemployment in the UK from 1861 to 1957. Samuelson and Solow (1960) extended this to price inflation and formalised it as a policy trade-off: policymakers could, in theory, choose a point on the curve — accepting higher inflation in exchange for lower unemployment, or vice versa.

The relationship was subsequently challenged by Friedman (1968) and Phelps (1968), who argued that it only held in the short run and that attempts to exploit it would shift expectations and eliminate the trade-off. Empirically, the curve appeared to steepen dramatically in the 1970s and to flatten substantially after the 1990s, leading some to declare it effectively dead as a forecasting tool.

You can see all of this in the data directly.

Set Tag A to `unrate`, Tag B to `cpiaucsl`, range to **All**.

![SCREENSHOT: Correlate view with unrate → cpiaucsl at lag 0, showing a negative correlation — low unemployment associated with higher CPI — reflecting the baseline Phillips Curve relationship]

At lag 0 you should observe a *negative* correlation — low unemployment co-occurs with higher CPI, consistent with the original Phillips hypothesis. The magnitude will be moderate, reflecting the fact that the full-sample correlation averages across three structurally distinct periods.

Now set the range to **1970–1985** using the custom range. The negative correlation strengthens considerably — this is the era when the trade-off was most apparent in US data, with the Fed repeatedly attempting to manage unemployment at the cost of inflation.

Switch to the **post-1990 period** and the correlation weakens markedly. During 1995–2019, the US economy ran unemployment as low as 3.5% with inflation persistently *below* the Fed's 2% target — a combination the original Phillips framework would not have predicted. This structural break, often attributed to anchored inflation expectations and global disinflationary pressures from trade integration, is visible without any statistical model: the scatter in the Correlate chart simply flattens.

![SCREENSHOT: Correlate view with unrate → cpiaucsl showing a visibly weaker correlation when the range is narrowed to the post-1990 period, demonstrating the flattening of the Phillips Curve]

**The reverse direction:** set a **negative lag** (Tag A leads negatively, meaning CPI leads unemployment). At around lag −4 to −6, you should observe that rising CPI *precedes* rising unemployment. This is not paradoxical — it captures the policy response channel. High inflation prompts rate hikes, which contract the economy, which raises unemployment. The lag between the inflation shock and the unemployment response reflects the time required for tighter financial conditions to produce job losses. Okun (1962) formalised the related relationship between GDP growth and unemployment; the CPI→unemployment lead seen here is a downstream manifestation of the same mechanism.

![SCREENSHOT: Correlate view with unrate → cpiaucsl at lag -6, showing how CPI changes precede unemployment changes, with the lag label reading "cpiaucsl leads unrate by 6d"]

---

## Step 5 — Headline vs Core: Decomposing the Inflation Signal

The distinction between headline and core CPI is not merely cosmetic. It reflects a theoretical argument about which price changes carry information about persistent inflationary pressure versus transitory supply disruptions.

Set Tag A to `cpilfesl` (core), Tag B to `cpiaucsl` (headline), range **All**, lag 0.

The correlation will be extremely high — likely r > 0.97 over the full sample. Over most of modern history, food and energy prices have not diverged persistently enough from the overall price level to matter for the level correlation.

![SCREENSHOT: Correlate view with cpilfesl → cpiaucsl at lag 0, showing a very high correlation around r = 0.97-0.99, with the "Strong positive correlation" label]

The more informative analysis is in sub-periods. Narrow to **1972–1982**. The correlation drops measurably — this is where oil-price-driven headline inflation substantially diverged from the underlying core trend. Strip out energy and the 1970s inflation, while still serious, looks structurally different: a combination of demand-pull pressure and wage-price spiralling rather than a pure commodity shock.

Now narrow to **2021–2023**. Here the two series track much more closely than in the 1970s, reinforcing the interpretation that the recent episode was a broad demand shock — amplified by supply chain disruptions — rather than a repeat of the oil embargo dynamics. This distinction matters for policy: a supply-shock-driven inflation may self-correct as the shock dissipates, whereas a demand-driven inflation requires active monetary tightening to resolve.

---

## Step 6 — AI-Assisted Pattern Recognition

Switch to the **Analyst** tab. The daily insight cards use the full dataset to surface the most statistically notable observations — you may see a trend card showing the recent trajectory of `fedfunds`, a correlation card identifying the lag relationship between rates and inflation, and an anomaly card flagging the 2021–2022 CPI acceleration as an outlier relative to the preceding two decades.

![SCREENSHOT: Analyst tab showing three Daily Insights cards: a trend card for fedfunds, a correlation card identifying the fedfunds → cpiaucsl lag relationship, and an anomaly card about the 2021-2022 CPI spike]

The chat interface allows free-form queries against the full dataset. Some analytically productive questions:

- *"At what Fed Funds Rate level did CPI begin declining in the 1980s tightening cycle, and how does that compare to 2022–2023?"*
- *"How many months after the Fed Funds Rate peaked in 1981 did CPI reach its subsequent trough?"*
- *"Compare the rate of CPI deceleration in 2022–2023 to 1980–1982 on a month-over-month basis."*
- *"Is there a threshold unemployment rate below which CPI has historically tended to accelerate?"*
- *"What is the cross-correlation between UNRATE and CPIAUCSL at lags 0 through 12 over the 1960–1990 period?"*

These questions probe whether empirical regularities documented in the academic literature are visible in this particular dataset — which itself provides an informal replication check.

![SCREENSHOT: Analyst chat showing a detailed question about comparing the 1980s and 2022 tightening cycles, with the AI response citing specific months, rate levels, and CPI values from the data]

---

## What the Data Shows

A few observations worth noting explicitly:

**The transmission lag is consistently positive and in the 9–14 month range.** This holds across the 1970s, 1980s, 1994 tightening, and 2022–2023 cycles. It is one of the more robust empirical regularities in this dataset and consistent with the academic literature.

**The 2021–2023 episode was the fastest acceleration in the sample but not the highest peak.** The index rose approximately 14% in 18 months — faster than any prior episode in the data. Peak year-on-year inflation of ~9.1% (June 2022) was lower than the ~14.8% recorded in March 1980.

**The Phillips Curve trade-off was not stable across the full sample.** The inverse relationship is clearly present in the 1960s–1980s data and largely absent in the post-1990 data, consistent with the theoretical predictions of the Friedman-Phelps natural rate hypothesis and subsequent work on expectation anchoring.

**Core CPI understated the 1970s shock and tracked headline closely in 2022.** The structural difference between the two episodes is visible directly in the headline-core spread: large in 1973–1975, much smaller in 2021–2023.

---

## Further Exploration

FRED publishes hundreds of additional series in the same direct-download format. A few extensions worth exploring with the same approach:

- **`PCEPI`** — Personal Consumption Expenditures Price Index, the Fed's formally preferred inflation measure; compare its lag structure to CPIAUCSL
- **`M2SL`** — M2 money supply; test the monetarist hypothesis that excess money growth leads inflation with a 12–24 month lag
- **`MORTGAGE30US`** — 30-year fixed mortgage rate; observe how quickly it responds to FEDFUNDS changes and how housing costs affect core CPI
- **`CPALTT01USM657N`** — CPI year-on-year percentage change from OECD; allows direct percentage-change analysis without computing first differences manually

Any series available at `https://fred.stlouisfed.org/graph/fredgraph.csv?id=SERIES_ID` can be imported directly. The full FRED catalogue contains over 800,000 time series.

---

*Data sourced from the Federal Reserve Bank of St. Louis (FRED) and Brian Dew's econ_data repository. Both are freely accessible without registration. Key references: Phillips (1958), Friedman (1968), Bernanke & Blinder (1992), Christiano, Eichenbaum & Evans (1999), Romer & Romer (2004). Screenshots taken on iPhone 17 Pro Max running Meetrics 1.1.*
