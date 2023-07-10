import os
import pandas as pd
#删除csv表格的标题行与第一列并转换为'.xlsx'格式
folder_path = 'D:\远程教学\硕士毕业设计\模式识别\津发科技采集数据处理\周豪_处理完成'

# 遍历文件夹中的所有csv文件
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)

        # 读取csv文件，不包括标题行
        df = pd.read_csv(file_path, header=None, skiprows=1)

        # 删除第一列
        df = df.iloc[:, 1:]

        # 保存修改后的xlsx文件
        new_file_path = os.path.splitext(file_path)[0] + '.xlsx'
        df.to_excel(new_file_path, index=False, header=False)
