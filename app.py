import streamlit as st
from starter import ZONES, TIME_BLOCKS, COSTS
from analysis import best_promise

st.title("Rosa's Pizza: Best Delivery Promise")
st.write(
    "Choose a zone, a time block, a range of promises, and cost "
    "assumptions. The app finds the promise with the highest "
    "simulated net profit."
)
st.info(
    "All results come from a four-week simulation (seed=1). "
    "They are not a guarantee of future profit."
)

# Zone and time block
zone = st.selectbox("Zone", ZONES)
time_block = st.selectbox("Time block", TIME_BLOCKS)

# Promise range (tested in 5-minute steps)
min_promise = st.number_input(
    "Minimum promise (minutes)", value=20, step=5
)
max_promise = st.number_input(
    "Maximum promise (minutes)", value=70, step=5
)

# Cost inputs start at the COSTS values; COSTS itself is never changed
margin = st.number_input("Margin per order ($)", value=float(COSTS["margin"]))
refund = st.number_input("Refund per late order ($)", value=float(COSTS["refund"]))
churn_orders = st.number_input(
    "Future orders lost per late order (churn_orders)",
    value=float(COSTS["churn_orders"]),
)

if st.button("Calculate best promise"):
    # Validate inputs before calculating
    errors = []
    if min_promise <= 0 or max_promise <= 0:
        errors.append("Promises must be positive.")
    if min_promise > max_promise:
        errors.append("Minimum promise must be less than or equal to maximum.")
    if min_promise % 5 != 0 or max_promise % 5 != 0:
        errors.append("Minimum and maximum promises must be multiples of 5.")
    if margin < 0 or refund < 0 or churn_orders < 0:
        errors.append("Margin, refund, and churn_orders cannot be negative.")

    if errors:
        for message in errors:
            st.error(message)
    else:
        # New dictionary built from user inputs
        user_costs = {
            "margin": margin,
            "refund": refund,
            "churn_orders": churn_orders,
        }
        promises = list(range(int(min_promise), int(max_promise) + 1, 5))

        best_time, best_profit, table = best_promise(
            zone, time_block, promises, user_costs
        )

        st.subheader("Result")
        st.write(f"**Best promise:** {best_time} minutes")
        st.write(f"**Simulated net profit:** ${best_profit:,.2f}")
        st.caption("Net profit is for a four-week simulation.")

        if best_time == min_promise or best_time == max_promise:
            st.warning(
                "The best promise is at the edge of your range. "
                "Try a wider range to check more promises."
            )

        st.subheader("Comparison of promises")
        st.dataframe(table.round(2), hide_index=True)
