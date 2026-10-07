---
name: notebook-to-streamlit
description: Convert the Rosa's Pizza analysis notebook into a Streamlit app using its existing calculation functions.
---

# Convert the notebook into a Streamlit app

Read Rosas_Pizza_Assignment_1.ipynb before building the app.

## Reuse the notebook logic

- Move cost_per_late_order() and best_promise() into analysis.py.
- Preserve their calculation logic and seed=1.
- Import these functions into app.py.
- Use the official rosa-starter package.
- Do not recreate or modify the official simulator or its constants.

## App requirements

- Provide dropdowns for zone and time block using ZONES and TIME_BLOCKS.
- Provide minimum and maximum promise inputs.
- Test promises in 5-minute steps.
- Provide inputs for margin, refund, and churn_orders.
- Use COSTS as the default values without modifying that dictionary.
- Add a button to calculate the best promise.
- Show the best promise, simulated net profit, and comparison table.
- Explain that results represent a four-week simulation.
- Validate inputs before calculating.

## Project and verification

- Create requirements.txt with the necessary dependencies.
- Keep Python code simple and explain each file to the student.
- Check that Far West, Fri/Sat eve, promises 20–70, and default
  costs reproduce 55 minutes and $1,212.40 with seed=1.
- Prepare the project for GitHub and Streamlit Community Cloud.