# Automated-File-Sorter

A python script that automates the moving of files in a source directory, the script will move files accordingly if they have a 2 letter key that corresponds to a destination directory.
A use case for this can be automating the Downloads folder to move School, Work or University documents into their corresponding folders. Once the file is downloaded, manually add your desired 2 letter key at the start of the file name and the script will move the file to the desired destination and remove the key from the file name.
**The file is best used when it starts on system startup**
automated-downloads-noLoop.pyw - The base script, main() function will run constantly in the background until the program is killed 
automated-downloads.pyw - An altered script that adds extra functionality to conserve resources, the script will sit idle in the background until a certain key is pressed, then the source directory will be scanned, the script stops when a certain key is pressed.
