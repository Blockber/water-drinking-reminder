# water-drinking-reminder
Reminds you to drink water every hour

#installation
Method 1:
1. Download install.exe
2. Run exe file

Method 2 (in case download of exe file is blocked):
1. Download the "files" directory
2. Download pyinstaller 
3. Open the command line and navigate to the downloaded directory
4. Enter "pyinstaller --onefile --windowed --add-data "icon.ico;." drink.py"
5. Extract the "drink.exe" file from the "dist" directory and put it in the same directory as install.py
6. Enter "pyinstaller --onefile --windowed --add-data "drink.exe;." install.py"
7. Extract the "install.exe" file from the "dist" directory then run it

#uninstallation
1. Run command prompt
2. Enter "tasklist" then find the PID of "drink.exe" (e.g. 1928)
3. Enter "taskkill /pid 1928 /f"
4. Open Run
5. Enter "shell:startup" 
6. Delete "drink.exe" file
