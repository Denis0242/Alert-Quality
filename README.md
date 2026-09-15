# AML Alert Quality, QA & Rule Performance Analytics

**AML / Transaction Monitoring Analytics Portfolio Project**

An end-to-end AML quality-assurance and rule-performance analytics
project using **Python, SQL, Tableau, and Streamlit** to evaluate alert
quality, false positives, escalation behavior, SAR conversion, QA
results, analyst review efficiency, and transaction-monitoring rule
performance.

> **Portfolio scope:** This project uses synthetic data created for
> educational and portfolio purposes. Rule thresholds, QA results,
> tuning scores, alert outcomes, and recommendations are illustrative
> and do not represent any financial institution's production
> transaction-monitoring or model-governance framework.

------------------------------------------------------------------------

## Project Overview

Transaction-monitoring programs need to balance detection effectiveness
with alert quality, investigator workload, QA standards, and
false-positive reduction.

This project analyzes:

-   **3,600 AML transaction-monitoring alerts**
-   **900 QA reviews**
-   **8 transaction-monitoring rules**
-   Rule-level false-positive, escalation, SAR-conversion, QA,
    review-time, and tuning metrics

The project moves from enriched alert data into QA analysis,
rule-performance measurement, tuning prioritization, and executive
decision support.

------------------------------------------------------------------------

## Business & Control Questions

-   Which monitoring rules generate the most alerts?
-   Which rules create the highest false-positive burden?
-   Which rules escalate the greatest share of alerts?
-   Which escalated alerts convert to SAR activity?
-   Which rules have weaker QA performance?
-   What QA issues occur most often?
-   Which rules should be prioritized for threshold or logic review?
-   How much analyst time is spent reviewing alerts?
-   Are higher-risk or escalated alerts associated with longer review
    times?
-   How can QA and rule-performance metrics support stronger AML
    controls without replacing governance review?

------------------------------------------------------------------------

## Data Model

  ---------------------------------------------------------------------------
  Dataset                                          Rows Purpose
  ------------------------ ---------------------------- ---------------------
  `alerts_enriched.csv`                           3,600 Alert-level AML
                                                        monitoring and
                                                        investigation
                                                        outcomes

  `qa_reviews.csv`                                  900 QA reviews and issue
                                                        findings

  `rule_performance.csv`                              8 Rule-level
                                                        performance and
                                                        tuning metrics

  `analysts.csv`                                     12 Analyst reference
                                                        information

  `rules.csv`                                         8 Monitoring-rule
                                                        logic, thresholds and
                                                        status
  ---------------------------------------------------------------------------

See [`docs/data_dictionary.md`](docs/data_dictionary.md) for field-level
definitions and relationships.

------------------------------------------------------------------------

## Exploratory Data Analysis & Data Quality

The notebook includes a practical EDA and validation workflow:

-   Dataset and schema review
-   Missing-value analysis
-   Duplicate validation
-   Datatype and range checks
-   Summary statistics
-   IQR-based outlier review
-   KPI/rate validation
-   Rule-level performance review
-   QA outcome validation
-   Business-rule checks
-   Final analytical-dataset validation

Unusual values are reviewed in context rather than automatically removed
because extreme review times, alert amounts, or risk scores can be
analytically meaningful.

------------------------------------------------------------------------

## Feature Engineering

The project already contains derived alert and rule-performance fields
such as:

-   `false_positive_flag`
-   `escalated_flag`
-   `month`
-   `false_positive_rate`
-   `escalation_rate`
-   `sar_conversion_rate`
-   `qa_pass_rate`
-   `tuning_priority_score`
-   `tuning_recommendation`

The notebook additionally demonstrates:

-   `estimated_false_positive_alerts`
-   `qa_failure_rate`
-   `rule_review_flag`

These features are intentionally straightforward so the analytical logic
remains explainable to recruiters, investigators, QA teams, and
model/rule-governance stakeholders.

------------------------------------------------------------------------

## AML QA & Rule Performance Analysis

The project evaluates four connected areas:

**Alert Quality** --- alert volume, risk, disposition, false positives,
escalation and SAR activity.

**QA Performance** --- QA pass/fail results, recurring QA issues,
analyst-review quality and documentation weaknesses.

**Rule Effectiveness** --- alert volume, false-positive rate, escalation
rate, SAR-conversion rate, average risk and alerted amount by rule.

**Rule Tuning Prioritization** --- project-derived tuning scores and
recommendations that identify rules requiring closer threshold or logic
review.

------------------------------------------------------------------------

## SQL Analysis

The SQL file contains **12 analytical queries/statements** covering
alert performance, rule efficiency, false positives, escalation, SAR
conversion, QA outcomes, analyst quality and tuning prioritization.

See [`sql/`](sql/) for the complete SQL analysis.

------------------------------------------------------------------------

## Verified Current KPIs

  KPI                                      Current Result
  ------------------------------------ ------------------
  Total Alerts                                  **3,600**
  QA Reviews                                      **900**
  QA Pass Rate                                  **86.7%**
  False Positives                               **1,973**
  False-Positive Rate                           **54.8%**
  Escalated Alerts                              **1,064**
  Escalation Rate                               **29.6%**
  SAR Cases                                       **147**
  SAR Conversion of Escalated Alerts            **13.8%**
  Total Alerted Amount                       **\$158.1M**
  Avg. Review Time                       **37.9 minutes**
  Avg. Alert Age                             **9.3 days**

------------------------------------------------------------------------

## Key Findings

-   **1,973 of 3,600 alerts** are false positives, producing a **54.8%
    false-positive rate**.
-   **1,064 alerts** were escalated, representing **29.6%** of the
    portfolio.
-   **147 alerts** are associated with SAR activity; approximately
    **13.8%** of escalated alerts converted to SAR activity.
-   The portfolio QA pass rate is **86.7%** across **900 reviews**.
-   **Structuring / Cash Activity** generates the largest alert volume
    at **650 alerts**.
-   **Unusual Volume Increase** is the highest-priority rule for review
    based on the project tuning-priority score (**49.9**).
-   **6 of 8 rules** have a tuning recommendation beyond routine
    monitoring.

The most frequent QA-failure issues are:

-   **KYC Context Missing: 32 failures**
-   **Insufficient Narrative: 32 failures**
-   **Incomplete Transaction Review: 29 failures**

These findings support rule-quality review and tuning prioritization;
they do not constitute production rule changes or model-governance
approval.

------------------------------------------------------------------------

## Streamlit QA & Rule Performance Application

The Streamlit application provides interactive review of AML alert
quality and monitoring-rule performance.

### Filters

-   Rule
-   Disposition

### Executive Decision Support

The application summarizes the selected rules as:

-   **Generally Stable**
-   **Monitor Closely**
-   **Action Recommended**

The status considers:

-   QA pass rate
-   False-positive rate
-   Number of rules identified for review

### Interactive Tabs

-   Rule Performance
-   QA Review
-   Portfolio Analytics
-   Tableau Gallery

The **Tableau Gallery is simplified to display only the Executive
Dashboard**, avoiding duplication of the KPI scorecard already
represented within the dashboard.

------------------------------------------------------------------------

## Tableau Executive Dashboard

The dashboard presents:

1.  Alerts, Escalations & SAR Trend
2.  Alert Disposition
3.  Top Rules by Alert Volume
4.  Alert Activity Heatmap
5.  Review Time vs Alert Risk Score
6.  QA Results by Analyst

### Dashboard Preview

![AML Alert Quality, QA & Rule Performance
Dashboard](images/02_executive_dashboard.png)


------------------------------------------------------------------------

## Analytical Workflow

``` text
Monitoring Rules
      ↓
AML Alerts
      ↓
Alert Investigation Outcomes
      ↓
QA Reviews
      ↓
EDA + KPI Validation
      ↓
Rule Performance Metrics
      ↓
Tuning Priority Analysis
      ↓
Tableau + Streamlit Decision Support
```

------------------------------------------------------------------------

## Tools & Technologies

  -----------------------------------------------------------------------
  Tool                                Use
  ----------------------------------- -----------------------------------
  **Python / Pandas**                 EDA, QA analysis, feature
                                      engineering and validation

  **SQL**                             Alert, QA and rule-performance
                                      analysis

  **Tableau**                         Executive AML quality dashboard

  **Streamlit**                       Interactive QA and rule-performance
                                      review

  **Jupyter Notebook**                Reproducible analytical workflow

  **Git / GitHub**                    Version control and portfolio
                                      presentation
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Repository Structure

``` text
Alert-Quality/
├── app/             # Streamlit application
├── data/            # Synthetic raw and processed datasets
├── docs/            # Data dictionary and supporting documentation
├── images/          # Executive dashboard
├── notebooks/       # EDA, QA and rule-performance analysis
├── sql/             # AML QA/rule-performance queries
├── tableau/         # Tableau workbook
├── .gitignore
├── .python-version
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md
```

------------------------------------------------------------------------

## How to Run

``` bash
git clone https://github.com/Denis0242/Alert-Quality.git
cd Alert-Quality
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

------------------------------------------------------------------------

## Skills Demonstrated

### AML / Financial Crime

-   Transaction Monitoring
-   AML Alert Quality
-   QA Review Analytics
-   Rule Performance Analysis
-   Alert Disposition Analysis
-   False-Positive Analysis
-   Escalation Analysis
-   SAR-Conversion Analysis
-   Rule Tuning Prioritization
-   Monitoring Effectiveness
-   Investigation Quality Review

### Data & Analytics

-   Exploratory Data Analysis
-   Feature Engineering
-   Data Quality Validation
-   SQL
-   Python / Pandas
-   KPI Development
-   Rate Validation
-   Trend Analysis
-   Operational Analytics
-   Business-Rule Validation

### Visualization & Decision Support

-   Tableau
-   Streamlit
-   Executive Dashboards
-   QA Performance Views
-   Rule Prioritization
-   Interactive Filtering
-   Data Storytelling

------------------------------------------------------------------------

## Disclaimer

This project uses **synthetic data** created for educational and
portfolio purposes. No real customer, transaction, AML alert, analyst,
SAR, financial institution, or confidential compliance data is included.

Rule thresholds, QA outcomes, tuning scores, false-positive rates,
escalation rates, SAR-conversion rates and recommendations are
illustrative. They should not be interpreted as actual
financial-institution policy, production rule tuning, model-validation
approval, or regulatory determinations.
