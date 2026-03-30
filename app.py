import pandas as pd
import streamlit as st
import logic

#######################    
def get_grade_bins(df):
    """Categorizes grades into letter brackets for plotting."""
    if df.empty:
        return pd.Series(dtype=int)
    bins = [0, 60, 70, 80, 90, 100], 
    labels = ['F', 'D', 'C', 'B', 'A'],
    return pd.cut(df['Grade'], bins=bins, labels=# placeholder).value_counts().sort_index()
    
########################    
    # Initialize Data Store
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Student", "Grade"])
    
    # Sidebar:  (Input UI)
with st.sidebar:
    st.header("Entry Form")
    name = st.text_input("Student Name")
    score = st.number_input("Score", 0, 100, 85)
    if st.button("Add Student"):
        new_entry = pd.DataFrame({"Student": [name], "Grade": [score]})
        st.session_state.data = pd.concat([st.session_state.data, new_entry], ignore_index=True)

#########################
 # Main Dashboard
if not st.session_state.data.empty:
    df = st.session_state.data
    
    # Logic Integration
    avg, high, low = logic.calculate_stats(df)
    

else:
    st.info("No data available. Use the sidebar to add students.")
    
#####################    
    # Visual Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Average", f"{avg:.1f}")
    c2.metric("Highest", int(Max))
    c3.metric("Lowest", int(Min))
    
    # Visualization
    st.subheader("Grade Distribution")
    dist_data = logic.get_grade_bins(df)
    st.bar_chart(dist_data)
    
    st.subheader("Current Roster")
    st.dataframe(df, use_container_width=True)
