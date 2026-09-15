# Data Dictionary

## AML Alert Quality, QA & Rule Performance Analytics

This data dictionary documents the datasets used in the AML transaction-monitoring quality, QA, and rule-performance analysis. It identifies field definitions, data types, representative values, and whether fields are source attributes or derived/engineered analytics features.

> **Portfolio note:** The datasets are structured for demonstration and analytical portfolio purposes. Field definitions reflect their use within this project and should not be interpreted as production-bank data standards.

## Dataset Overview

| Dataset | Rows | Columns | Purpose |
|---|---:|---:|---|
| `alerts.csv` | 3,600 | 15 | Alert-level transaction-monitoring dataset used for alert review, disposition, escalation, SAR, and operational analysis. |
| `analysts.csv` | 12 | 4 | Reference table containing analyst team and experience information. |
| `rules.csv` | 8 | 7 | Reference table describing transaction-monitoring rules, detection logic, thresholds, and status. |
| `alerts_enriched.csv` | 3,600 | 15 | Analytics-ready alert dataset containing alert attributes plus rule descriptors and derived analysis fields. |
| `qa_reviews.csv` | 900 | 13 | Quality-assurance review dataset used to evaluate investigation quality and identify review issues. |
| `rule_performance.csv` | 8 | 18 | Rule-level performance dataset containing aggregated KPIs and derived tuning metrics. |

## `alerts.csv`

Alert-level transaction-monitoring dataset used for alert review, disposition, escalation, SAR, and operational analysis.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `alert_id` | String | Source / Operational | Unique identifier assigned to each transaction-monitoring alert. | `ALT00001` |
| `alert_date` | Date | Source / Operational | Date on which the transaction-monitoring alert was generated. | `2026-08-25` |
| `rule_id` | String | Source / Operational | Unique identifier for the monitoring rule that generated the alert. | `R001` |
| `analyst_id` | String | Source / Operational | Identifier of the analyst assigned to or responsible for reviewing the alert. | `ANL04` |
| `risk_score` | Float | Source / Operational | Numeric risk score representing the assessed risk level of the alert. | `96` |
| `alert_amount` | Float | Source / Operational | Monetary amount associated with the activity that generated the alert. | `7578.03` |
| `alert_age_days` | Integer | Source / Operational | Number of days the alert remained in the review workflow. | `18` |
| `review_minutes` | Integer | Source / Operational | Number of minutes spent reviewing or investigating the alert. | `36` |
| `disposition` | String | Source / Operational | Final analyst decision or outcome of the alert review. | `Close - False Positive` |
| `sar_flag` | Integer | Source / Operational | Binary indicator showing whether the alert was associated with a SAR decision/case (1 = yes, 0 = no). | `0` |
| `rule_name` | String | **Engineered / Derived** | Descriptive name of the transaction-monitoring rule. | `Structuring / Cash Activity` |
| `channel_focus` | String | **Engineered / Derived** | Transaction channel or payment type primarily monitored by the rule. | `Cash` |
| `false_positive_flag` | Integer | **Engineered / Derived** | Binary indicator identifying alerts determined to be false positives (1 = yes, 0 = no). | `1` |
| `escalated_flag` | Integer | **Engineered / Derived** | Binary indicator showing whether an alert was escalated for further investigation (1 = yes, 0 = no). | `0` |
| `month` | String | **Engineered / Derived** | Year-month period derived from the alert date for monthly trend analysis. | `2026-08` |

## `analysts.csv`

Reference table containing analyst team and experience information.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `analyst_id` | String | Source / Operational | Identifier of the analyst assigned to or responsible for reviewing the alert. | `ANL01` |
| `analyst_name` | String | Source / Operational | Display name assigned to the analyst. | `Analyst 01` |
| `team` | String | Source / Operational | Transaction-monitoring operations team to which the analyst belongs. | `TM Operations A` |
| `experience_level` | String | Source / Operational | Analyst role or experience classification. | `Analyst I` |

## `rules.csv`

Reference table describing transaction-monitoring rules, detection logic, thresholds, and status.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `rule_id` | String | Source / Operational | Unique identifier for the monitoring rule that generated the alert. | `R001` |
| `rule_name` | String | **Engineered / Derived** | Descriptive name of the transaction-monitoring rule. | `Structuring / Cash Activity` |
| `channel_focus` | String | **Engineered / Derived** | Transaction channel or payment type primarily monitored by the rule. | `Cash` |
| `logic_type` | String | Source / Operational | Type of detection logic or monitoring approach used by the rule. | `Daily aggregation` |
| `threshold_1` | Float | Source / Operational | Primary numeric threshold used by the monitoring rule. | `8200` |
| `threshold_2` | Float | Source / Operational | Secondary numeric threshold used by the monitoring rule when applicable. | `9800` |
| `rule_status` | String | Source / Operational | Operational status of the transaction-monitoring rule. | `Active` |

## `alerts_enriched.csv`

Analytics-ready alert dataset containing alert attributes plus rule descriptors and derived analysis fields.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `alert_id` | String | Source / Operational | Unique identifier assigned to each transaction-monitoring alert. | `ALT00001` |
| `alert_date` | Date | Source / Operational | Date on which the transaction-monitoring alert was generated. | `2026-08-25` |
| `rule_id` | String | Source / Operational | Unique identifier for the monitoring rule that generated the alert. | `R001` |
| `analyst_id` | String | Source / Operational | Identifier of the analyst assigned to or responsible for reviewing the alert. | `ANL04` |
| `risk_score` | Float | Source / Operational | Numeric risk score representing the assessed risk level of the alert. | `96` |
| `alert_amount` | Float | Source / Operational | Monetary amount associated with the activity that generated the alert. | `7578.03` |
| `alert_age_days` | Integer | Source / Operational | Number of days the alert remained in the review workflow. | `18` |
| `review_minutes` | Integer | Source / Operational | Number of minutes spent reviewing or investigating the alert. | `36` |
| `disposition` | String | Source / Operational | Final analyst decision or outcome of the alert review. | `Close - False Positive` |
| `sar_flag` | Integer | Source / Operational | Binary indicator showing whether the alert was associated with a SAR decision/case (1 = yes, 0 = no). | `0` |
| `rule_name` | String | **Engineered / Derived** | Descriptive name of the transaction-monitoring rule. | `Structuring / Cash Activity` |
| `channel_focus` | String | **Engineered / Derived** | Transaction channel or payment type primarily monitored by the rule. | `Cash` |
| `false_positive_flag` | Integer | **Engineered / Derived** | Binary indicator identifying alerts determined to be false positives (1 = yes, 0 = no). | `1` |
| `escalated_flag` | Integer | **Engineered / Derived** | Binary indicator showing whether an alert was escalated for further investigation (1 = yes, 0 = no). | `0` |
| `month` | String | **Engineered / Derived** | Year-month period derived from the alert date for monthly trend analysis. | `2026-08` |

## `qa_reviews.csv`

Quality-assurance review dataset used to evaluate investigation quality and identify review issues.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `qa_review_id` | String | Source / Operational | Unique identifier for a quality-assurance review. | `QA0001` |
| `alert_id` | String | Source / Operational | Unique identifier assigned to each transaction-monitoring alert. | `ALT01830` |
| `alert_date` | Date | Source / Operational | Date on which the transaction-monitoring alert was generated. | `2026-06-27` |
| `rule_id` | String | Source / Operational | Unique identifier for the monitoring rule that generated the alert. | `R006` |
| `rule_name` | String | **Engineered / Derived** | Descriptive name of the transaction-monitoring rule. | `P2P Funnel Activity` |
| `analyst_id` | String | Source / Operational | Identifier of the analyst assigned to or responsible for reviewing the alert. | `ANL11` |
| `qa_reviewer_id` | String | Source / Operational | Identifier of the analyst/reviewer who performed the QA review. | `ANL12` |
| `risk_score` | Float | Source / Operational | Numeric risk score representing the assessed risk level of the alert. | `71` |
| `review_minutes` | Integer | Source / Operational | Number of minutes spent reviewing or investigating the alert. | `54` |
| `alert_age_days` | Integer | Source / Operational | Number of days the alert remained in the review workflow. | `25` |
| `disposition` | String | Source / Operational | Final analyst decision or outcome of the alert review. | `Close - False Positive` |
| `qa_result` | String | Source / Operational | Quality-assurance outcome for the reviewed alert. | `Pass` |
| `qa_issue` | String | Source / Operational | Issue or deficiency identified during QA review, when applicable. | `Incomplete Transaction Review` |

## `rule_performance.csv`

Rule-level performance dataset containing aggregated KPIs and derived tuning metrics.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `rule_id` | String | Source / Operational | Unique identifier for the monitoring rule that generated the alert. | `R001` |
| `rule_name` | String | **Engineered / Derived** | Descriptive name of the transaction-monitoring rule. | `Structuring / Cash Activity` |
| `alert_volume` | Integer | **Engineered / Derived** | Total number of alerts generated by the rule. | `650` |
| `false_positives` | Integer | **Engineered / Derived** | Number of alerts generated by the rule that were closed as false positives. | `394` |
| `escalations` | Integer | **Engineered / Derived** | Number of alerts generated by the rule that were escalated. | `169` |
| `sar_cases` | Integer | **Engineered / Derived** | Number of escalated alerts associated with SAR cases. | `18` |
| `avg_risk_score` | Float | **Engineered / Derived** | Average risk score across alerts generated by the rule. | `58.7385` |
| `avg_alert_age` | Float | **Engineered / Derived** | Average alert age in days for alerts generated by the rule. | `9.6554` |
| `avg_review_minutes` | Float | **Engineered / Derived** | Average analyst review time in minutes for alerts generated by the rule. | `38.4231` |
| `alerted_amount` | Float | **Engineered / Derived** | Total monetary value associated with alerts generated by the rule. | `27667596.17` |
| `false_positive_rate` | Float | **Engineered / Derived** | Proportion of generated alerts classified as false positives. | `0.6062` |
| `escalation_rate` | Float | **Engineered / Derived** | Proportion of generated alerts escalated for further investigation. | `0.26` |
| `sar_conversion_rate` | Float | **Engineered / Derived** | Proportion of escalated alerts that converted to SAR cases. | `0.1065` |
| `qa_reviews` | Integer | **Engineered / Derived** | Number of QA reviews performed for alerts associated with the rule. | `143` |
| `qa_failures` | Integer | **Engineered / Derived** | Number of QA reviews that resulted in a failure. | `18` |
| `qa_pass_rate` | Float | **Engineered / Derived** | Proportion of QA reviews that resulted in a pass. | `0.8741` |
| `tuning_priority_score` | Float | **Engineered / Derived** | Derived score used to prioritize monitoring rules for tuning or optimization. | `46.4` |
| `tuning_recommendation` | String | **Engineered / Derived** | Recommended rule-tuning action based on performance and quality metrics. | `Review Threshold / Logic` |

## Key Relationships

- `alerts.rule_id` → `rules.rule_id` links each alert to the monitoring rule that generated it.
- `alerts.analyst_id` → `analysts.analyst_id` links alerts to assigned analysts.
- `qa_reviews.alert_id` → `alerts.alert_id` links QA reviews to the underlying alert.
- `qa_reviews.rule_id` → `rules.rule_id` supports QA analysis by monitoring rule.
- `rule_performance.rule_id` → `rules.rule_id` links aggregated rule KPIs to rule definitions and thresholds.

## Feature Engineering & Derived Metrics

The analytics workflow uses derived fields and aggregations to convert operational alert data into decision-support features. Examples include `false_positive_flag`, `escalated_flag`, and `month` at the alert level, together with rule-level measures such as `false_positive_rate`, `escalation_rate`, `sar_conversion_rate`, `qa_pass_rate`, and `tuning_priority_score`. These features support trend analysis, rule-quality assessment, operational monitoring, and rule-tuning prioritization.

### Metric Interpretation

- **False Positive Rate:** share of a rule's alerts determined to be false positives.
- **Escalation Rate:** share of alerts escalated for additional investigation.
- **SAR Conversion Rate:** share of escalated alerts associated with SAR cases.
- **QA Pass Rate:** share of reviewed alerts that passed quality assurance.
- **Tuning Priority Score:** project-derived indicator used to prioritize rules for threshold or logic review.

## Data Quality Notes

- Missing values may be valid where a field is conditional, such as `threshold_2` for rules requiring only one threshold or `qa_issue` when a QA review passes.
- Binary flags use `1` for yes/true and `0` for no/false.
- Monetary fields are represented numerically and should be formatted as currency in reporting layers where appropriate.
- Rate fields are stored as decimal proportions; for example, `0.60` represents 60%.
- `month` is a reporting-period feature derived from `alert_date`.

---

*Prepared for the AML Alert Quality, QA & Rule Performance Analytics portfolio project.*