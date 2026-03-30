import pandas as pd
import streamlit as st


def calculate_stats(df):
    """Calculates summary statistics from the grade dataframe."""
    if df.empty:
        return 0, 0, 0
    avg = df["Grade"].mean()
    high = df["Grade"].max()
    low = df["Grade"].min()
    return avg, high,low




def get_grade_distribution(df):
    return df["Grade"].value_counts().sort_index()