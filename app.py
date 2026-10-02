import streamlit as st
from core.pipeline import run_lifelink
from core.models import Resource

st.set_page_config(
    page_title="LIFELINK — Real-World Needs Coordination",
    page_icon="🔗",
    layout="wide",
)

st.title("LIFELINK")
st.caption("Multi-Agent AI coordination for real-world needs")

with st.sidebar:
    st.header("Request settings")
    country = st.selectbox("Country", ["Pakistan", "United Kingdom", "United States", "United Arab Emirates", "Other"])
    city = st.text_input("City / area", "Lahore")
    budget = st.number_input("Maximum budget (optional)", min_value=0.0, value=0.0, step=10.0)
    urgency = st.selectbox("Urgency", ["Normal", "Today", "Urgent"])
    language = st.selectbox("Output language", ["English", "Roman Urdu", "Urdu"])
    st.divider()
    st.info("Demo data is clearly labelled. Connect real provider APIs before claiming live availability or booking.")

examples = [
    "I need wheelchair-accessible transport for my elderly mother tomorrow morning.",
    "My small business needs 200 custom boxes within 3 days.",
    "I need a laptop repair service that can collect the device from my home.",
    "Our community needs a temporary accessible venue for a 50-person event.",
]

st.subheader("What do you need to get done?")
selected = st.selectbox("Try an example", ["Custom request"] + examples)
request = st.text_area(
    "Describe the real-world need",
    value="" if selected == "Custom request" else selected,
    height=120,
    placeholder="Tell LIFELINK what you need, where, when, and any important constraints...",
)

if st.button("Analyze & Coordinate", type="primary", use_container_width=True):
    if not request.strip():
        st.warning("Please describe a need first.")
        st.stop()

    with st.spinner("LIFELINK agents are analyzing the request..."):
        result = run_lifelink(
            request=request,
            city=city,
            country=country,
            budget=budget if budget > 0 else None,
            urgency=urgency,
            language=language,
        )

    st.success("Multi-agent analysis complete.")

    tabs = st.tabs([
        "Need",
        "Matches",
        "Checks",
        "Action Plan",
        "Agent Trace",
    ])

    with tabs[0]:
        st.subheader("Structured need")
        need = result["need"]
        c1, c2, c3 = st.columns(3)
        c1.metric("Category", need["category"])
        c2.metric("Urgency", need["urgency"])
        c3.metric("Location", need["location"])
        st.write("**Summary:**", need["summary"])
        if need["constraints"]:
            st.write("**Constraints:**")
            for x in need["constraints"]:
                st.write("•", x)

    with tabs[1]:
        st.subheader("Potential matches")
        if not result["matches"]:
            st.warning("No demo resources matched this request. Try another request or connect a provider directory.")
        for m in result["matches"]:
            with st.container(border=True):
                st.markdown(f"### {m['name']}")
                st.write(m["description"])
                cols = st.columns(4)
                cols[0].write(f"**Type**\n{m['type']}")
                cols[1].write(f"**Estimated cost**\n{m['estimated_cost']}")
                cols[2].write(f"**Distance**\n{m['distance']}")
                cols[3].write(f"**Match**\n{m['match_score']}%")
                st.caption(m["data_status"])

    with tabs[2]:
        st.subheader("Cross-agent checks")
        for check in result["checks"]:
            icon = "✅" if check["status"] == "pass" else "⚠️"
            st.markdown(f"{icon} **{check['agent']}** — {check['finding']}")

    with tabs[3]:
        st.subheader("Recommended coordination plan")
        for i, step in enumerate(result["action_plan"], 1):
            st.markdown(f"**{i}. {step}**")
        if result["follow_up"]:
            st.info(result["follow_up"])

    with tabs[4]:
        st.subheader("How the agents contributed")
        for event in result["trace"]:
            st.write(f"**{event['agent']}** → {event['action']}")
            st.caption(event["output"])

st.divider()
st.caption("LIFELINK is a coordination intelligence prototype. It does not independently guarantee provider quality, availability, safety, pricing, or successful fulfillment.")
