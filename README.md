# Folders-synchronization

The program folders_synchronization.py is written in Python and synchronizes two folders, the source and the replica. The synchronization is one-way, meaning that the replica folder is updated to match the source folder, but not vice versa. The synchronization is performed periodically and the file operations are logged to a file and to the console. 

- Folder Synchronization: Compares files in the source and replica folders, copying new or modified files from the source to the replica folder.

- Logging: Logs synchronization activities to a specified log file, including file updates, copies, and removals.

- Checksum-based Comparison: Utilizes MD5 checksums to efficiently determine if a file needs to be updated in the replica folder.

- Periodic Synchronization: Synchronizes the folders at regular intervals, specified by the user.

# Code structure 

The script is organized as follows:

* log(message, log_file): Function to log messages to the console and a log file.

* sync_folders(source_folder, replica_folder, log_file): Function to synchronize the folders and log activities.

* main(source_folder, replica_folder, sync_interval, log_file): Function to start periodic synchronization.

* The main block of code initiates the script, parses command-line arguments, and calls the main function to start synchronization.

# Usage:

python folders_synchronization.py <source_folder> <replica_folder> <sync_interval> <log_file>

Command-line Arguments:

    source_folder: The path to the source folder.
    replica_folder: The path to the replica folder.
    sync_interval: The synchronization interval in seconds.
    log_file: The path to the log file.

Example:

python folders_synchronization.py /path/source /path/replica 120 /path/log
