from dataclasses import dataclass
import os, re, struct
import numpy as np
#将边序号生成大图序号
dir1_1 = open("scrap/edges0.1.txt","r")
dir1_2 = open("scrap/edges0.2.txt","r")
dir2 = open("scrap/num_sum_nodes3.txt","r")
f1 = open("scrap/edges0.11.txt", "w")
f2 = open("scrap/edges0.21.txt", "w")
lines1 = dir1_1.readlines()
lines2 = dir2.readlines()
lines3 = dir1_2.readlines()

data2 = []
data1 = []
data3 = []
i=0

for line2 in lines2:
    data2.append(int(line2))#得到第二个文件的数据，存在一个一维数组里面

i=0
for line1 in lines1:
    dataline1 = []
    line1 = line1.replace("  ", " ")
    line1 = line1.replace("  ", " ")
    line_num = line1.count(" ") + 1 #得到每一行数字的个数
    for j in range(line_num):
        data = int(line1.split()[j]) + data2[i] #将读取到的数据变成int型
        dataline1.append(data)

    i=i+1
    data1.append(dataline1)
print(data1,file=f1)
a = 0
for line3 in lines3:
    dataline2 = []
    line3 = line3.replace("  "," ")
    line3 = line3.replace("  ", " ")
    line_num = line3.count(" ") + 1 #得到每一行数字的个数
    for j in range(line_num):
        data = int(line3.split()[j]) + data2[a] #将读取到的数据变成int型
        dataline2.append(data)

    a = a+1
    data3.append(dataline2)
print(data3,file=f2)


def updateFile1(file, old_str, new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:旧字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r") as f:
        for line in f:
            line = line.replace(old_str, new_str)
            line = (line.lstrip())
            file_data += line
    with open(file, "w") as f:
        f.write(file_data)
#处理边1
updateFile1(r"scrap/edges0.11.txt","[", "")
updateFile1(r"scrap/edges0.11.txt","]", "")
updateFile1(r"scrap/edges0.11.txt",",", "\n")
#处理边2
updateFile1(r"scrap/edges0.21.txt","[", "")
updateFile1(r"scrap/edges0.21.txt","]", "")
updateFile1(r"scrap/edges0.21.txt",",", "\n")

#合并成adj
with open("scrap/edges0.21.txt") as xh:
  with open('scrap/edges0.11.txt') as yh:
    with open("compound_nr/compound_A_nr.txt","w") as zh:
      xlines = xh.readlines()
      ylines = yh.readlines()
      #Combine content of both lists
      #combine = list(zip(ylines,xlines))
      #Write to third file
      for i in range(len(xlines)):
        line = ylines[i].strip() + ' ' + xlines[i]
        zh.write(line)
updateFile1(r"compound_nr/compound_A_nr.txt","  ", " ")
updateFile1(r"compound_nr/compound_A_nr.txt"," ", ",")