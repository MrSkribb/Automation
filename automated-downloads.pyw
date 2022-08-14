import os
import shutil
import time
import keyboard

source = "C:\\path\\to\\source\\" # Directory that is scanned
destination1 = "C:\\path\\to\\destination1\\"
destination2 = "C:\\path\\to\\destination2\\"
destination3 = "C:\\path\\to\\destination3\\"
destination4 = "C:\\path\\to\\destination4\\"
sub1 = 'CC' # 2 letter key used to manually rename files
sub2 = 'CI'
sub3 = 'IS'
sub4 = 'SD'

def main():
    time.sleep(2)
    fileNames = os.listdir(source) # Lists all files in source directory
    global fileName
    for fileName in fileNames:
        if fileName.endswith(('.crdownload', '.download', '.temp')): # Doesn't touch downloading files
            print("File(s) downloading...")
            time.sleep(1)
        else:
            if sub1 in fileName:
                fileHandler(destination1)

            elif sub2 in fileName:
                fileHandler(destination2)
                
            elif sub3 in fileName:
                fileHandler(destination3)

            elif sub4 in fileName :
                fileHandler(destination4)

# File handler 
def fileHandler(destination):
    print('File Name: ' + fileName)
    time.sleep(1) # Removes rename errors
    shutil.move(source + fileName, destination) # Moves file from source directory to destination directory
    print(fileName+" was moved")
    new = (fileName[2:])
    os.rename(destination+fileName, destination+new) # Removes 2 letter code from name in new directory
    print('File has been renamed.')


# This code was added due to instablity and high CPU usage, script sits idle until 'home' key is pressed, then scans source directory constantly until '-' key is pressed. 
run = 0
if keyboard.read_key() == 'home': # home key starts the main() function in a loop
    print("Run script")
    while run == 0:
        main()   
        if keyboard.read_key() == '-': # - key stops the loop
            break
           
else:
    keyboard.wait()
    print("Script waiting")

    



