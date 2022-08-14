import os
import shutil
import time


source = "C:\\Users\\CSGO\\Downloads\\" # Directory that is scanned
destination1 = "C:\\Users\\CSGO\\Desktop\\Griffith\\CCoding\\"
destination2 = "C:\\Users\\CSGO\\Desktop\\Griffith\\Comp Interaction\\"
destination3 = "C:\\Users\\CSGO\\Desktop\\Griffith\\Info Sys\\"
destination4 = "C:\\Users\\CSGO\\Desktop\\Griffith\\Sys Dev\\"
sub1 = 'CC'
sub2 = 'CI'
sub3 = 'IS'
sub4 = 'SD'

def main():
    #print('main')
    time.sleep(2)
    fileNames = os.listdir(source) # Lists all files in source directory
    global fileName
    for fileName in fileNames:
        if fileName.endswith(('.crdownload', '.download')): # Doesn't touch downloading files
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


run = 0

while run == 0:
    main()   
      
        

    



