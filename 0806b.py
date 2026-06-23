# pip install pandas
# pip install numpy   
# pip install streamlit
# pip install matplotlib
# pip install seaborn
# python -m pip install scikit-learn

# Create statistical charts

# Para executar:
# python -m streamlit run "G:\Meu Drive\Cursos\Python\MachineLearning\0806b.py"
# python -m streamlit run C:\Users\Roger\Documents\GitHub\RogerTangRT\Colab\MachineLearning\0806b.py

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris_data = load_iris()

data = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)

fig = plt.figure()
sns.histplot(data=data, bins=20)
st.pyplot(fig)

fig = plt.figure()
sns.boxplot(data=data)
st.pyplot(fig)

fig = plt.figure()
sns.scatterplot(data=data)
st.pyplot(fig)