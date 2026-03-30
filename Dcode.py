#Part D
    c1, c2, c3 = st.columns(3)
    c1.metric("Average", f"{avg:.1f}")
    c2.metric("Highest", int(high))
    c3.metric("Lowest", int(low))
   
    st.subheader("Grade Distribution")
    dist_data = logic.get_grade_bins(df)
    st.bar_chart(dist_data)
    
    st.subheader("Current Roster")
    st.dataframe(df, use_container_width=True)


