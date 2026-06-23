import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

'Growing Line Chart'
# Create a clean placeholder container
chart_placeholder = st.empty()

# Start with your baseline DataFrame
df_total = pd.DataFrame(np.random.randn(1, 1), columns=["a"])

for i in range(1,100):
    # Simulate receiving new streaming data
    new_rows = pd.DataFrame(np.random.randn(1, 1), columns=["a"])
    
    # Append the new data to your local tracking DataFrame
    df_total = pd.concat([df_total, new_rows], ignore_index=True)
    
    # Redraw the updated chart in the placeholder spot
    chart_placeholder.line_chart(df_total)
    
    time.sleep(0.1)

values = np.random.rand(10)
'matplotlibs Line Chart:'
fig, ax = plt.subplots()
ax.plot(values)
st.pyplot(fig)
