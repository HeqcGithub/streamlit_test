import numpy as np
from scipy import stats
import pandas as pd
#C:\Users\xiaohe\AppData\Roaming\Python\Python39\Scripts   numpy路径


def bessel_correction_np(data):

    statistics = {
        'sample_mean': np.nanmean(data),
        'sample_std_dev': np.nanstd(data, ddof=1),
        'sample_variance': np.nanvar(data, ddof=1),
        'median_value': np.nanmedian(data),
        'min_value': np.nanmin(data),
        'max_value': np.nanmax(data)
    }
    return statistics



def leyda_criterion(data):
    print("******伊莱达检验*******")
    all_outliers = []
    while True:
        outliers = []
        statistics = bessel_correction_np(data)
        mean=statistics['sample_mean']
        std_dev=statistics['sample_std_dev']
        for value in data:
            if abs(value - mean) > 3 * std_dev:
                outliers.append(value)
        if not outliers:
            break
        data = [value for value in data if value not in outliers]
        all_outliers.extend(outliers)
        #outliers1 = ", ".join(f"误差值：{num:.3f}" for num in outliers)
    cleaned_data = [value for value in data if value not in all_outliers]
    return all_outliers,cleaned_data

def grubbs_test(data,alpha=0.05):
 
    # Calculate the Grubbs' statistic for the maximum and minimum values
    all_outliers = []
    while True:
        
        n = len(data)
        statistics = bessel_correction_np(data)
        mean=statistics['sample_mean']
        std_dev=statistics['sample_std_dev']
        g_max = np.abs(np.max(data) - mean) / std_dev
        g_min = np.abs(np.min(data) - mean) / std_dev
        g_calc = max(g_max, g_min)

        # Calculate the critical G value
        t_dist = stats.t.ppf(1 - alpha / (2 * n), df=n-2)
        g_crit = ((n - 1) * np.sqrt(np.square(t_dist))) / (np.sqrt(n) * np.sqrt(n - 2 + np.square(t_dist)))
      
        # Determine if there is an outlier
        if g_calc > g_crit:
            outlier_max = np.max(np.abs(data - mean))
            outlier_mask = np.abs(data - mean) == outlier_max #outlier_mask为bool型
            outlier_index = np.where(outlier_mask)[0]
            for index in outlier_index:
                all_outliers.append(data[index])
            data = [value for value in data if value not in all_outliers]
        else:
            break
    cleaned_data = [value for value in data if value not in all_outliers]
    return all_outliers,cleaned_data
           

def dixon_test(data, alpha=0.05):

    print("******迪克逊检验*******")
    outliers = []
    while True:    
        n = len(data)
        sorted_data = np.sort(data)

        # 计算各种Q值
        max10 = (sorted_data[n-1] - sorted_data[n-2]) / (sorted_data[n-1] - sorted_data[0])
        max11 = (sorted_data[n-1] - sorted_data[n-2]) / (sorted_data[n-1] - sorted_data[1])
        max21 = (sorted_data[n-1] - sorted_data[n-3]) / (sorted_data[n-1] - sorted_data[1])
        max22 = (sorted_data[n-1] - sorted_data[n-3]) / (sorted_data[n-1] - sorted_data[2])
    
        min10 = (sorted_data[0] - sorted_data[1]) / (sorted_data[0] - sorted_data[n-1])
        min11 = (sorted_data[0] - sorted_data[1]) / (sorted_data[0] - sorted_data[n-2])
        min21 = (sorted_data[0] - sorted_data[2]) / (sorted_data[0] - sorted_data[n-2])
        min22 = (sorted_data[0] - sorted_data[2]) / (sorted_data[0] - sorted_data[n-3])
        # 获取临界值（可查表或使用统计软件获取）
        # 这里假设使用
        critical_value =0.406

        
        if n<= 7:
            if max10 > critical_value:
                outliers.append(sorted_data[n-1])
                
            elif min10 > critical_value:
                outliers.append(sorted_data[0])
                
            else:
                break
        elif (n>7 and n<=10):
            if max11 > critical_value:
                outliers.append(sorted_data[n-1])
                
            elif min11 > critical_value:
                outliers.append(sorted_data[0])
                
            else:
                break
        elif (n>10 and n<=13):
            print(10,13)
            if max21 > critical_value:
                outliers.append(sorted_data[n-1])
                
            elif min21 > critical_value:
                outliers.append(sorted_data[0])
                
            else:
                break
        elif n>=14:
            print (14)
            print (max22,min22)
            if max22 > critical_value:
                outliers.append(sorted_data[n-1])
               
            elif min22 > critical_value:
                outliers.append(sorted_data[0])
               
            else:
                break
        data = [value for value in data if value not in outliers]
    #outliers3 = ", ".join(f"误差值：{num:.3f}" for num in outliers)
    cleaned_data = [value for value in data if value not in outliers]
    print(outliers)
    return outliers,cleaned_data

def plot_function(data, outliers,ax):
    ax.clear()
    data_index = np.arange(len(data))
    ax.scatter(data_index,data,s=50)
    outlier_indices = []
    if outliers:
        mid_data = data.copy()
        for outlier in outliers:
            indices = np.where(mid_data == outlier)[0]
            outlier_indices.append(indices[0])
            mid_data[indices[0]] = np.nan   #将使用过的索引置为nan
    print(outlier_indices,outliers)
    ax.scatter(outlier_indices, outliers, color='red', marker='x',s=100)
    ax.set_xlabel('number',fontsize=15)
    ax.set_ylabel('value',fontsize=15)



















    


