# Meetrics – Support

**Contact:** sergeybokhnyak@icloud.com

For bug reports, feature requests, or general questions, email the address above and I'll get back to you as soon as possible.

[![Download Meetrics](https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg)](https://apps.apple.com/us/app/meetrics/id6760925743) 

---

## Frequently Asked Questions

**How do I add a data point?**
Tap the **+** button on the Feed tab. Choose a tag name, type (Number, Binary, or Text), enter a value, and tap Save.

**What is a tag?**
A tag is a label for anything you want to track — e.g. `weight`, `mood`, `sleep_hours`, `headache`. All entries with the same tag are grouped together in Analytics.

**How do I view a chart for my data?**
Go to the **Analytics** tab and tap any tag to open its chart. You can change the time range, switch between chart types, and apply filters like rolling average or outlier removal.

**What does the Correlate feature do?**
Correlate lets you compare two tags to see if they move together. You can adjust the time lag to discover delayed relationships (e.g. does `sleep_hours` predict `mood` the next day?).

**What is the Analyst feature?**
Analyst is an AI-powered chat that can answer questions about your data, surface patterns, and generate insights. It is a Premium feature.

**How do I import data?**
In the Add Entry sheet, tap **Import from CSV URL** and paste a link to a CSV file. The file should have a `date` column otherwise it marks all the data as current date and time.

**How do I delete an entry?**
On the Feed tab, swipe left on any entry to reveal the Delete button.

**Does Meetrics sync with Apple Health?**
Not currently. Data is stored locally on your device.

**Where is my data stored?**
All data is stored locally on your device using Apple's SwiftData framework. Nothing is sent to any server except when using the Analyst AI feature, which sends your questions (not your raw data) to an AI model.

  **How do I restore my Premium subscription?**
  Go to the Analyst tab and tap **Restore Purchases**.
