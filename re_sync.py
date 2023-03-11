import os
import argparse
import shutil
import hashlib
import logging
import schedule
import time
import sys


logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
logFormatter = logging.Formatter("%(asctime)s %(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.INFO)

fileHandler = logging.FileHandler("{0}/{1}.log".format(os.getcwd(), "modifications"))
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
  
class FileSync():

    def _recurse(self, parent_path, file_list, sync_path):

        self._deleted(file_list, sync_path)

        if len(file_list) == 0:
            return

        if not os.path.exists(sync_path):
            logging.info(f"New Folder: {sync_path}")
            os.mkdir(sync_path)

        for sub_path in file_list:
            full_path = os.path.join(parent_path, sub_path)

            if os.path.isdir(full_path):

                sync_full_path = os.path.join(sync_path, sub_path)

                if not os.path.exists(sync_full_path):
                    logging.info(f"New Folder: {sync_full_path}")
                    os.mkdir(sync_full_path)

                self._recurse(full_path, os.listdir(full_path), sync_full_path)

            elif os.path.isfile(full_path):

                filename = full_path.split(os.path.sep)
                sync_file = os.path.join(sync_path, filename[-1])

                if not (os.path.exists(sync_file)):
                    shutil.copy2(full_path, sync_path)
                    logging.info(f"New file: {sync_file}")
            

                elif not self._check_md5(full_path, sync_file):
                    shutil.copy2(full_path, sync_path)
                    logging.info(f"Updated file: {sync_file}")
                    

    def _check_md5(self, input_file, output_file):
        with open(input_file, "r", encoding="utf-8", errors="ignore") as in_file, \
                open(output_file, "r", encoding="utf-8", errors="ignore") as out_file:

            md5_input = hashlib.md5(in_file.read().encode()).hexdigest()
            md5_output = hashlib.md5(out_file.read().encode()).hexdigest()
            return md5_input == md5_output

    def _delete_recurse(self, folder, subdirs):
        if len(subdirs) == 0:
            os.rmdir(folder)
            logging.info(f"Deleted folder: {folder}")
            return

        for file in subdirs:
            full_path = os.path.join(folder, file)

            if os.path.isdir(full_path):
                self._delete_recurse(full_path, os.listdir(full_path))
                if os.path.exists(full_path):
                    os.rmdir(full_path)
                    logging.info(f"Deleted Folder: {full_path}")
                    
            else:
                os.remove(full_path)
                logging.info(f"Deleted File: {full_path}")
                

    def _deleted(self, file_list, sync_path):
        src_files = set(file_list)

        if os.path.isdir(sync_path):
            dst_files = set(os.listdir(sync_path)) 
        deleted_files = dst_files.difference(src_files)

        if len(deleted_files) > 0:
            for file in deleted_files:
                full_path = os.path.join(sync_path, file)

                if os.path.isdir(full_path):
                    self._delete_recurse(full_path, os.listdir(full_path))
                else:
                    os.remove(full_path)
                    logging.info(f"Deleted File: {full_path}")
                    

    def sync(self, args):
        self.src = args.source
        self.dst = args.destination
       
        if not os.path.isdir(self.dst):
            os.mkdir(self.dst)
        self._recurse(self.src, os.listdir(self.src), self.dst)
            


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-src", "--source",
                        help="Original folder", default=".")
    parser.add_argument("-dst", "--destination",
                        help="Destination folder", default="../folderSync")
    parser.add_argument("-sec", "--seconds",
                        help="Time in seconds to sync folders", type=int, default=0)
    parser.add_argument("-min", "--minutes",
                        help="Time in minutes to sync folders", type=int, default=0)
    parser.add_argument("-hrs", "--hours",
                        help="Time in hours to sync folders", type=int, default=0)
    

    args = parser.parse_args()
    frecuency= args.hours*3600 + args.minutes*60 + args.seconds

    schedule.every(frecuency).seconds.do(FileSync().sync, args=args)


while True:
    schedule.run_pending()
    time.sleep(1)