if not df.empty:
    st.divider()#separator
    avg_grade = calculate_stats(df)
    col1, col2 = st.columns(2)
    with col1:
        sts.metric(label="Average class Grade", value= f"{avg_grade:.2f}%")
    with col2:
        sts.metric(label="Total Students", value= len(df))
        #display the interactive table
        st.subheader("Student Grade List")
        st.dataframe(df, use_container_width = True)#

