import streamlit as st

# 定义导航链接的函数，返回 HTML 格式的链接
def navigation_link(url, label):
    return f"""
    <a href="{url}" target="_blank" 
       style="text-decoration: none; color: #000; 
              background-color: #fff; padding: 8px 12px; 
              margin-right: 10px; border-radius: 5px;">
        {label}
    </a>
    """

# Streamlit 主页内容
def main():
    st.markdown(
        """
        <style>
        .title {
            text-align: center;
            font-size: 2em;
            margin-bottom: 20px;
        }
        .nav-pills {
            text-align: center;
            margin-bottom: 20px; /* 设置页边距 */
        }
        .nav-pills a {
            margin: 0 10px;
            display: inline-block; /* 确保链接在同一行显示 */
            margin-bottom: 10px; /* 设置行间距 */
        }
        </style>
        <div class="title">网址导航页面</div>
        """,
        unsafe_allow_html=True
    )

    # 生成带有超链接的列表项
    links = [
        ('https://www.google.com', 'Google'),
        ('https://www.github.com', 'GitHub'),
        ('https://www.twitter.com', 'Twitter'),
        ('https://www.facebook.com', 'Facebook'),
        ('https://www.someacg.top', 'SomeACG'),
        ('https://sm.ms/','Image_Upload'),
        ('https://postimages.org/','PostImage'),
        ('https://wallhere.com/zh','WallHere'),
        ('https://www.vpnbook.com/','VPNBook'),
        ('https://missing-semester-cn.github.io/','计算机教育'),
        ('https://www.hhduc.com/','盗版电影'),
        ('https://courses.d2l.ai/zh-v2/','动手学深度学习'),
        ('https://www.stpaper.cn/','中国科讯'),
        ('https://www.wolframalpha.com/calculators/integral-calculator','积分计算器'),
        ('https://www.wolframalpha.com/','WolframAlpha计算引擎'),
        ('https://ac.scmor.com/','谷歌学术镜像')
    ]

    # 将链接转换为 HTML 格式
    links_html = '<div class="nav-pills">' + ' | '.join([navigation_link(url, label) for url, label in links]) + '</div>'

    # 使用 CSS 样式将链接排成一行
    st.markdown(links_html,unsafe_allow_html=True)

main()



