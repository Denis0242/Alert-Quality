def review_priority(false_positive_rate, qa_pass_rate, escalation_rate, avg_alert_age):
    return round(
        false_positive_rate * 45
        + (1 - qa_pass_rate) * 25
        + (1 - escalation_rate) * 15
        + min(avg_alert_age / 30, 1) * 15,
        1
    )
