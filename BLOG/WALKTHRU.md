# The Soft Landing That Wasn't Supposed to Happen: Replicating decades of Macro-Econ research on your phone

There is a pattern in American economic history so consistent it has the status of a law. The Federal Reserve raises interest rates. A recession follows. Unemployment spikes. The Fed cuts rates. Repeat.

It happened after 1969. After 1973. After 1979. After 1989. After 2000. After 2006. In each case, the Fed tightened policy, and somewhere between 12 and 24 months later, the labour market broke. The mechanism varies in its details — sometimes it's housing, sometimes credit markets, sometimes business investment — but the outcome is remarkably consistent. Hiking rates is, historically, how recessions are made.

So when the Fed raised rates eleven times between March 2022 and July 2023 — the most aggressive tightening cycle in forty years — economists made predictions. Some said 2 million jobs lost. Others said 4 million. Almost no mainstream forecast had unemployment staying below 4.5%. The soft landing, the scenario where the Fed successfully cools an overheated economy without triggering a recession, was considered the rarest outcome in macroeconomics. It had essentially happened once in the post-war period, in 1994–1995, and even that is contested.

And yet here we are.

What follows is a walkthrough of importing the raw Fed and unemployment data into Meetrics and seeing that history — and its anomalous recent chapter — with your own eyes.

---

## The Data

Two series. That's all you need.

| Series | Description | Source | Coverage |
|---|---|---|---|
| `FEDFUNDS` | Effective Federal Funds Rate | FRED / St. Louis Fed | Jul 1954 – present |
| `UNRATE` | Civilian Unemployment Rate | FRED / St. Louis Fed | Jan 1948 – present |

The Fed Funds Rate is the interest rate at which banks lend reserves to each other overnight. It is the primary lever the Federal Reserve pulls to slow or accelerate the economy — when the Fed "raises rates," this is what they're raising. UNRATE is the monthly unemployment rate from the Bureau of Labor Statistics. Together, these two numbers, updated monthly, tell most of the story of American economic management over the past seventy years.

**Import URLs:**

```
Federal Funds Rate:
https://fred.stlouisfed.org/graph/fredgraph.csv?id=FEDFUNDS

Unemployment Rate:
https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE
```

---

## Step 1 — Import the Data

Open Meetrics, tap **⋯** in the top-right corner of the Feed, and select **Import from CSV**.

Each FRED file has exactly two columns — the date and the series value. Nothing needs to be deselected. Paste the FEDFUNDS URL, tap **Load**, then **Import**. Repeat for UNRATE.

![SCREENSHOT: CSV import preview for FEDFUNDS, showing observation_date as the timestamp and FEDFUNDS as the single selected tag, with a sample of rows from the 1950s-60s](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/IMG_F6F4AA34C056-1.jpeg?raw=true)

After two imports, your Feed will contain both tags. Combined, you have roughly 1,700 monthly observations — every interest rate decision and every unemployment reading since the Eisenhower administration.

![SCREENSHOT: Feed screen showing recent entries for both fedfunds and unrate, with current values visible alongside recent historical readings](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/Simulator%20Screenshot%20-%20iPhone%2016%20Pro%20Max%20-%202026-03-27%20at%2021.10.43.png?raw=true)

---

## Step 2 — The Shape of Economic History

Open the **Analytics** tab. Tap `fedfunds` and set the range to **All**.

Take a moment with this chart. What you're looking at is a complete record of how aggressively the United States has tried to manage its economy through monetary policy. The shape is not random. There's a 25-year mountain — rates rising through the 1960s and 1970s, peaking at nearly 20% in 1981, then declining almost continuously for four decades until they hit zero in 2008 and stayed there. Then a modest rise, then zero again in 2020, then the sharpest spike since that 1981 peak.

![SCREENSHOT: TagChartView for fedfunds with All range, showing the full arc from ~1% in the 1950s up to the ~20% peak in 1981, the long downward slope through 2008, the near-zero era, and the sharp 2022-2023 rise](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/Simulator2.png?raw=true)

Enable **Rolling Avg** to smooth out month-to-month noise. The three-decade downward trend from 1981 to 2021 — what economists sometimes call the "great rate decline" — becomes unmistakable. Every tightening cycle during this period was smaller than the last. The 1984 peak was lower than 1981. The 1989 peak was lower than 1984. And so on. By the time the Fed got to 2006, the "tight" level was 5.25% — a rate that would have been considered accommodative in 1975.

Now tap `unrate` and set it to **All**.

![SCREENSHOT: TagChartView for unrate with All range, showing unemployment's historical peaks and valleys — the 10.8% peak in 1982, the 9.9% peak in 2009, and the historic lows of 3.5-3.7% in 2019-2020 and again in 2022-2023](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/Simulator3.png?raw=true)

The unemployment chart looks like a seismograph. The tall spikes are recessions — and if you already have the FEDFUNDS chart memorised, you can start to see the pattern. Every significant spike in unemployment is preceded by a significant rise in the Fed Funds Rate. The 1982 spike to nearly 11% came after rates hit 20%. The 2009 spike to nearly 10% came after rates rose from 1% to 5.25% between 2004 and 2006. The timing isn't coincidental. It's the mechanism.

---

## Step 3 — The Lag: How Long Does the Damage Take?

The Fed doesn't raise rates and immediately throw people out of work. The economy isn't that responsive. What happens is a chain: higher rates raise borrowing costs, which slow business investment and consumer spending, which reduces demand for labour, which eventually shows up in the unemployment numbers. This takes time.

Navigate to **Correlate**. Set Tag A to `fedfunds`, Tag B to `unrate`, range to **All**, bucket to **1 Month**.

At **lag 0**, the correlation is around 0. This looks paradoxical. Shouldn't higher rates mean higher unemployment? But remember: the Fed also *cuts* rates when unemployment is already high. So in the raw contemporaneous data, high unemployment and high rates appear together (late-cycle tightening), and low unemployment and low rates appear together (accommodative post-crisis policy). The cause and effect are tangled.

Now step the lag forward using the **+** control. This is where it gets interesting.

As you move through lags 6 through 18, watch the correlation coefficient. It will start increasing. Around **lag +12 to +18**, it typically reaches its highest point — meaning the Fed's rate at time *t* is most strongly associated with unemployment approximately 12 to 18 months later. Conclusion: higher rates today predict *higher* unemployment next year.

![SCREENSHOT: Correlate view with fedfunds → unrate at different lags"](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/combined.png?raw=true)

Twelve to eighteen months. That's how long it takes for a rate hike to show up as jobs lost. This lag is one of the most consistent empirical findings in monetary economics — it appears in academic research going back to Friedman's 1961 paper on the lag in monetary policy effects, and you're reproducing it from a phone with two public datasets and a cross-correlation function.

---

## Step 4 — A Tour of Hard Landings

The history of Fed tightening cycles is largely a history of recessions. Let's look at a few.

**The Volcker Shock (1979–1983)**

Narrow both the range and context to the early 1980s in Analytics. Paul Volcker became Fed Chair in August 1979 with one mandate: kill inflation, no matter the cost. He raised the Fed Funds Rate to 17.6% by April 1980, briefly cut during a recession, then raised it again to an extraordinary 19.1% in July 1981.

In the Correlate view, isolate **1979–1984** and step through lags on `fedfunds` → `unrate`. The relationship is brutal and clean: unemployment rose from around 6% in 1979 to 10.8% in December 1982 — the highest level since the Great Depression. About 3 million people lost their jobs. Volcker's policy worked — inflation collapsed — but the human cost was enormous and the lag between cause and effect was textbook: roughly 12 to 15 months from the peak in rates to the peak in unemployment.

![SCREENSHOT: TagChartView for unrate narrowed to 1979-1984, showing the dramatic rise to 10.8% and the chart for fedfunds on the All view with the 1981 spike clearly visible as the preceding cause](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/Simulator4.png?raw=true)

**The Greenspan Hikes (1994–1995)**

This one is the exception that proves the rule. Alan Greenspan raised rates from 3% to 6% in twelve months — a pace that, at the time, seemed aggressive — while the economy was still recovering from the 1990–91 recession. Unemployment was at 6.1% when he started and fell to 5.5% by the time he was done.

Narrow to **1994–1997**. The unemployment rate kept *falling* throughout the tightening cycle. No recession followed. This is the famous soft landing — the one time in the modern era when the Fed raised rates and the labour market shrugged. Economists have debated why ever since. Luck, timing, the unique productivity boom of the early internet era, global disinflationary tailwinds — all have been proposed. The data is silent on the mechanism. It just shows the anomaly.

![SCREENSHOT: Correlate view with fedfunds → unrate narrowed to 1994-1997, showing a weak or positive correlation — unusually, higher rates did not predict rising unemployment during this cycle](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/Simulator5.png?raw=true)

**The 2004–2006 Cycle and What Followed**

Narrow to **2004–2009**. The Fed raised rates seventeen times over two years, from 1% to 5.25%. Unemployment at the time was falling and stayed low through 2007. It seemed, for a while, like another soft landing.

It wasn't. The lag was just longer. The rate hikes had inflated a credit bubble in housing markets — the mechanism was not direct labour market suppression but financial system stress. When the bubble burst, unemployment didn't just rise. It nearly doubled in 18 months, from 4.4% in May 2007 to 9.9% in November 2009. The lag between the tightening and the unemployment damage was unusually long — almost three years — because the channel ran through finance rather than directly through business investment. But it arrived.

![SCREENSHOT: TagChartView for unrate narrowed to 2004-2010, showing the deceptively flat unemployment from 2004-2007 followed by the rapid rise to nearly 10% — illustrating how the delayed lag from the 2004-2006 rate hikes eventually materialized](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/Simulator6.png?raw=true)

---

## Step 5 — The Anomaly: 2022–2024

Now look at the most recent cycle.

Set to **2022-2024**. The chart shows eleven rate hikes in sixteen months — from 0.08% in February 2022 to 5.33% by July 2023. In raw speed and magnitude, this is the most aggressive tightening since Volcker. The Fed moved faster than it had in four decades.

![SCREENSHOT: TagChartView for fedfunds with 2Y range, showing the near-vertical rise from near zero in early 2022 to above 5% by mid-2023 — the steepest rate of increase visible in the recent portion of the chart](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/Simulator7.png?raw=true)

Unemployment barely moved. It started the tightening cycle around 3.8%, dipped to 3.4% at its lowest, and even after the most aggressive rate hike campaign in a generation had fully run its course, remained below 4%. Apply the 12–18 month lag you measured earlier: by late 2023 and into 2024, the unemployment consequences of the 2022 hikes should have been visible. They largely weren't.

In  the Correlate view set **2022–present** and bucket of **1 Month**, and step through lags +6 through +18. The correlation is quite strong but that is due to low variance in the unemployment rate. If you expand the window to **2021-present** the correlation in the 6 month window disappears.

![SCREENSHOT: Correlate view with fedfunds → unrate narrowed to 2022-present, showing a weak or near-zero correlation at lags +12 to +18, a striking departure from the historical pattern visible in the full-sample analysis](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/Simulator8.png?raw=true)

---


## What the Numbers Say (And What They Don't)

A few things stand out from this analysis.

**The 12–18 month lag is one of the most consistent patterns in the dataset.** Across different Fed Chairs, different economic conditions, different inflation regimes, and different starting levels of unemployment, the cross-correlation between the Fed Funds Rate and subsequent unemployment peaks in roughly the same window. This is not a statistical abstraction — it is the fingerprint of a real mechanism operating through real decisions made by real businesses and consumers in response to credit costs.

**There have been two genuine soft landings in the data, and one contested near-miss.** The 1994–1995 cycle produced no recession. The most recent cycle, by early measures, appears to be the second. Every other significant tightening cycle in the dataset ended in a recession with meaningful unemployment increases. Two out of ten is not a reliable blueprint.

**The post-2008 zero lower bound era is historically unprecedented.** From December 2008 to December 2015, the Fed Funds Rate sat at 0.00–0.25% — the longest period of near-zero rates in the dataset's history. Unemployment gradually fell from 9.9% to 5.0% over those seven years. The recovery was the slowest of any post-war recession. Whether the zero lower bound constrained the Fed's ability to accelerate that recovery, or whether structural factors were responsible, is a question that remains genuinely open.

**The 2022–2023 cycle is the most interesting data point in recent economic history.** Whether it represents a permanent change in how the economy responds to rate hikes — or whether the unemployment effect is simply delayed, or operating through channels not visible in these two series — is the question that macroeconomists are currently arguing about. The data lets you see the anomaly. It does not tell you why.

---

## Try These Extensions

FRED publishes hundreds of additional series in the same direct-download format. A few that would extend this analysis naturally:

- **`NROU`** — The CBO's time-varying estimate of the natural rate of unemployment; compare this to UNRATE to see how close the economy has run to its estimated full-employment level across different eras
- **`MORTGAGE30US`** — 30-year fixed mortgage rate; observe how directly and quickly it mirrors Fed Funds Rate movements, and whether the 2022–2023 mortgage shock was comparable to prior tightening cycles
- **`PAYEMS`** — Total nonfarm payroll employment; a more granular look at job creation than UNRATE, and more sensitive to the leading edge of economic slowdowns
- **`JTSJOL`** — Job openings from the JOLTS survey; a key indicator for the "soft landing" debate, since the 2022–2023 cycle saw job openings fall substantially without unemployment rising — a pattern unlike any prior cycle

Any series available at `https://fred.stlouisfed.org/graph/fredgraph.csv?id=SERIES_ID` can be imported directly. The full FRED catalogue contains over 800,000 time series.

---

*Data sourced from the Federal Reserve Bank of St. Louis (FRED). Freely accessible without registration. Key references: Friedman (1961), Bernanke & Blinder (1992), Romer & Romer (2004). Screenshots taken on iPhone 17 Pro Max running Meetrics 1.1.*
