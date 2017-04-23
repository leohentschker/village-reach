# import pyudev
import os
import time
import shutil
import hashlib


class FileTransfer(object):

    # dirname = "test"
    # # target_directory = os.path.expanduser("~")+"/"+"Documents"
    # target_directory = "target"
    # hasher = hashlib.md5()

    def hash_text(self, text):
        self.hasher.update(text)
        return self.hasher.hexdigest()

    def print_dictionary(self):
        for key, value in self.file_dictionary.items():
            print "Hash Name: " + key + " File Name: " + value


    def create_dictionary(self):
        for dirName, subdirList, fileList in os.walk(self.target_directory):
            print dirName
            print fileList
            for fname in fileList:
                with open(dirName + "/" + fname, 'r') as myfile:
                    hash_name = self.hash_text(myfile.read())
                    self.file_dictionary[os.path.join(dirName, fname) + hash_name] = fname

        self.print_dictionary()


    def copy_files(self):
        if os.path.isdir(self.source_directory):
            shutil.copytree(self.source_directory, self.target_directory)

    def main(self):
        self.file_dictionary = {}
        self.source_directory = "./test"
        self.target_directory = "./target"
        self.hasher = hashlib.md5()
        # context = pyudev.Context()
        # monitor = pyudev.Monitor.from_netlink(context)
        # monitor.filter_by('block')
        # for device in iter(monitor.poll, None):
        #     if 'ID_FS_TYPE' in device and device.action == 'add':
        #         print('{0} partition {1}'.format(device.action,device.get('ID_FS_LABEL')))
        #         time.sleep(5)
        #         for l in file('/proc/mounts'):
        #             if device.device_node in l:
        #                 print l
        #                 x = l.split(' ')[1].replace('\\040',' ')
        #                 if dirname in os.listdir(x):
        #                     copy_files(x+"/"+dirname)
        # target_directory = os.path.expanduser("~")+"/"+"Documents"
        self.create_dictionary()
        self.copy_files()
                

if __name__ == '__main__':
    FileTransfer().main()
