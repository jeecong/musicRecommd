#构建KNN movielen格式数据集
import os
from surprise import  Reader
from surprise import Dataset


def get_dataset(file_path):
    # 指定文件格式
    reader = Reader(line_format='user item rating timestamp', sep=',')
    # 从文件读取数据
    music_data = Dataset.load_from_file(file_path, reader=reader)
    music_data = music_data.build_full_trainset()
    return music_data