# 开发时间：2022/8/24 20:00
import numpy as np
import scipy.sparse as sp
from sklearn.model_selection import train_test_split

class compound_nr_all(object):
    def __init__(self, data_root="data", train_size=0.6, valid_size=0.1, test_size=0.3):
        self.data_root = data_root
        sparse_adjacency, node_features, graph_indicator, graph_labels = self.read_data()                          
        # 把coo格式转换为csr 进行稀疏矩阵运算
        self.sparse_adjacency = sparse_adjacency.tocsr()
        self.node_features = node_features
        self.graph_indicator = graph_indicator
        self.graph_labels = graph_labels

        self.train_index,self.valid_index, self.test_index = self.split_data(train_size,valid_size, test_size)
        self.train_label = graph_labels[self.train_index]  # 得到训练集中所有图对应的类别标签
        self.valid_label = graph_labels[self.valid_index]  # 得到验证集中所有图对应的类别标签
        self.test_label = graph_labels[self.test_index]  # 得到测试集中所有图对应的类别标签

    def split_data(self, train_size,valid_size, test_size):
        unique_indicator = np.asarray(list(set(self.graph_indicator)))                      ###zsy###  将节点图指示向量随机划分  （节点图指示向量的每一个值是该节点对应图的索引）
        # 随机划分训练集和测试集 得到各自对应的图索引   （一个图代表一条数据）
        train_index, test_index = train_test_split(unique_indicator, train_size=1 - test_size, random_state=12345)
        train_index, valid_index = train_test_split(np.asarray(train_index), train_size=train_size / (1 - test_size),random_state=12345)
        return train_index, valid_index, test_index
    def __getitem__(self, index):

        mask = self.graph_indicator == index
        # 得到图索引为index的图对应的所有节点(索引)
        graph_indicator = self.graph_indicator[mask]
        # 每个节点对应的特征标签
        node_features = self.node_features[mask]
        # 该图对应的类别标签
        graph_labels = self.graph_labels[index]
        # 该图对应的邻接矩阵
        adjacency = self.sparse_adjacency[mask, :][:, mask]
        return adjacency, node_features, graph_indicator, graph_labels
    def __len__(self):
        return len(self.graph_labels)

    def read_data(self):
        # 解压后的路径
        print("Loading compound_A.txt")
        # 从txt文件中读取邻接表(每一行可以看作一个坐标，即邻接矩阵中非0值的位置)  包含所有图的节点
        adjacency_list = np.genfromtxt('data/compound_nr_all/compound_A.txt',
                                       dtype=np.int64, delimiter=',')
        print("Loading compound_node_labels.txt")
        # 读取节点的特征标签
        node_labels = np.genfromtxt('data/compound_nr_all/compound_node_labels.txt',
                                    dtype=np.float32)

        print("Loading compound_graph_indicator.txt")
        # 每个节点属于哪个图
        graph_indicator = np.genfromtxt(
            'data/compound_nr_all/compound_graph_indicator.txt',
            dtype=np.int64)
        print("Loading compound_graph_labels.txt")
        # 每个图的标签  回归预测  标签为毒性指标 数值类型为浮点型float
        graph_labels = np.genfromtxt('data/compound_nr_all/compound_graph_labels_all.txt',
                                     dtype=np.float32)
        num_nodes = len(node_labels)  # 节点数 （包含所有图的节点）
        # 通过邻接表生成邻接矩阵  （包含所有的图）稀疏存储节省内存（coo格式 只存储非0值的行索引、列索引和非0值）
        # coo格式无法进行稀疏矩阵运算
        sparse_adjacency = sp.coo_matrix((np.ones(len(adjacency_list)),
                                          (adjacency_list[:, 0], adjacency_list[:, 1])),
                                         shape=(num_nodes, num_nodes), dtype=np.float32)
        print("Number of nodes: ", num_nodes)
        return sparse_adjacency, node_labels, graph_indicator, graph_labels
