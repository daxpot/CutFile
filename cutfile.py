#coding=utf-8

import re
import os

class CutFile(object):

	"""分割文件"""
	def __init__(self, src, dist, preg):
		if os.path.isfile(src) == False:
			raise Exception("src 必须为一个文件")

		dist = dist.rstrip("/") + "/";
		if os.path.exists(dist) == False:
			os.mkdir(dist)

		if os.path.isdir(dist) == False:
			raise Exception("dist 必须为一个目录，分割出来的文件存放于该目录")

		self.src = src
		self.dist = dist
		self.pattern = re.compile(preg)


	def cut(self):
		first = ""
		current = False

		with open(self.src) as f:
			for line in f:
				r = self.pattern.findall(line)
				if r:
					filename = self.dist + r[0] + ".txt"
					print filename
					current = open(filename, "w")

				if current:
					if first:
						current.write(first)
						first = ""
					current.write(line)
				else:
					first += line + "\n"


if __name__ == '__main__':
	cf = CutFile("hunqiburumen.txt", "result", "第.*章")
	cf.cut();