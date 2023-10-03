import os
import shutil
import hashlib
import argparse
import time
from datetime import datetime

def log(message, log_file=None):
  """Logs a message to the console and to the log file"""
  print(f"{datetime.now()}: {message}")
  if log_file is not None:
    with open(log_file, "a") as log_f:
      log_f.write(f"{datetime.now()}: {message}\n")


def sync_folders(source_folder, replica_folder, log_file):
  """Synchronizes two folders, one way, with logging"""
  #Get the list of all files and directories in the source folder
  source_files = os.listdir(source_folder)

  #Iterate over all files in the source folder
  for file in source_files:
    source_file_path = os.path.join(source_folder, file)
    replica_file_path = os.path.join(replica_folder, file)

    #If the file isn't present in the replica folder, copy it from the source folder
    if not os.path.exists(replica_file_path):
      log(f"Copying file {file} from source folder to replica folder", log_file)
      shutil.copy2(source_file_path, replica_file_path)

    elif os.path.getmtime(source_file_path) > os.path.getmtime(replica_file_path):
    #Calculate the MD5 checksum for the source file
      with open(source_file_path, "rb") as f:
        source_checksum = hashlib.md5(f.read()).hexdigest()

    #Calculate the MD5 checksum for the replica file
      with open(replica_file_path, "rb") as f:
        replica_checksum = hashlib.md5(f.read()).hexdigest()

    #Compare the checksums to determine if the file is up to date
      if source_checksum != replica_checksum:
        log(f"Updating file {file} in replica folder", log_file)
        shutil.copy2(source_file_path, replica_file_path)
    else:
      log(f"File {file} in replica folder is up to date", log_file)
      
  #Iterate over all files in the replica folder that are not in the source folder
  for file in os.listdir(replica_folder):
    if file not in source_files:
      #If the file is not in the source folder, remove it from the replica folder
      log(f"Removing file {file} from replica folder", log_file)
      os.remove(os.path.join(replica_folder, file))

def main(source_folder, replica_folder, sync_interval, log_file):
  """Synchronizes periodically two folders, one way, with logging"""
  while True:
    sync_folders(source_folder, replica_folder, log_file)
    time.sleep(sync_interval)

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description="Periodic one-way synchronization of two folders, with log file")
  parser.add_argument("source_folder", help="The path to the source folder")
  parser.add_argument("replica_folder", help="The path to the replica folder")
  parser.add_argument("sync_interval", type=int, help="The synchronization interval in seconds")
  parser.add_argument("log_file", help="The path to the log file")

  args = parser.parse_args()

  print("Periodic one-way synchronization of two folders")
  main(args.source_folder, args.replica_folder, args.sync_interval, args.log_file)
