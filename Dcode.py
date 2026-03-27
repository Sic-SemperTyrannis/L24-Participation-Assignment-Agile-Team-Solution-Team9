#Part D
    st.subheader("Grade Distribution")
    dist_data = logic.get_grade_bins(df)
    st.bar_chart(dist_data)
    
    st.subheader("Current Roster")
    st.dataframe(df, use_container_width=True)
    
