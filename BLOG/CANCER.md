# I Built an App to Track My Cancer Treatment. Then It Became Something Bigger.

Last year I was diagnosed with cancer. In between the shock and the treatment plans, I found myself drowning in numbers — blood test results, biomarker levels, medication schedules, daily pain scores, fatigue ratings. My oncologist needed to see trends. I needed to understand what was happening to my body. And no app I tried could handle what I actually needed to track.

Health apps wanted me to log steps and water intake. Spreadsheets worked but were miserable on a phone. What I wanted was dead simple: let me log any number, with any tag, at any time, and then show me what's happening over time. So I built it.

## What Meetrics Actually Does

[![Download Meetrics](https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg)](https://apps.apple.com/us/app/meetrics/id6760925743)

Meetrics is a personal metrics tracker. You define what matters — there are no pre-built categories or onboarding wizards asking about your fitness goals. You just log values with tags.

In my case, my tags look like this:

- `cea` — a cancer biomarker from my blood work
- `ldh` — another cancer biomarker
- `pain` — daily score, 1-10
- `fatigue` — daily score, 1-10
- `wbc` — white blood cell count, an immune system indicator
- `hgb` - hemoglobin, helps get oxygen to cells
- `rbc` - red blood cell count
- `took_medication_x` — yes/no (or how many), logged daily
- `bowel_movements` — on account of it being colorectal cancer
- `water` — water intake, logged daily
- Plus automatic imports from Apple Health: steps, heart rate, sleep

![SCREENSHOT: Feed tab with medical logs](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/IMG_1452.PNG?raw=true)

That's the Feed tab. Tap +, pick a tag, enter a value, done. It takes about three seconds to log something. Over weeks and months, those three-second entries turn into something genuinely useful. You can also backfill data which I did for the available tp me test data.

## Where It Gets Interesting: Analytics

The Analytics tab is where the data starts talking. You can view any tag over time as a line chart, toggle a rolling average to smooth out day-to-day noise, or enable a 2σ filter to strip outliers that would skew the picture.

But the feature that changed how I talk to my oncologist is the **Correlate** tab. You pick any two tags and Meetrics calculates the correlation between them — with an adjustable time lag.

For example, I found a meaningful correlation between my chemo and its side-effects which was surprising because the side-effects did not happen when thee doctors said they would but later.

![SCREENSHOT: tab with pain correlation](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/IMG_401067240146-1.jpeg?raw=true)

I showed this to my oncologist on my phone during an appointment. Instead of me trying to describe "I think the side-effects come much later than you warned," I had a chart that showed exactly that with a max correlation at an 8 day lag. It changed the conversation.

---

Recently, I had positive results on my latest CT scan. All of my tumors had shrunk compared to the previous scan. This is in sharp contrast to my previous scans which either showed stable sizes or even slight growth - despite being on chemo for months. I haven't figured out how to log this yet because the CT scans don't provide tumor UUIDs ;-).

My current mission is to figure out what made this last month different from the previous months. Perhaps it was the slight improvement in my glucose readings (I am also a T1 diabetic). 

![SCREENSHOT: glucose readings 6M](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/IMG_1454.PNG?raw=true)

Although the downward trend looks very weak. In any case I know that I need to keep it lower. Ever since I started chemo, it has seemed to me that keeping my glucose in control has been much more difficult. Although the data shows otherwise (note that I have been on chemo for 5 months and below I'm showing 1Y):

![SCREENSHOT: glucose readings 1Y](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/IMG_651A49EF94C5-1.jpeg?raw=true)

What has ticked up is my walking and this one is a known predictor of cancer survival. Below is my steps for the last 3 months which has an obvious upward trajectory (note that the previous scan was about 6 weeks before the one this week):

![SCREENSHOT: glucose readings](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/IMG_1456.PNG?raw=true)

And the sharp increase in walking is in part due to the weather improving and in part because my puppy was not able to be walked outside until mid February due to vaccine stuff. My puppy was not able to be walked outside until about the time of my previous CT scan. And this past month has been filled with walks.



## Binary (and Discrete Numeric) Tracking and Streaks

For yes/no habits (like medication adherence), Meetrics shows your current streak, your longest streak, and a Bayesian probability estimate of your true success rate. That last one sounds academic, but it's genuinely useful — it tells you whether the probabiliity of some relation along with its uncertainty.

For example, below are the estimates of how Miralax (a laxative - I have colon cancer) affects my bowel movements the next day. It shows us the probability of me having more than 2 bowel movements (BM) in the left image, and the probability of me having at least 1 BM in the right image. What's counter intuitive is that it seems that not having Miralax (miralax = 0) results in more bowel movements. But the reason for that is that diarrhea is a side-effect of one of the chemo's and when that starts I stop taking the miralax. The right image suggests that half a dose of miralax results in highest probability of at least 1 BM - I have no explanation for it being higher than miralax=1 other than there isn't enough data and you can see that in the heatmaps of the Bayesian estimates.

![SCREENSHOT: glucose readings](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/miralax.jpeg?raw=true)

## The AI Analyst

This is the premium feature I'm most proud of. The Analyst tab connects to Claude (Anthropic's AI) and gives it full access to your data. You can ask questions in plain language:

- "What's my average pain level on days I walk more than 5,000 steps?"
- "Have my biomarker levels been trending up or down over the last 3 months?"
- "Is there any correlation between my sleep duration and fatigue the next day?"

It also generates Daily Insight cards each morning — automatic highlights about trends, anomalies, or correlations it's spotted in your data. Tap a card to read more and get suggested follow-up questions.

For me, this turned raw data into something actionable. I didn't have to think about what to look for — the AI surfaced patterns I hadn't considered.

![SCREENSHOT: glucose readings](https://github.com/sergeybok/meetrics-support/blob/main/RESOURCES/IMG_1AE6983255E5-1.jpeg?raw=true)

## It's Not Just for Health

I built Meetrics for cancer tracking, but the app itself knows nothing about cancer. It doesn't know what a CEA level is. It doesn't care. It just tracks numbers, binary values, and text over time and finds patterns.

Since building it, I've seen it can work for completely different use cases:

- **Students** tracking grades, study hours, and test scores to find what study habits actually move the needle
- **Quantified self enthusiasts** logging caffeine intake, mood, productivity, and sleep to find personal correlations
- **Athletes** tracking custom workout metrics that don't fit neatly into existing fitness apps
- **Anyone** who's ever wanted to answer "is X actually affecting Y?" with data instead of gut feeling

The macroeconomics community might appreciate it too — I wrote a [separate post](https://github.com/sergeybok/meetrics-support/blob/main/BLOG/WALKTHRU.md) using Meetrics to visualize the 12-18 month lag between Fed rate changes and unemployment shifts. The Correlate feature with adjustable lag made it trivially easy to find that pattern.

## Why I Made the Analyst Tab Premium

I want to be transparent about this. I'm not working right now — I'm fighting cancer, and treatment is expensive. The core tracking and analytics features are completely free. The AI-powered Analyst tab is a premium feature, and the revenue from it helps me pay my bills while I can't work - also Claude is expensive.

If the free features are all you need, that's genuinely great. The app does a lot without the AI layer. But if you want the conversational analysis and daily insights, the premium tier helps keep me going — both the app and me personally.

## Try It

Meetrics is available on the App Store.

[![Download Meetrics](https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg)](https://apps.apple.com/us/app/meetrics/id6760925743)


If you track anything — health data, habits, grades, finances, workouts, side project metrics — give it a shot. Log a few things for a week, then check the Analytics tab. You might be surprised by what your own data tells you.

I'd love to hear what you end up tracking. And if you have feedback or feature requests, I read every message.


