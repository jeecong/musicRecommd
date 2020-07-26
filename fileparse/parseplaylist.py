# 清洗数据，提取有用的数据
import json
import sys

def parse_song_line(in_line):
	data = json.loads(in_line)
	name = data['result']['name']
	tags = ",".join(data['result']['tags'])
	subscribed_count = data['result']['subscribedCount']
	if(subscribed_count<100):
		return False
	playlist_id = data['result']['id']
	song_info = ''
	songs = data['result']['tracks']
	for song in songs:
		try:
			song_info += "\t"+":::".join([str(song['id']),song['name'],song['artists'][0]['name'],str(song['popularity'])])
		except Exception as e:
			#print e
			#print song
			continue
	return name+"##"+tags+"##"+str(playlist_id)+"##"+str(subscribed_count)+song_info

def parse_file(in_file, out_file):
	out = open(out_file, 'w' , encoding='UTF-8')
	for line in open(in_file ,'rb'):
		result = parse_song_line(line)
		if(result):
			out.write(result.strip()+"\n")
	out.close()

def main():
	parse_file("D:/recommention/playlist.detail.all/playlistdetail.all.json", "./163_music_playlist.txt")
if __name__ == '__main__':
	print("begin  to parse..... ")
	main()
	print(" parse end!")