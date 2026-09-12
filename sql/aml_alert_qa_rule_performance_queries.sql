-- AML Alert Quality, QA & Rule Performance Analytics

-- 1. Alert volume by rule
SELECT rule_id, rule_name, COUNT(*) AS alert_volume
FROM alerts_enriched
GROUP BY rule_id, rule_name
ORDER BY alert_volume DESC;

-- 2. False positive rate by rule
SELECT rule_id, rule_name,
       AVG(false_positive_flag * 1.0) AS false_positive_rate
FROM alerts_enriched
GROUP BY rule_id, rule_name
ORDER BY false_positive_rate DESC;

-- 3. Escalation rate by rule
SELECT rule_id, rule_name,
       AVG(escalated_flag * 1.0) AS escalation_rate
FROM alerts_enriched
GROUP BY rule_id, rule_name
ORDER BY escalation_rate DESC;

-- 4. SAR conversion by rule
SELECT rule_id, rule_name,
       SUM(sar_flag) AS sar_cases,
       SUM(escalated_flag) AS escalations,
       1.0 * SUM(sar_flag) / NULLIF(SUM(escalated_flag),0) AS sar_conversion_rate
FROM alerts_enriched
GROUP BY rule_id, rule_name
ORDER BY sar_conversion_rate DESC;

-- 5. QA pass rate by rule
SELECT rule_id, rule_name,
       COUNT(*) AS qa_reviews,
       AVG(CASE WHEN qa_result='Pass' THEN 1.0 ELSE 0 END) AS qa_pass_rate
FROM qa_reviews
GROUP BY rule_id, rule_name
ORDER BY qa_pass_rate ASC;

-- 6. QA issue distribution
SELECT qa_issue, COUNT(*) AS reviews
FROM qa_reviews
WHERE qa_result='Fail'
GROUP BY qa_issue
ORDER BY reviews DESC;

-- 7. Alert aging
SELECT rule_id, rule_name,
       AVG(alert_age_days) AS avg_alert_age,
       MAX(alert_age_days) AS max_alert_age
FROM alerts_enriched
GROUP BY rule_id, rule_name
ORDER BY avg_alert_age DESC;

-- 8. Review productivity
SELECT analyst_id,
       COUNT(*) AS alerts_reviewed,
       AVG(review_minutes) AS avg_review_minutes
FROM alerts_enriched
GROUP BY analyst_id
ORDER BY alerts_reviewed DESC;

-- 9. Rule review candidates
SELECT *
FROM rule_performance
WHERE tuning_recommendation <> 'Monitor'
ORDER BY tuning_priority_score DESC;

-- 10. Monthly alert trend
SELECT DATE_TRUNC('month', alert_date) AS month,
       COUNT(*) AS alerts,
       SUM(escalated_flag) AS escalations,
       SUM(sar_flag) AS sar_cases
FROM alerts_enriched
GROUP BY DATE_TRUNC('month', alert_date)
ORDER BY month;

-- 11. High-volume / high-FP rules
SELECT *
FROM rule_performance
WHERE alert_volume >= 400
  AND false_positive_rate >= 0.50
ORDER BY false_positive_rate DESC;

-- 12. QA failures requiring remediation
SELECT *
FROM qa_reviews
WHERE qa_result='Fail'
ORDER BY alert_date DESC;
