# 开发时间：2022/4/12 16:18
import re
import os
'''
获取节点特征数据\边特征数据\节点，转化成图神经网络需要的形式
'''
def updateFile(file,file1, old_str, new_str):
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
    with open(file1, "w") as f:
        f.write(file_data)

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
###节点特征数据
updateFile(r"scrap/ndata.txt","scrap/ndata1.txt","{'x': tensor([", "")
updateFile1(r"scrap/ndata1.txt","[", "")
updateFile1(r"scrap/ndata1.txt","]], dtype=torch.float64)}", "")
updateFile1(r"scrap/ndata1.txt","]", ",")
updateFile1(r"scrap/ndata1.txt",",,", "")
updateFile(r"scrap/ndata1.txt","compound_nr/compound_node_labels_nr.txt",",\n", ",")
updateFile1(r"compound_nr/compound_node_labels_nr.txt",",  ", ",")
updateFile1(r"compound_nr/compound_node_labels_nr.txt",",dtype=torch.float64)}", "")
updateFile1(r"compound_nr/compound_node_labels_nr.txt"," ", "")
updateFile1(r"compound_nr/compound_node_labels_nr.txt",",", " ")
####边特征数据
updateFile(r"scrap/edata.txt","scrap/edata1.txt","{'w': tensor([[", "")
updateFile1(r"scrap/edata1.txt","[", "")
updateFile1(r"scrap/edata1.txt","]])}", "")
updateFile1(r"scrap/edata1.txt","],", ",")
updateFile(r"scrap/edata1.txt","compound_nr/compound_edata_nr.txt",",", "")
###节点
updateFile(r"scrap/nodes.txt","scrap/nodes1.txt","tensor([", "")
updateFile1(r"scrap/nodes1.txt",")", "")
updateFile1(r"scrap/nodes1.txt",",", "\n")
updateFile(r"scrap/nodes1.txt","compound_nr/nodes.txt","]", "")
###生成大图序号
f = open("compound_nr/compound_graph_indicator_nr.txt", "w")  # 打开文件以便写入
with open("compound_nr/nodes.txt","r") as f1:
 i=-1
 for line in f1:#遍历每一行
     wordlist=line.split()#将每一行的数字分开放在列表中
     for a in wordlist:#遍历每一行的数字
         number=int(a)
         if number==0:
             i=i+1
             print(i,file=f)
         else:
             print(i,file=f)
f.close()
f1.close()

'''
对边数据进行分类整理
'''

f2 = open('scrap/edges1.txt','w')
f3 = open('scrap/edges2.txt','w')
with open("scrap/edges.txt", "r") as f4:  # 打开文件
    data = f4.read()  # 读取文件
'''re1 = r'tensor[(](.*?), tensor'
reResult = re.findall(re1, data)
print(reResult, file=f1)
with open("names/data/1000/edges1_1000.txt", "r") as f:  # 打开文件
    data1 = f.read()  # 读取文件


'''

def fun1(S):

        pattern = re.compile('[(]tensor[(]\[(.*?)\][)], tensor', re.S)  # 表达式为: (.*?)
        list = pattern.findall(S)
        # 找到后返回的列表，转化为以“+”相连的字符串即可
        list1 = '+ '.join(list)
        f2.write(list1)

fun1(data)


def fun2(S):
    pattern = re.compile(', tensor[(]\[(.*?)\]', re.S)  # 表达式为: (.*?)
    list = pattern.findall(S)
    # 找到后返回的列表，转化为以“+”相连的字符串即可
    list1 = '+ '.join(list)
    f3.write(list1)

fun2(data)
f4.close()
'''
生成节点和文件，n*1维
'''
f5 = open("scrap/num_sum_nodes1.txt", "w")
sum=0
with open("scrap/num_nodes.txt","r") as f6:
 for line in f6:
     wordlist=line.split()
     for a in wordlist:
         number=int(a)
         sum=sum+number
         print(sum,file=f5)
f5.close()
f6.close()
updateFile1(r"scrap/num_sum_nodes1.txt","\n", ",")
updateFile1(r"scrap/num_sum_nodes1.txt",",", "\n")
#! /usr/bin/python

fp = open('scrap/num_sum_nodes1.txt','r')
fp1 = open('scrap/num_sum_nodes2.txt','w')
#指定文件
s = fp.read()                   #将指定文件读入内存
fp.close()                      #关闭该文件
a = s.split('\n')
a.insert(0, '0')    #在第 LINE+1 行插入
s = '\n'.join(a)                #用'\n'连接各个元素
fp1.write(s)
fp.close()
fp1.close()

# 按行读入，删除最后一行
file_old = open('scrap/num_sum_nodes2.txt', 'r')
lines = [i for i in file_old]
del lines[-1]
file_old.close()
# 再覆盖写入
file_new = open('scrap/num_sum_nodes3.txt', 'w')
file_new .write(''.join(lines))
file_new .close()



###处理边1，n*1维
updateFile(r"scrap/edges1.txt","scrap/edges0.1.txt","+", "\n")
updateFile1(r"scrap/edges0.1.txt",",\n", ", ")
updateFile1(r"scrap/edges0.1.txt",",", "")
###处理边2，n*1维
updateFile(r"scrap/edges2.txt","scrap/edges0.2.txt","+", "\n")
updateFile1(r"scrap/edges0.2.txt",",\n", ", ")
updateFile1(r"scrap/edges0.2.txt",",", "")