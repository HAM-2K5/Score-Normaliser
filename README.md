# 📊 Subject Score Normalization Dashboard

A Streamlit app to analyze and compare normalized student scores across categories and subjects.

## 🚀 Features
- Upload CSV with subject and exam scores
- Normalize subject scores by category
- Set custom weights for Physics, Chemistry, and Math
- View bar charts, line graphs, and final scores

## 📁 Sample CSV Format

```csv
StudentID,Category,Physics,Chemistry,Math,Exam2
S1,A,88,85,78,75
S2,A,72,70,74,80
S3,B,60,65,67,85
S4,B,90,88,92,70
S5,C,55,60,58,60
S6,C,75,80,85,90
```

## 🔧 Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the App

```bash
streamlit run subject_dashboard.py
```

## 🌐 Deploy Online

Push this repo to GitHub and deploy on [Streamlit Cloud](https://streamlit.io/cloud)
