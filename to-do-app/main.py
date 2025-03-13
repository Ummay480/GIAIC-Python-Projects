import streamlit as st

st.title("To-Do List 📝")
tasks = []

task = st.text_input("Add a new task:")
if st.button("Add Task"):
    tasks.append(task)

st.subheader("Your Tasks:")
for t in tasks:
    st.write(f"✅ {t}")



