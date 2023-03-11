# Recursive directories sync script :

Program that synchronizes two folders: source and replica.
- One-way synchronization: after the synchronization, content of the replica folder is modified to match source´s content.
- Synchronization is performed periodically in hours, mins, or seconds as the user requires/specifies.
- File creation/copying/removal operations are logged to a file and displayed on the console output;
- Folder paths, synchronization interval and log file path must be provided using the command line arguments;

## How it works:

1. Clone repository from Github: 
$ https://github.com/DaniestBP/Sync_DirTree.git

2. Create a Virtual Enviroment to run the script: python3 -m venv .venv

3. Activate env: source .venv/bin/activate (in Linux) / source venv/Scripts/activate (in Windows)

4. Install requirements: 

$ pip3 install -r requirements.txt

5. Execute program: python3 re_sync.py -src (source file abs path) -dst (replica file abs path) -sec (in case you want set sync.up in seconds) -min (same in minutes) -hours (samething)
NOTE: Sync. may be set as a summatory of hours, minutes and seconds  -->

6. Whenever you want to stop program use: Ctrl+C

