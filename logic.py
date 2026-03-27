import pandas as pd
import streamlit as st

def calculate_stats(df):
    return {
        "Average": df["Grade"].mean(),
        "Max": df["Grade"].max(),
        "Min": df["Grade"].min()
    }

def get_grade_distribution(df):
    return df["Grade"].value_counts().sort_index()