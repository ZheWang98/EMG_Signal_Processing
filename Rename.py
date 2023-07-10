import os
import re
#批量重命名文件夹内文件
list1 =[]
path = r'D:\远程教学\硕士毕业设计\模式识别\津发科技采集数据\李杰_处理完成\新建文件夹'#要进行批量修改文件名的文件夹位置
filelist = os.listdir(path)
i = 0
for file in filelist:
    pattern = ')'#想要删掉的字符串
    oldname = path + '\\' + filelist[i]
    newname = path + '\\' + filelist[i].replace(pattern, '')
    os.rename(oldname, newname)
    i += 1