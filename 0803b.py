# pip install pandas
# pip install numpy    
# pip install matplotlib

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

col_names = ['column 1','column 2','column 3']
data = pd.DataFrame(np.random.randint(30,size=(30,3)), columns=col_names)
print (data)

'line graph'
st.line_chart(data)

# Para executar:
# python -m streamlit run "G:\Meu Drive\Cursos\Python\MachineLearning\0803b.py"

'barr graph'
st.bar_chart(data)

# Grafico de Pizza
animals =['cat','cow','dog']
heights = [30,150,80]

'pie chart:'
fig, ax = plt.subplots()
ax.pie(heights, labels=animals)
st.pyplot(fig)