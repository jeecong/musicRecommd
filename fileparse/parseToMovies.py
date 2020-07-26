# coding: utf-8
# 将清洗好的数据转化为movielength数据格式  便于构建模型
# 解析成userid itemid rating timestamp行格式
#
import json
import sys


def is_null(s):
    return len(s.split(",")) > 2


def parse_song_info(song_info):
    print(song_info)
    try:
        song_id, name, artist, popularity = song_info.split("::")
        return ",".join([song_id, name.strip(), artist, popularity])
        # song_id, name, artist, popularity = song_info.split(":::")
        # return ",".join([song_id, "1.0", '1300000'])
    except Exception as  e:
        print (e.with_traceback())
        # print song_info
        return ""


def parse_playlist_line(in_line):
    try:
        # print(in_line)
        contents = in_line.strip().split("\t")
        name, tags, playlist_id, subscribed_count = contents[0].split("##")
        songs_info = map(lambda x: playlist_id + "," + parse_song_info(x), contents[1:])
        songs_info = filter(is_null, songs_info)
        return "\n".join(songs_info)
    except Exception as e:
        print(e.with_traceback())
        return False


def parse_file(in_file, out_file):
    out = open(out_file, 'w',encoding='utf-8')
    for line in open(in_file,'r',encoding='UTF-8'):
        result = parse_playlist_line(line)
        if (result):
            out.write(result.strip() + "\n")
            #out.write(result.strip() + "\n")
    out.close()

def main():
    parse_file("./163_music_playlist.txt", "./163_music_suprise_format.txt")
def main1():
    try:
        parse_file("D:/recommention/popular.playlist", "./163_music_popularList_format.txt")
    except Exception as e:
        print(e.with_traceback())

if __name__ == '__main__':
    print("begin to parse ....")
    #main()
    main1()
    print("end ")