import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
# Streamlit页面标题
st.title('最小二乘法处理')

# 设置表格的列数
num_columns = st.number_input('请输入表格的列数（至少为2）:', min_value=2, value=10, step=1)

# 设置表格的行数
num_rows = st.number_input('请输入表格的行数（至少为1）:', min_value=1, value=6, step=1)

# Create column names for DataFrame
columns = ['Y'] + [f'X{i}' for i in range(1, num_columns)]
# Create row names
row_names = [f'row{i+1}' for i in range(num_rows)]

# Check if saved data exists in session state
if 'saved_data' in st.session_state:
    saved_data = st.session_state['saved_data']
    # Adjust DataFrame dimensions if row or column count has changed
    if saved_data.shape != (num_rows, num_columns):
        # Create a new DataFrame with the updated dimensions
        new_df = pd.DataFrame(index=row_names, columns=columns)
        # Copy data from the saved DataFrame to the new DataFrame as much as possible
        min_rows = min(saved_data.shape[0], num_rows)
        min_cols = min(saved_data.shape[1], num_columns)
        new_df.iloc[:min_rows, :min_cols] = saved_data.iloc[:min_rows, :min_cols]
        # Update session state with the adjusted DataFrame
        st.session_state['saved_data'] = new_df
else:
    # Initialize session state data if it doesn't exist
    st.session_state['saved_data'] = pd.DataFrame(index=row_names, columns=columns)

# Display and edit the DataFrame
st.write('Please enter data:')
edited_df = st.data_editor(st.session_state['saved_data'], key='data_editor')

# Update session state with the edited data
if st.button('保存数据'):
    st.session_state['saved_data'] = edited_df
    st.success('Data has been saved!')



def LSM(edited_df):
    # 如果用户提交了数据
    if edited_df is not None:
        # 确保数据不为空
        if not edited_df.empty:
            try:
                # 删除空列
                edited_df = edited_df.dropna(axis=1, how='all')
                # 删除空行
                edited_df = edited_df.dropna(axis=0, how='all')
                # 将数据转换为numpy数组
                data = edited_df.values.astype(float)  # 确保所有数据都是浮点数类型
                print(data)
                # 分离因变量和自变量
                y = data[:, 0]
                X = data[:, 1:]

                # 执行最小二乘法
                beta, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)
                
                results_df = pd.DataFrame({
                    'Parameter': ['参数向量', '残差', '矩阵的秩', 's'],
                    'Value': [beta, residuals, rank, s]
                })
                st.write('计算结果：')
                st.write(results_df)
            except ValueError as e:
                st.error('数据包含非数值类型，请确保所有输入都是数值。')
                st.write(e)
        else:
            st.write('请输入有效的数据。')
    else:
        st.write('请输入数据。')


if st.button('运行最小二乘法'):
    LSM(edited_df)
