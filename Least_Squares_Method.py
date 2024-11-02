import streamlit as st
import numpy as np

# Streamlit页面标题
st.title('最小二乘法计算')

# 输入数据的表单
st.write('请输入数据以进行线性回归分析：')

# 获取用户输入的数据点数量
rows = st.number_input('请输入数据点的数量:', min_value=2, value=2)
def main():
    # 使用session_state来存储输入数据
    if 'X_data' not in st.session_state:
        st.session_state['X_data'] = []
    if 'y_data' not in st.session_state:
        st.session_state['y_data'] = []

    # 输入数据点的表单
    for i in range(rows):
        x_values = st.text_input(f'输入第{i+1}个数据点的自变量值（以逗号分隔）:', key=f'x_values_{i}')
        y_value = st.number_input(f'输入第{i+1}个数据点的因变量值:', format="%f", key=f'y_value_{i}')

    # 清除数据按钮
    if st.button('清除数据'):
        st.session_state['X_data'] = []
        st.session_state['y_data'] = []

    # 当用户点击按钮时，处理输入数据并计算最小二乘解
    if st.button('计算最小二乘解'):
        for i in range(rows):
            x_values = st.session_state.get(f'x_values_{i}', '')
            y_value = st.session_state.get(f'y_value_{i}', None)
            
            # 将输入的值存储到session_state中
            try:
                x_values_list = [float(v) for v in x_values.split(',')]  # 添加截距项
                st.session_state['X_data'].append(x_values_list)
                st.session_state['y_data'].append(y_value)
            except ValueError:
                # 如果转换失败，显示错误信息
                st.error(f'在第{i+1}个数据点的自变量值输入有误，请确保输入的是逗号分隔的数字。')
                st.session_state['X_data'] = []  # 清除错误数据
                st.session_state['y_data'] = []
                break  # 退出循环

        # 确保有足够的数据点进行计算
        if len(st.session_state['X_data']) >= 2 and len(st.session_state['y_data']) >= 2:
            # 将输入数据转换为NumPy数组
            X = np.array(st.session_state['X_data'])
            y = np.array(st.session_state['y_data'])
            print(X,y)
            # 使用NumPy的linalg.lstsq方法求解最小二乘问题
            beta, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)
            
            # 显示结果
            st.write('计算结果：')
            st.write('参数向量 beta:', beta)
            st.write('残差向量 residuals:', residuals)
            st.write('矩阵X的秩 rank:', rank)
            st.write('奇异值 s:', s)
        else:
            st.error('没有足够的数据点进行最小二乘法计算。')

main()
