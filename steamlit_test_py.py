import streamlit as st

# 创建文件上传组件

pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")])
pg.run()

