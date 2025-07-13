import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Subject Score Dashboard", layout="wide")
st.title("📊 Student Subject-wise Performance Dashboard")

# File upload
uploaded_file = st.sidebar.file_uploader("📤 Upload CSV File", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.warning("Upload a CSV file to continue. Using sample data for now.")
    df = pd.read_csv("sample_data.csv")

# Subject weights
st.sidebar.title("⚖️ Subject Weights")
subjects = ['Physics', 'Chemistry', 'Math']
weights = {}
for subject in subjects:
    weights[subject] = st.sidebar.slider(f"{subject}", 0.0, 1.0, 0.33)

# Normalize scores per category
for subject in subjects:
    norm_col = subject + '_Norm'
    norm_scores = []
    for category in df['Category'].unique():
        cat_df = df[df['Category'] == category]
        min_score = cat_df[subject].min()
        max_score = cat_df[subject].max()
        if max_score == min_score:
            cat_norm = [100] * len(cat_df)
        else:
            cat_norm = 100 * (cat_df[subject] - min_score) / (max_score - min_score)
        norm_scores.extend(cat_norm)
    df[norm_col] = norm_scores

# Compute weighted Exam1 + FinalScore
df['Exam1_Normalized'] = sum(df[sub + '_Norm'] * weights[sub] for sub in subjects)
df['FinalScore'] = 0.5 * df['Exam1_Normalized'] + 0.5 * df['Exam2']

# Display table
st.subheader("📄 Final Score Table")
st.dataframe(df[['StudentID', 'Category', 'Exam1_Normalized', 'Exam2', 'FinalScore']])

# Charts
for subject in subjects:
    st.subheader(f"📈 {subject} Normalized Scores by Category")
    fig = px.bar(df, x='Category', y=subject + '_Norm', color='Category', barmode='group')
    st.plotly_chart(fig, use_container_width=True)

# Line chart comparing subjects
st.subheader("📊 Subject Comparison Per Student")
df_melted = df.melt(id_vars=['StudentID'], value_vars=[s + '_Norm' for s in subjects],
                    var_name='Subject', value_name='Normalized Score')
df_melted['Subject'] = df_melted['Subject'].str.replace('_Norm', '')
fig2 = px.line(df_melted, x='StudentID', y='Normalized Score', color='Subject', markers=True)
st.plotly_chart(fig2, use_container_width=True)
