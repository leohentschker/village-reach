import os
import pickle
from lightblue import *
 

class Receive(object):

	def main(self):
		s = socket()
 		s.bind(("", 0))
 		advertise("My OBEX Service", s, OBEX)
		obex.recvfile(s, "directory_contents.txt")
		self.receive_directory_contents()
		os.makedirs("test")
		for dirName, subdirList, fileList in self.itemlist:
			for subdir in subdirList:
				os.makedirs(os.path.join(dirName, subdir))
			for file in fileList:
				obex.recvfile(s, os.path.join(dirName, file))

    
	def receive_directory_contents(self):
		with open('directory_contents.txt', 'rb') as fp:
			self.itemlist = pickle.load(fp)
			print "RECEIVED"
			print self.itemlist

if __name__ == '__main__':
    r = Receive()
    r.main()