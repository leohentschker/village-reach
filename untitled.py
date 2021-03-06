import os
import pickle
from lightblue import *
 

class ReceiveFiles(object):

	def main(self):
		self.receive_directory_contents()
		s = socket()
 		s.bind(("", 0))
 		advertise("My OBEX Service", s, OBEX)
		obex.recvfile(s, "MyFile.txt")

    
	def receive_directory_contents(self):
		with open('directory_contents.txt', 'rb') as fp:
			self.itemlist = pickle.load(fp)
			print "RECEIVED"
			print self.itemlist

if __name__ == '__main__':
    r = ReceiveFile()
    r.main()