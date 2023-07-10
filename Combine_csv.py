import pandas as pd
import os
#将文件夹中每一个excel文件合并
# 指定多个csv文件所在的目录
csv_dir = 'D:\远程教学\硕士毕业设计\模式识别\津发科技采集数据\李杰_处理完成\新建文件夹'

# 获取目录下所有csv文件的文件名
file_names = os.listdir(csv_dir)
file_names.sort(key=lambda x:int(x.split('.')[0]))
print(file_names)
# 存储所有csv文件数据的列表
data_list = []

# 循环读取每个csv文件的数据并添加到data_list列表中
for file_name in file_names:
    if file_name.endswith('.csv'):
        file_path = os.path.join(csv_dir, file_name)
        data = pd.read_csv(file_path)
        data_list.append(data)

# 使用pandas的concat函数将所有数据按行合并为一个DataFrame对象
all_data = pd.concat(data_list, axis=0)

# 将合并后的所有数据保存为一个csv文件
all_data.to_csv('指向4通道.csv', index=False)
