import sys
import time
# 推荐每日歌曲
import redis as redis
from surprise import KNNBaseline

from train.KNNTrain import getDataset, name_id_dict


def train():
    data_set=getDataset.get_dataset("G:\degreeDisign\\fileparse\\163_music_suprise_format.txt")
    algo = KNNBaseline()
    algo.train(data_set)
    return  algo,data_set

def predict_user(user_id,algo):
    playlist_id_name_dic,song_id_name_dic, playlist_name_id_dic,song_name_id_dic=name_id_dict.getpickle()
    print("歌单id", user_id)
    print("歌单名字",playlist_id_name_dic[user_id])
    # 取出来对应的内部user id => to_inner_uid
    playlist_inner_id = algo.trainset.to_inner_uid(user_id)
    print("内部id", playlist_inner_id)
    playlist_neighbors = algo.get_neighbors(playlist_inner_id, k=10)
    print("和歌单（用户）"+playlist_id_name_dic[user_id]+"最相似的歌单（用户）：")
    res=[]
    for inner_id in playlist_neighbors:
        predict_id=algo.trainset.to_raw_uid(inner_id)
        print("/t 歌单Id："+predict_id)
        res.append(predict_id)
        print("/t歌单名字："+playlist_id_name_dic[predict_id])
    return res

def predict_user_song(user_id,dataset,algo):
    # 预测打分
    print("dddddddd"+algo.trainset.to_raw_uid(4))
    playlist_id_name_dic, song_id_name_dic, playlist_name_id_dic, song_name_id_dic = name_id_dict.getpickle()
    user_inner_id = 4
    user_rating = dataset.ur[user_inner_id]
    print(user_rating)
    items = map(lambda x: x[0], user_rating)
    items_test=range(1,2000)
    for song in items_test:
        print(algo.predict(user_inner_id, song, r_ui=1), song_id_name_dic[algo.trainset.to_raw_iid(song)])
def main():
    playlist_songs=name_id_dict.getplaylist_song()
    algo, data_set=train()
    for i in playlist_songs:
        res=predict_user(i,algo)
        save_redis(i,res,playlist_songs)
    # predict_user_song(4,data_set,algo)
    # predict_user("306948578",algo)

def save_redis(id,res,playlist_songs):
    pool = redis.ConnectionPool(host='127.0.0.1', password='foobared')  # 实现一个连接池
    r = redis.Redis(connection_pool=pool)
    value =[]
    key="USER::"+id
    for item in res:
        for i in playlist_songs[item]:
            value.append(int(i))
    day=time.strftime('%Y.%m.%d',time.localtime(time.time()))
    print(key,day,str(value).strip("'"))
    r.hset(key,day,str(value).strip("'"))
    pass
if __name__ == '__main__':
    main()




