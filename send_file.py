import os
import pickle

class SendFile(object):

	def main(self):
		self.source = "./test"
		self.send_directory_contents()

    
	def send_directory_contents(self):
		with open('directory_contents.txt', 'wb') as fp:
			self.itemlist = list(os.walk(self.source))
			print "SENDING"
			print self.itemlist
			pickle.dump(self.itemlist, fp)

if __name__ == '__main__':
    s = SendFile()
    s.main()