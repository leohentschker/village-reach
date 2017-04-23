# import pyudev
import os
import sys
import time
import shutil
import hashlib


class FileTransfer():

    def __init__(self, sourcedir, targetdir=None):
        if targetdir is None:
            self.target_directory = os.path.expanduser("~")
        else:
            self.target_directory = targetdir
        self.dirname = sourcedir

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

    def copy_files(self, path):
        if os.path.isdir(path):
            shutil.copytree(path, os.path.join(self.target_directory, self.dirname))

    def main(self):
        self.file_dictionary = {}
        self.source_directory = "./test"
        self.target_directory = "./target"
        self.hasher = hashlib.md5()
        context = pyudev.Context()
        monitor = pyudev.Monitor.from_netlink(context)
        monitor.filter_by('block')
        for device in iter(monitor.poll, None):
            if 'ID_FS_TYPE' in device and device.action == 'add':
                print('{0} partition {1}'.format(device.action,device.get('ID_FS_LABEL')))
                time.sleep(5)
                for l in file('/proc/mounts'):
                    if device.device_node in l:
                        print l
                        x = l.split(' ')[1].replace('\\040',' ')
                        if self.dirname in os.listdir(x):
                            self.copy_files(x+"/"+self.dirname)
        self.create_dictionary()
        self.copy_files()
                

if __name__ == '__main__':
    if len(sys.argv) == 3:
        ft = FileTransfer(sys.argv[1], sys.argv[2])
        ft.main()
    elif len(sys.argv) == 2:
        ft = FileTransfer(sys.argv[1])
        ft.main()
    else:
        print("Usage: \"file_transfer.py <source>\": Transfer source directory on usb to local storage")
        print("Usage: \"file_transfer.py <source> <target>\": Transfer source directory on usb to full path target directory on local storage")
        sys.exit(2)
