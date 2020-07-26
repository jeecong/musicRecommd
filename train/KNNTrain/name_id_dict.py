import pickle as pickle
# 首先蒋保存歌单name 歌曲name 对Id的映射
# 重建歌单id到歌单名的映射字典
import sys
def parse_playlist_get_info(in_line, playlist_dic, song_dic,playlist_song):
    songs=[]
    contents = str(in_line,'utf-8').strip().split("\t")
    name, tags, playlist_id, subscribed_count = contents[0].split("##")
    playlist_dic[playlist_id] = name
    for song in contents[1:]:
        try:
            song_id, song_name, artist, popularity = song.split(":::")
            song_dic[song_id] = song_name + "\t" + artist
            songs.append(song_id)
        except:
            print("song format error")
            print(song + "\n")
    playlist_song[playlist_id]=songs
def getplaylist_song():
    playlist_song = dict()
    for in_line in open("G:\degreeDisign\\fileparse\\163_music_playlist.txt", "rb"):
        songs = []
        contents = str(in_line, 'utf-8').strip().split("\t")
        name, tags, playlist_id, subscribed_count = contents[0].split("##")
        for song in contents[1:]:
            try:
                song_id, song_name, artist, popularity = song.split(":::")
                songs.append(song_id)
            except:
                print("song format error")
                print(song + "\n")
        playlist_song[playlist_id] = songs
    return playlist_song

def parse_file(in_file, out_playlist, out_song):
    # 从歌单id到歌单名称的映射字典
    playlist_dic = {}
    # 从歌曲id到歌曲名称的映射字典
    song_dic = {}
    playlist_song=dict()
    for line in open(in_file,"rb"):
        parse_playlist_get_info(line, playlist_dic, song_dic,playlist_song)
    # 把映射字典保存在二进制文件中
    pickle.dump(playlist_dic, open(out_playlist, "wb"))
    # 可以通过 playlist_dic = pickle.load(open("playlist.pkl","rb"))重新载入
    pickle.dump(song_dic, open(out_song, "wb"))
    return playlist_song

def getpickle():
    # parse_file("G:\degreeDisign\\fileparse\\163_music_playlist.txt", "playlist.pkl", "song.pkl")
    playlist_id_name_dic = pickle.load(open("G:\degreeDisign\\train\KNNTrain\playlist.pkl","rb"))
    print("加载歌单id到歌单名的映射字典完成...")
    song_id_name_dic=pickle.load(open("G:\degreeDisign\\train\KNNTrain\song.pkl","rb"))
    print("加载歌曲id到歌曲名的映射字典完成...")
    # 重建歌单名到歌单id的映射字典
    playlist_name_id_dic = {}
    song_name_id_dic={}
    for playlist_id in playlist_id_name_dic:
        playlist_name_id_dic[playlist_id_name_dic[playlist_id]] = playlist_id
    print("加载歌单名到歌单id的映射字典完成...")
    for song_di in song_id_name_dic:
        song_name_id_dic[song_id_name_dic[song_di]] = song_di
    print("加载歌曲名到歌曲id的映射字典完成...")
    return playlist_id_name_dic,song_id_name_dic, playlist_name_id_dic,song_name_id_dic

