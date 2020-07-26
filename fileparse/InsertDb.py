#将歌曲信息插入数据库
#  format： playListId  songId  songName  singer
import json

import mysql.connector
def parseList(cnn,infile):
    for line in open (infile,'r', encoding='UTF-8'):
        res=parseLine(line)
        playListId=res[0]
        songId=res[1]
        songName=res[2]
        singer=res[3]
        insert(cnn,playListId,songId,songName,singer)
def parseLine(line):
    print(str(line))
    # data = json.loads(line);
    # print(data)
    print(str(line).split(','))
    return  str(line).split(',')
def insert(cnn,playListId,songId,songName,singer):

    cour = cnn.cursor()
    value = (playListId,songId,songName,singer)
    sql = """insert into b_hot_song (play_list_id,song_id,song_name,songer) values (%s,%s,%s,%s)"""
    cour.execute(sql, value)
    # 以下这一句很关键我少了这一句导致不报错，也插不进去数据，崩溃呀~~~
    cnn.commit()
def main():
    config = {'host': '127.0.0.1',  # 默认127.0.0.1
              'user': 'root',
              'password': 'root123',
              'port': 3306,  # 默认即为3306
              'database': 'bachelor_degree_design',
              'charset': 'utf8'  # 默认即为utf8
              }
    cnn = mysql.connector.connect(**config)
    print("连接成功")
    parseList(cnn,"G:\degreeDisign\\fileparse\\163_music_popularList_format.txt")

if __name__ == '__main__':
    main()