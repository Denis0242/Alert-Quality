from pathlib import Path
import streamlit as st
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
A = pd.read_csv(ROOT / "data/processed/alerts_enriched.csv")
Q = pd.read_csv(ROOT / "data/processed/qa_reviews.csv")
R = pd.read_csv(ROOT / "data/processed/rule_performance.csv")

st.set_page_config(page_title="AML Alert QA & Rule Performance", layout="wide")
st.title("AML Alert Quality, QA & Rule Performance Analytics")

with st.sidebar:
    st.header("Filters")
    rules = st.multiselect(
        "Rule",
        sorted(A["rule_name"].dropna().unique()),
        default=sorted(A["rule_name"].dropna().unique()),
    )
    dispositions = st.multiselect(
        "Disposition",
        sorted(A["disposition"].dropna().unique()),
        default=sorted(A["disposition"].dropna().unique()),
    )

F = A[A["rule_name"].isin(rules) & A["disposition"].isin(dispositions)].copy()
QF = Q[Q["rule_name"].isin(rules)].copy()
RF = R[R["rule_name"].isin(rules)].copy()

alerts_count = len(F)
qa_reviewed = len(QF)
qa_pass_rate = (QF["qa_result"].eq("Pass").mean() * 100) if len(QF) else 0
false_positive_rate = (F["false_positive_flag"].mean() * 100) if len(F) else 0
escalation_rate = (F["escalated_flag"].mean() * 100) if len(F) else 0
escalated = F[F["escalated_flag"] == 1]
sar_conversion = (escalated["sar_flag"].mean() * 100) if len(escalated) else 0
review_candidates = (
    RF[RF["tuning_recommendation"] != "Monitor"].copy()
    if "tuning_recommendation" in RF.columns
    else pd.DataFrame()
)

st.subheader("Executive Summary")

if alerts_count == 0:
    st.warning("No alerts match the selected filters.")
else:
    if qa_pass_rate < 85 or false_positive_rate >= 50 or len(review_candidates) >= 2:
        status = "Action Recommended"
        message = (
            "The selected rules show quality or efficiency signals that should be "
            "reviewed before continuing without changes."
        )
    elif qa_pass_rate < 95 or false_positive_rate >= 30 or len(review_candidates) == 1:
        status = "Monitor Closely"
        message = (
            "Overall performance is acceptable, but one or more rules require "
            "closer monitoring or targeted review."
        )
    else:
        status = "Generally Stable"
        message = "QA quality and alert performance are generally stable across the selected rules."

    s1, s2, s3 = st.columns([1.2, 1.0, 2.8])
    s1.metric("Overall Status", status)
    s2.metric("Rules Needing Review", f"{len(review_candidates):,}")
    s3.info(message)

    st.markdown(
        f"""
        The selected population contains **{alerts_count:,} alerts**,
        of which **{qa_reviewed:,}** received QA review. The QA pass rate is
        **{qa_pass_rate:.1f}%**, while **{false_positive_rate:.1f}%** of alerts are false positives.
        The escalation rate is **{escalation_rate:.1f}%**, and **{sar_conversion:.1f}%** of
        escalated alerts converted to SAR activity.
        """
    )

    st.markdown("#### What This Means")

    if qa_pass_rate < 90:
        st.write(
            "• QA performance is below a strong-control threshold and may indicate "
            "inconsistent alert handling or documentation quality."
        )
    else:
        st.write("• QA performance is relatively strong across the selected reviews.")

    if false_positive_rate >= 50:
        st.write(
            "• The false-positive rate is high, suggesting some rules may be generating "
            "too many non-actionable alerts."
        )
    elif false_positive_rate >= 30:
        st.write("• False positives are meaningful enough to justify closer rule-efficiency review.")
    else:
        st.write("• The false-positive rate is comparatively controlled.")

    if len(review_candidates):
        top_rule = (
            review_candidates.sort_values("tuning_priority_score", ascending=False)
            .iloc[0]["rule_name"]
        )
        st.write(f"• **{top_rule}** is the highest-priority rule currently identified for review.")

    st.markdown("#### Final Decision")

    if status == "Action Recommended":
        st.error(
            "Prioritize the rules with the highest tuning-priority scores. Review false-positive "
            "behavior, QA failures, escalation outcomes, and SAR conversion before recommending "
            "rule changes."
        )
    elif status == "Monitor Closely":
        st.warning(
            "Continue monitoring the selected rules, but review the highest-priority rule and "
            "track whether QA quality or false-positive performance deteriorates."
        )
    else:
        st.success(
            "Maintain the current monitoring approach. No immediate broad rule-review action "
            "is indicated by the selected data."
        )

st.divider()

c1, c2, c3, c4, c5, c6 = st.columns(6)
c1.metric("Alerts", f"{alerts_count:,}")
c2.metric("QA Reviewed", f"{qa_reviewed:,}")
c3.metric("QA Pass Rate", f"{qa_pass_rate:.1f}%")
c4.metric("False Positive", f"{false_positive_rate:.1f}%")
c5.metric("Escalation Rate", f"{escalation_rate:.1f}%")
c6.metric("SAR Conversion", f"{sar_conversion:.1f}%")

tabs = st.tabs([
    "Rule Performance",
    "QA Review",
    "Portfolio Analytics",
    "Tableau Gallery",
])

with tabs[0]:
    st.subheader("Rule Performance & Review Priorities")
    st.caption(
        "Combines rule effectiveness and tuning priorities so you can see which rules "
        "are performing well and which may need adjustment."
    )

    if RF.empty:
        st.info("No rule-performance data is available for the selected filters.")
    else:
        st.dataframe(
            RF.sort_values("tuning_priority_score", ascending=False),
            use_container_width=True,
            hide_index=True,
        )

        if len(review_candidates):
            st.markdown("#### Rules Requiring Attention")
            st.dataframe(
                review_candidates.sort_values("tuning_priority_score", ascending=False),
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.success("No selected rules currently have a tuning recommendation beyond monitoring.")

with tabs[1]:
    st.subheader("QA Review Results")
    st.caption(
        "Shows whether alert investigations met expected quality standards and helps identify "
        "recurring documentation or decision-quality issues."
    )

    if QF.empty:
        st.info("No QA-review records are available for the selected rules.")
    else:
        st.dataframe(
            QF.sort_values(["qa_result", "alert_date"]),
            use_container_width=True,
            hide_index=True,
        )

with tabs[2]:
    st.subheader("Portfolio Analytics")

    st.caption(
        "Compares rule efficiency and QA quality across the selected monitoring rules."
    )

    if RF.empty:
        st.info("No portfolio analytics are available for the selected rules.")

    else:
        a, b = st.columns(2)

        with a:
            st.markdown("##### False Positive Rate by Rule")

            if "false_positive_rate" in RF.columns:
                fp_chart = (
                    RF.set_index("rule_name")["false_positive_rate"]
                    .round(2)
                )

                st.bar_chart(fp_chart)

        with b:
            st.markdown("##### QA Pass Rate by Rule")

            if "qa_pass_rate" in RF.columns:
                qa_chart = (
                    RF.set_index("rule_name")["qa_pass_rate"]
                    .round(2)
                )

                st.bar_chart(qa_chart)                

with tabs[3]:
    st.subheader("Tableau Gallery")
    st.caption("Final Executive Dashboard aligned with the current processed datasets and verified KPI results.")

    images = [
        ("02_executive_dashboard.png", "AML Alert Quality, QA & Rule Performance — Final Executive Dashboard"),
    ]

    for filename, caption in images:
        image_path = ROOT / "images" / filename
        if image_path.exists():
            st.image(str(image_path), caption=caption, use_container_width=True)
        else:
            st.info(f"{caption} image is not available.")

st.caption(
    "Synthetic educational portfolio project. Rule review scores support analyst "
    "recommendations only and do not represent production model tuning."
)
