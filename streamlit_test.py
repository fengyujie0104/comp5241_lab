import streamlit as st

# 创建输入框和提交按钮
user_input = st.text_input("请输入一些内容:")
submit_button = st.button("提交")

# 处理用户输入
if submit_button:
    st.write(f"你输入的内容是: {user_input}")