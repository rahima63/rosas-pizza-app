import numpy as np
import pandas as pd
from starter import delivery_times


def cost_per_late_order(costs):
    return costs["refund"] + costs["churn_orders"] * costs["margin"]


def best_promise(zone, time_block, promises, costs):
    late_cost = cost_per_late_order(costs)

    best_time = None
    best_profit = None
    results = []

    for promise in promises:
        times = delivery_times(zone, time_block, promise, seed=1)

        number_orders = len(times)
        number_late = np.sum(times > promise)

        profit = (
            number_orders * costs["margin"]
            - number_late * late_cost
        )

        results.append({
            "Promise (minutes)": promise,
            "Number of orders": number_orders,
            "Late orders": number_late,
            "Net profit": profit
        })

        if best_profit is None or profit > best_profit:
            best_time = promise
            best_profit = profit

    return best_time, best_profit, pd.DataFrame(results)
