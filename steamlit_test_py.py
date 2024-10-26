import streamlit as st

# 创建文件上传组件

# 自定义侧边栏的CSS样式
def sidebar_style():
    st.markdown("""
    <style>       
    [data-testid="stSidebar"] {
        background-color: #ffebcd;
        color: white;
    }
    [data-testid="stSidebar"] .css-1q8dd3e {
        background-color: #404040;
        color: white;
    }
    [data-testid="stSidebar"] a {
        color: white;
        text-decoration: none;
    }
    [data-testid="stSidebar"] a:hover {
        text-decoration: underline;
    }
    [data-testid="stSidebar"] .css-1d391kg {
        color: white;
    }
    [data-testid="stSidebar"] .css-1y4p8pa {
        color: white;
    }
    [data-testid="stSidebar"] .st-bb {
        border-bottom-color: white;
    }
    [data-testid="stSidebar"] .st-at {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 应用自定义侧边栏样式
pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")])
 
sidebar_style()

pg.run()

