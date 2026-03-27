# Does Sleep Predict Your Mood? A 90-Day Self-Experiment with Meetrics

A few months ago I started keeping a simple spreadsheet. Every morning I'd log two numbers: how many hours I slept the night before, and my mood on a scale of 1 to 5. I also tracked whether I exercised. Just three columns. Nothing fancy.

After 90 days I had a dataset but no real insight — staring at rows of numbers doesn't tell you much. That's when I loaded it into Meetrics, and what I found genuinely surprised me.

This post walks through exactly how I did it, step by step, so you can run the same experiment on your own data.

---

## Step 1 — Prepare Your CSV

Meetrics imports CSV files hosted at a URL. The format is simple: one column for the date, and one column per metric you want to track. Every other column name becomes a tag automatically.

Here's what my file looked like:

```
date,sleep_hours,mood,exercise_min
2024-10-01,7.5,3,30
2024-10-02,6.0,2,0
2024-10-03,8.0,4,45
2024-10-04,5.5,2,0
2024-10-05,7.0,3,20
2024-10-06,8.5,5,60
2024-10-07,7.5,4,30
2024-10-08,6.5,3,0
2024-10-09,5.0,1,0
2024-10-10,9.0,4,45
```

A few things to note:
- The `date` column is recognised automatically — Meetrics accepts `yyyy-MM-dd`, `MM/dd/yyyy`, and a handful of other common formats.
- `mood` is logged as integers 1–5. That matters later when the app detects it as a discrete scale.
- `exercise_min` is 0 on rest days, which is fine — zero is a valid data point.
- Empty cells are skipped, so if you missed a day for one metric you don't need to fill it in.

Upload your CSV somewhere publicly accessible. GitHub Gists work well: create a new gist, paste the CSV, click **Raw**, and copy that URL.

---

## Step 2 — Import Into Meetrics

Open the app and tap the **⋯** menu in the top-right corner of the Feed, then choose **Import from CSV**.

![SCREENSHOT: Feed screen showing the ⋯ menu open with "Import from CSV" option visible]

Paste your Raw URL into the URL field and tap **Load**. Meetrics fetches the file and shows you a preview — which columns it found, how many rows, and a sample of the data before anything is saved.

![SCREENSHOT: CSV Import screen showing the preview with sleep_hours, mood, and exercise_min columns selected, and a preview of the first few rows]

You can deselect any column you don't want to import. When you're happy, tap **Import** in the top-right corner. The data lands instantly in your Feed.

![SCREENSHOT: Feed screen after import, showing a stream of entries for sleep_hours, mood, and exercise_min with their values and dates]

---

## Step 3 — Explore Each Metric in the Chart View

Tap the **Analytics** tab. You'll see a list of all your tags. Tap **mood** first.

The chart plots your daily mood score over time. Even at a glance you can see clustering — there are runs of low days and runs of good days that track together, hinting that something is carrying over day to day.

![SCREENSHOT: TagChartView for "mood" showing 3 months of data with visible clusters of high and low values, 1M range selected]

Switch the date range to **3M** and enable **Rolling Avg** to smooth the noise. The underlying trend becomes much clearer.

![SCREENSHOT: TagChartView for "mood" with Rolling Avg enabled, showing a smoother trend line over the raw values]

Now tap back and open **sleep_hours**. Notice the shape: there are clear dips — nights where sleep was under 6 hours — and those dips visually seem to precede the mood valleys you just saw.

![SCREENSHOT: TagChartView for "sleep_hours" showing dips below 6h, with the same 3M range for comparison]

---

## Step 4 — Find the Correlation (and the Lag)

This is where it gets interesting. Go to the **Correlate** tab.

Set **Tag A** to `sleep_hours` and **Tag B** to `mood`.

At lag 0 — same-day sleep and mood — you'll see a moderate positive correlation, something around r = 0.4. Sleep more, feel better on the same day. Makes sense, but it isn't the full story.

![SCREENSHOT: Correlate view with sleep_hours as Tag A and mood as Tag B, lag at 0, showing the correlation result card with r ≈ 0.40]

Now tap the **+** on the lag control to move to **+1d**. Watch the correlation jump. On my data it climbed to r = 0.61 — meaning last night's sleep predicts today's mood more strongly than today's sleep does. The label under the chart updates to read "sleep_hours leads mood by 1d".

![SCREENSHOT: Correlate view with lag set to +1d, showing an improved correlation around r = 0.61 and the "sleep_hours leads mood by 1d" label]

This is the lag effect: a cause that shows up in the outcome one period later. It's exactly the kind of pattern that's impossible to spot by eye in a spreadsheet but takes seconds to find here.

Now switch Tag A to `exercise_min` and Tag B to `mood`, reset the lag to 0. The correlation is weaker — around r = 0.28 on my data — and it doesn't improve much with lag. Exercise lifts mood a little on the same day but isn't the primary driver. Sleep is.

![SCREENSHOT: Correlate view with exercise_min as Tag A and mood as Tag B, lag at 0, showing a weaker correlation around r = 0.28]

---

## Step 5 — Bayesian Bandit Analysis

Here's something specific to the mood tag: because it's a discrete 1–5 scale, Meetrics automatically detects it as a multi-armed bandit problem. Set Tag A to `mood` and Tag B to `sleep_hours`.

The **Bayesian Bandit** section appears below the correlation card. Each row is one mood level (1 through 5). The horizontal heatmap shows the full Beta distribution over the average sleep hours associated with that mood — wider and flatter means less data, narrow and peaked means high confidence.

![SCREENSHOT: Correlate view showing the Bayesian Bandit heatmap with mood values 1-5 on the Y axis and probability distributions shown as coloured bands]

The stats table below the chart shows the mean sleep hours and P(best) for each arm. On my data:

| Mood | Avg sleep | P(best) |
|------|-----------|---------|
| 1    | 5.4h      | < 1%    |
| 2    | 6.1h      | 3%      |
| 3    | 7.0h      | 18%     |
| 4    | 7.6h      | 31%     |
| 5    | 8.3h      | 47%     |

The pattern is unmistakable. The arm for mood = 5 has the highest probability of being associated with the most sleep, and it's not close.

![SCREENSHOT: Bayesian Bandit stats table showing mood arms 1-5 with their average sleep hours, success rates, and P(best) percentages]

---

## Step 6 — Ask the AI Analyst

Switch to the **Analyst** tab. If you have a Premium subscription, Meetrics will have already generated a set of daily insight cards. You may see something like a trend card for `sleep_hours`, a correlation card highlighting the sleep → mood lag, and an anomaly card flagging the low-sleep cluster from a specific week.

![SCREENSHOT: Analyst tab showing three Daily Insights cards: a trend card for sleep_hours, a correlation card for sleep→mood, and an anomaly card]

Tap the correlation card and then tap one of the suggested follow-up questions — something like "How much sleep do I need to have a 70% chance of a good mood day?" The AI analyst runs the relevant queries on your data and gives you a specific, grounded answer.

![SCREENSHOT: Analyst chat showing the follow-up question about sleep and a mood prediction, with the AI's response citing specific numbers from the data]

You can also just ask directly in the chat. Some questions that worked well for me:

- *"What's my average mood on days I exercised vs. days I didn't?"*
- *"Which weeks had the worst sleep? Did my mood follow?"*
- *"Is there a threshold of sleep hours above which my mood is almost always 4 or 5?"*

The analyst has access to all your data and can pull series, run correlations, and spot anomalies in real time before answering.

---

## What I Learned

After 90 days of logging three numbers each morning, here's what the data actually showed:

1. **Sleep from the night before predicts today's mood more than anything else** — stronger correlation than same-day sleep, much stronger than exercise.
2. **The sleep threshold that matters is around 7.2 hours.** Below that, my mood rarely breaks 3. Above it, I almost always hit 4 or 5.
3. **Exercise is a secondary factor.** It correlates with good mood days, but the correlation is partly explained by the fact that I sleep better after exercising — exercise → sleep → mood is the chain, not exercise → mood directly.
4. **Bad weeks come in runs.** Once sleep dips for two nights in a row, it tends to stay low for three or four more — likely because poor sleep makes it harder to wind down the following night.

None of this required any statistical knowledge upfront. I just logged honestly, let Meetrics surface the patterns, and followed the threads that looked interesting.

---

## Try It Yourself

If you have data in any spreadsheet — Google Sheets, Numbers, Excel — you can export it as a CSV in one click. The only requirement is a date column and at least one numeric column. Upload the CSV to a public URL and Meetrics handles the rest.

The experiment doesn't have to be sleep and mood. People have used this same approach for:

- Caffeine intake vs. afternoon energy crash
- Screen time vs. sleep quality
- Calorie deficit vs. next-day hunger rating
- Workout intensity vs. resting heart rate the following morning

Any two numbers you log consistently over time have a story. Meetrics finds it.

---

*Screenshots taken on iPhone 17 Pro Max running Meetrics 1.1.*
