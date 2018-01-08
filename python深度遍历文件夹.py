# 导入os collection模块

import os
import collections

# 创建一个getAllDirAndFile函数,来进行深度遍历文件目录的具体操作,有参函数getAllDirAndFile的形参为sourcePath
def getAllDirAndFile(sourcePath):
# 首先判断要遍历的总的文件夹是否存在
  if not os.path.exists(sourcePath): # 如果该文件目录不存在
    return # return结束运行
  queue = collections.deque() #如果存在,则创建一个队列来存放路径
  queue.append(sourcePath) #将根路径放入队列
  
  #不停的从队列中取
  while True:
  #判断,当队列中没有路径时,证明遍历完了,则结束循环
  if len(queue)<0:
    break
 
  path = queue.pop() #将队列中的路径取出来
  # 遍历path
  for fileName in os.listdir(path):
    #拼接成绝对路径
    absPath = os.path.join(path,fileName)
    if os.path.isfile(absPath):
      print("fileName:%s''%(absPath))
    if os.path.isdir(absPath):
      #如果是目录,则放到队列中 去
      queue.append(absPath)
   # 测试
   if __name__ == "__main__":
    path = r"f\myproject"
    getAllDirAndFile(path)
    
