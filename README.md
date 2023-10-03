# Folders-synchronization

The program folders_synchronization.py is written in Python and synchronizes two folders, the source and the replica. The synchronization is one-way, meaning that the replica folder is updated to match the source folder, but not vice versa. The synchronization is performed periodically and the file operations are logged to a file and to the console.

The program works by first getting a list of all files and directories in the source folder. It then creates a dictionary to store the MD5 checksums of all files in the source folder.


# Usage:

python folders_synchronization.py <source_folder> <replica_folder> <sync_interval> <log_file>

Arguments:

    source_folder: The path to the source folder.
    replica_folder: The path to the replica folder.
    sync_interval: The synchronization interval in seconds.
    log_file: The path to the log file.

Example:

python sync_folders.py /path/to/source/folder /path/to/replica/folder 60 /path/to/log/file
