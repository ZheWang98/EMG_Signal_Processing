from scipy.signal import butter, lfilter, iirnotch#spicy的signal模块可以进行滤波操作
import pandas as pd#文件操作
import matplotlib.pyplot as plt#画图
import pywt#小波库
import numpy as np
from sklearn.metrics import mean_squared_error
import math
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# 读取xlsx文件
file_path = 'D:\远程教学\硕士毕业设计\模式识别\津发科技采集数据处理\陈赫_C1-C4_Processed\侧边1通道.xlsx'
df = pd.read_excel(file_path)
signal = df['signal'].values

# 假设你已经从xlsx文件中读取了信号数据，并将其存储在一个名为signal的numpy数组中
plt.plot(signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Raw Signal')
plt.show()

# 设定采样率和截止频率
fs = 1000.0
lowcut = 30.0
highcut = 450.0
sEMG_l = len(signal)
# 对信号进行带通滤波
filtered_signal = butter_bandpass_filter(signal, lowcut, highcut, fs)

# 设定陷波频率和品质因数
f0 = 50.0
Q = 30.0

# 设计陷波滤波器
b, a = iirnotch(f0, Q, fs)

# 对信号进行陷波滤波
filtered_signal = lfilter(b, a, filtered_signal)

# 设定小波基、分解层数和阈值方法
wavelet = 'sym7'
level = 2
threshold_method = 'hard'

# 对信号进行小波分解
coeffs = pywt.wavedec(filtered_signal, wavelet, level=level)

# 计算阈值
sigma = np.median(np.abs(coeffs[-1])) / 0.6745
threshold = sigma * np.sqrt(2 * np.log(len(filtered_signal)))

# 对小波系数进行阈值处理
coeffs[1:] = [pywt.threshold(c, threshold, mode=threshold_method) for c in coeffs[1:]]

# 对信号进行小波重构
denoised_signal = pywt.waverec(coeffs, wavelet)

# 创建一个新的数据帧
df = pd.DataFrame({'signal': denoised_signal})

# 将数据帧保存为新的xlsx文件
df.to_excel('denoised_signal.xlsx', index=False)

plt.plot(denoised_signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Denoised Signal')
plt.show()

# 计算均方误差(MSE)，以评价降噪后的信号质量，MSE越小越好
mse = np.sqrt(np.sum((signal - denoised_signal) ** 2) / sEMG_l)
print(f'MSE: {mse}')

# 计算信噪比(SNR), 以评价所选小波基以及层数的优劣
SNR = 10 * np.log10((np.sum(denoised_signal ** 2) / sEMG_l) / (np.sum((signal - denoised_signal) ** 2) / sEMG_l))
print(f"SNR: {SNR}")