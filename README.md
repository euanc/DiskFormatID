# DiskFormatID

This program is intended to help to identify floppy disk formats.  It takes a folder of http://www.Kryoflux.com stream files as input. It only works with linux and requires

python 2.7
pyqt4
mount

At some point I'll figure out how to package it all up, but for now you'll have to add the dependencies yourself. Should be fairly straight forward in most linux distributions, e.g. BitCurator. Almost all come with mount and python (2.x) already installed. 


Please support http://kryoflux.com/ !

To use:
Clone the repository or download all the files using the download zip button and extract them to a folder (not all are actually needed).

Run the program as root with:

"sudo python diskIDMain.py"

(If you properly install DTC according to the instructions in the Kryoflux documentation then you may not need to run it as root).

Click "choose formats" to select disk image formats to be created
Select input and output folders and specify the directory containing the Kryoflux DTC application. These settings (including selected formats) will be saved in "settings.json" 

NB: the program license must already have been agreed to by navigating to the dtc directory in a terminal winwdow and running the GUI with:

java -jar kryoflux-ui.jar

Then accpeting the prompt.

Choose how many concurrent dtc instances you want to run to create the disk images.
Click "create images" to use a local copy of the Kryoflux DTC program to create the image files from a folder containing folders of raw Kryoflux stream files. NB: the interface may lock up and not update the results for a indeterminate period of time. 

Click a button to mount the disk image files and get feedback on which files could be mounted. Check "delete unmountable" to delete the image files that couldn't be mounted. 

Click either of the "save results" buttons to save the results from the corresponding window to a file (extension will be added automatically). 

