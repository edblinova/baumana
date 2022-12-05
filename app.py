from secrets import choice
import streamlit as st
import pandas as pd
import os
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pycaret.classification import save_model, setup, compare_models, pull 


with st.sidebar:
    st.title("AutoStreamML")
    choice = st.radio("NAVIGATION", ["Upload", "Profiling", "ML", "Download"])
    st.info("Это приложение основанное на Streamlit и Catboost. Для решения задач классификации.")


if os.path.exists("source.csv"):
    df = pd.read_csv("source.csv", index_col=None)

if choice == "Upload":
    st.title("Upload Your Data For Modelling 🎯")
    file = st.file_uploader("🎲 Upload Your Dataset Here")
    if file:
        df = pd.read_csv(file, index_col=None)
        df.to_csv("source.csv", index=None)
        st.dataframe(df)

if choice == "Profiling":
    st.title("Automated EDA 🏆")
    profile_report = df.profile_report()
    st_profile_report(profile_report)

if choice == "ML":
    st.title("✅ Machine Learning go >>> 🌟")
    target = st.selectbox("Select your target ▶", df.columns)
    if st.button("Train model 🔥"):
        setup(df, target=target)
        setup_df = pull()
        st.info("This is the ML Experiment ☣")
        st.dataframe(setup_df)
        best_model = compare_models()
        compare_df = pull()
        st.info("This is th ML Model ❂")
        st.dataframe(compare_df)
        save_model(best_model, "best_model")

if choice == "Download":
    with open("best_model.pkl", "rb") as f:
        st.download_button("Download the predictions", f, "trained_model.pkl")
