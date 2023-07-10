import os
#当前50个文件名为1-50，此文件更改为50-1(原来的1，现在是50)
folder_path = 'D:\远程教学\硕士毕业设计\模式识别\津发科技采集数据\李杰_处理完成\新建文件夹' # 更改为文件夹的路径
extension = '.csv' # 更改为文件的扩展名

# 首先将文件重命名为临时名称
for i in range(1, 51):
    old_name = os.path.join(folder_path, str(i) + extension)
    new_name = os.path.join(folder_path, 'temp' + str(i) + extension)
    os.rename(old_name, new_name)

# 然后按照倒序重命名文件
for i in range(1, 51):
    old_name = os.path.join(folder_path, 'temp' + str(i) + extension)
    new_name = os.path.join(folder_path, str(51-i) + extension)
    os.rename(old_name, new_name)
