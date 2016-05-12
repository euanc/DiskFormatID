# DiskFormatID

This program is intended to help to identify floppy disk formats. 

To use:
Run the program as root with:

"sudo python diskIDMain.py"

(If you properly install DTC according to the instructions in the Kryoflux documentation then you may not need to run it as root).

Click "choose formats" to select disk image formats to be created
Select input and output folders and specify the directory containing the Kryoflux DTC application. These settings (including selected formats) will be saved in "settings.json" 

NB: the program license must already have been agreed to by navigating to the dtc directory in the terminal and running the GUI with:

java -jar kryoflux-ui.jar

Click "create images" to use a local copy of the Kryoflux DTC program to create the image files from a folder containing folders of raw Kryoflux stream files.

Click a button to mount the disk image files and get feedback on which files could be mounted. Check "delete unmountable" to delete the image files that couldn't be mounted. 

Click either of the "save results" buttons to save the results from the corresponding window to a file (extension will be added automatically). 

  



# DiskFormatID
