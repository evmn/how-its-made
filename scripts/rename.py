#!/usr/bin/python3
import csv
import os


def rename_file(keyword, title):
	all_files = os.listdir('.')
	file_list = [f for f in all_files if f[:6] == keyword]
	for old in file_list:
		ext = old[-4:]
		if ext == '.mp4':
			new = title + ext
			print("{}  ---> {}".format(old,new))
		elif ext == '.srt':
			new = title + ".en" + ext
			print("{}  ---> {}".format(old,new))
		elif ext == '.jpg':
			new = title + "-thumb" + ext
			print("{}  ---> {}".format(old,new))
#		os.rename(old, new)

def main():
	with open("lists", 'r') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter='|')
		for row in csv_reader:
			keyword=row[0]
			seg1=row[1]
			seg2=row[2]
			seg3=row[3]
			try:
				seg4=row[4]
			except:
				seg4=""
			if seg4 =="":
				title = "{} - {}, {}, {}".format(keyword, seg1, seg2, seg3)
			else:
				title = "{} - {}, {}, {}, {}".format(keyword, seg1, seg2, seg3, seg4)
			if keyword[4:6] == "01":
				newdir =  "../Season " + keyword[1:3]
				print(newdir)
				os.chdir(newdir)
			rename_file(keyword, title)


if __name__ == "__main__":
	main()
