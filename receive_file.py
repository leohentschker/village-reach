import os
import pickle

class ReceiveFile(object):

	def main(self):
		self.receive_directory_contents()

    
	def receive_directory_contents(self):
		with open('directory_contents.txt', 'rb') as fp:
			self.itemlist = pickle.load(fp)
			print "RECEIVED"
			print self.itemlist

if __name__ == '__main__':
    r = ReceiveFile()
    r.main()