# AML Alert Quality, QA & Rule Performance Analytics

Project 6 in the Financial Crime Analytics portfolio.

This project is designed to complement the earlier portfolio rather than repeat transaction-monitoring investigations. Instead of asking **“Is this individual alert suspicious?”**, Project 6 asks **“How well are our AML alerts, review process, and monitoring rules performing?”**

## Scale
- 3,600 synthetic AML alerts
- 8 transaction-monitoring rules
- 900 QA reviews
- 12 synthetic analysts

## Core Analytics
- Alert volume
- False-positive rate
- Escalation rate
- SAR conversion
- QA pass/fail rate
- QA defect categories
- Alert aging
- Review time
- Rule review priority

## Tools
SQL, Python, Tableau, Streamlit.

## Separate KPI Visualization
1. Total Alerts
2. QA Reviewed
3. QA Pass Rate
4. False Positive Rate
5. Escalation Rate
6. SAR Conversion

## Executive Dashboard
Exactly six analytical visualizations:
1. Alert, Escalation & SAR Trend
2. False Positive Rate by Rule
3. QA Pass Rate by Rule
4. Alert Aging Heatmap with values inside cells
5. Alert Volume vs Escalation Rate scatter
6. Rule Review Priority Score

The dashboard uses one visualization color only: blue. Dates use MM/YY such as 07/26.

## Dashboard Preview

The visuals below provide a quick view of the project's key AML alert-quality, QA, and rule-performance findings.

### KPI Scorecard

![AML Alert Quality KPI Scorecard](images/01_kpi_scorecard.png)

The KPI scorecard summarizes the core operating measures used throughout the project: Total Alerts, QA Reviewed, QA Pass Rate, False Positive Rate, Escalation Rate, and SAR Conversion.

### Executive Dashboard

![AML Alert Quality Executive Dashboard](images/02_executive_dashboard.png)

The executive dashboard brings together alert trends, rule efficiency, QA quality, alert aging, escalation behavior, and rule-review priorities in one view.

### Featured Dashboard Visual 1 — Alert, Escalation & SAR Trend

![Alert Escalation and SAR Trend](images/03_alert_escalation_sar_trend.png)

Shows how alert volume, escalations, and SAR-related outcomes change over time, making it easier to identify shifts in transaction-monitoring activity and downstream investigative workload.

### Featured Dashboard Visual 2 — False Positive Rate by Rule

![False Positive Rate by Rule](images/04_false_positive_rate_by_rule.png)

Compares false-positive performance across transaction-monitoring rules to identify scenarios generating a larger share of non-actionable alerts.

### Featured Dashboard Visual 3 — QA Pass Rate by Rule

![QA Pass Rate by Rule](images/05_qa_pass_rate_by_rule.png)

Compares QA performance across monitoring rules to highlight areas where investigation quality, documentation, or disposition consistency may require closer review.

## Resume Bullets
**AML Alert Quality, QA & Rule Performance Analytics | SQL, Python, Tableau, Streamlit**
- Analyzed 3,600 synthetic AML alerts across 8 monitoring rules to measure alert volume, false-positive rates, escalation rates, SAR conversion, alert aging, and operational performance.
- Built QA and rule-performance reporting using SQL and Python, then developed Tableau and Streamlit views to identify QA defects, compare rule effectiveness, and prioritize monitoring scenarios for analyst review.

## Interview Explanation
“I built this project to analyze the quality and performance of AML monitoring rules rather than investigate one alert at a time. I measured alert volume, false-positive rate, escalation rate, SAR conversion, QA pass rate, aging, and review effort. I then created an explainable rule-review priority score to identify scenarios that may deserve threshold or logic review. The project stays at the analyst level: it recommends where to investigate performance issues, but it does not claim production rule tuning or model validation.”

## Disclaimer
All data is synthetic. The rule-review priority score is an educational analytics framework and does not represent production AML model tuning or regulatory model validation.


## Approved Blue & Orange Dashboard
The final Project 6 dashboard uses only blue and orange for analytical marks, with navy text on a white background. It contains six KPI cards and exactly six analytical visualizations. The QA Results by Analyst visualization is a stacked Pass/Fail bar chart.

The packaged `images/02_executive_dashboard.png` is the approved final dashboard reference.
