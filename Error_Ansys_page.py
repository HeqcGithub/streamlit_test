import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from python1 import bessel_correction_np,leyda_criterion,grubbs_test,dixon_test,plot_function

uploaded_file = st.file_uploader("上传数据文件", type=["csv", "xlsx"])

def main():
    # 判断是否有文件上传
    if uploaded_file is not None:
        # 根据文件类型读取数据
        # 读取数据  
        try:
            df = pd.read_csv(uploaded_file)
       
        except Exception as e:
            st.error(f"读取文件失败：{e}")
        else:
            data = df.values
            data = data[~np.isnan(data)]
            mean,std_dev = bessel_correction_np(data)
            print(mean,std_dev)
            criterion = st.selectbox("选择异常检测方法", ["莱伊达准则", "格拉布斯准则", "迪克逊准则"])
            if criterion == "莱伊达准则":
                    outliers,cleaned_data = leyda_criterion(data)
            elif criterion == "格拉布斯准则":
                    outliers,cleaned_data = grubbs_test(data,alpha=0.05)  # 设置显著性水平
            elif criterion == "迪克逊准则":
                    outliers,cleaned_data = dixon_test(data, alpha=0.05)
            
            st.write(df)
            #绘制散点图
            fig, ax = plt.subplots()
            plot_function(data, outliers,ax)
            st.pyplot(fig)
            #数据格式转换
            cleaned_data = np.array(cleaned_data)
            pad_arry = np.pad(cleaned_data, (0, 10 - len(cleaned_data) % 10), 'constant', constant_values=(np.nan,))
            cleaned_data_arr = pad_arry.reshape(-1,10)
            cleaned_data_df = pd.DataFrame(cleaned_data_arr)
            new_column_labels = ['Colum 1', 'Colum 2', 'Colum 3', 'Colum 4', 'Colum 5',
                     'Colum 6', 'Colum 7', 'Colum 8', 'Colum 9', 'Colum 10']
            cleaned_data_df.columns = new_column_labels
            st.write(cleaned_data_df)
                
#if __name__ == '__main__':
main()
