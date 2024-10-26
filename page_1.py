import streamlit as st

def set_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 主函数
def background():
    # 设置背景图片，这里使用的是一个网络链接，你可以替换为本地图片路径
    image_url = "https://i.postimg.cc/T3qPM9Mq/origin5ceb58b6e7bce720f6f0165f.jpg"
    set_background_image(image_url)
    
    # Streamlit 应用内容
    st.title('Welcome to my Streamlit app with a background image!')
    # ... 其他内容 ...

background()