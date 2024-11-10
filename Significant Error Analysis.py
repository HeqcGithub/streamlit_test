import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from python1 import bessel_correction_np,leyda_criterion,grubbs_test,dixon_test,plot_function

uploaded_file = st.file_uploader("Upload the data file that needs to be analyzed", type=["csv", "xlsx"])

def read_file(uploaded_file):
    try:
        if uploaded_file.type == 'text/csv':
            return pd.read_csv(uploaded_file)
        elif uploaded_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            return pd.read_excel(uploaded_file) 
        raise ValueError('The file type is not supported')
    except Exception as e:
        st.error(f"file reading failure:{e}")
        return None

def main():
    # 判断是否有文件上传
    if uploaded_file is not None:
        # 根据文件类型读取数据
        # 读取数据  
        df = read_file(uploaded_file)
        data = df.values
        data = data[~np.isnan(data)]
       
        criterion = st.selectbox("选择异常检测方法", ["莱伊达准则", "格拉布斯准则", "迪克逊准则"])
        if criterion == "莱伊达准则":
                 outliers,cleaned_data = leyda_criterion(data)
        elif criterion == "格拉布斯准则":
                 alpha = st.slider('选择显著性水平 (0.01 to 0.10)', 0.01, 0.10, 0.05, step=0.01)
                 outliers,cleaned_data = grubbs_test(data,alpha)  # 设置显著性水平
        elif criterion == "迪克逊准则":
                 outliers,cleaned_data = dixon_test(data, alpha=0.05)
        
        
        #绘制散点图
        fig, ax = plt.subplots()
        plot_function(data, outliers,ax)

        fig1,ax1 = plt.subplots()
        plot_function(cleaned_data,[],ax1)


        #数据格式转换
        cleaned_data = np.array(cleaned_data,dtype=float)
        # pad_arry = np.pad(cleaned_data, (0, 10 - len(cleaned_data) % 10), 'constant', constant_values=(np.nan,))
        # cleaned_data_arr = pad_arry.reshape(-1,10)
        #data_len = len(data_len)
        df_col_len = df.shape[1]
        pad_with = df_col_len - len(cleaned_data)%df_col_len
        if pad_with > 0:
            pad_arry = np.pad(cleaned_data,(0,pad_with),'constant',constant_values=np.nan)
        else:
            pad_arry = cleaned_data
        reshape_arry = pad_arry.reshape(-1,df_col_len)
        cleaned_data_df = pd.DataFrame(reshape_arry)
        
        #
        cleaned_data_df = pd.DataFrame(cleaned_data_df)
        new_column_labels = [f'Colum {i+1}' for i in range(df_col_len)]
        cleaned_data_df.columns = new_column_labels
        
        col1,col2 = st.columns(2)
        with col1:
            st.title('Original data')
            st.dataframe(df,height=300)
            st.pyplot(fig)
        with col2:
            st.title('Processed data')
            st.dataframe(cleaned_data_df,height=300) 
            st.pyplot(fig1)
         
         # 展示数据的统计量
        statistics = bessel_correction_np(data)
        stats_cleaned = bessel_correction_np(cleaned_data)
        st.subheader('数据的统计量')
        st.write(pd.DataFrame([statistics,stats_cleaned],index=['原始数据','处理后数据']))
#if __name__ == '__main__':
main()