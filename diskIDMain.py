#!/usr/bin/env python2
from PyQt4 import QtGui, QtCore

import sys
import os
import diskIDMainGUI
import chooseFormats 
import subprocess
import json
import sys
from subprocess import Popen
from subprocess import check_output
from itertools import islice


global inpDirLoc
global outDirLoc
global dtcDirloc


impDirLoc = ""
outDirLoc = ""
dtcDirLoc = ""


class kryoMain(QtGui.QMainWindow, diskIDMainGUI.Ui_kryoMain):
  def __init__(self, parent=None):
    #don't really understand global variables well enough, but I think I need to ptu these here
    global inpDirLoc
    
    global outDirLoc
    
    global dtcDirLoc
    # start the whole gui thing
    super(kryoMain, self).__init__(parent)
    self.setupUi(self)
    
    # set the dtc max concurrent isntances box to default to 1
    self.DTCInstances.setText("1")

    #open the settings.json file for reading
    if os.stat('settings.json').st_size != 0:
      with open('settings.json') as settings_file:    
      
    #set main settings to values from settings json file
        settings = json.load(settings_file)
        if "mainSettings" in settings:
          for setting in settings["mainSettings"]:
            self.inputDir.setText(setting["Input directory"])
            dtcDirLoc = str(setting["DTC directory"])
            self.DTCDir.setText(setting["DTC directory"])
            inpDirLoc = str(setting["Input directory"])
            self.outputDir.setText(setting["Output directory"])
            outDirLoc = str(setting["Output directory"])
            if setting == "Delete unmountable":
              if setting["Delete unmountable"] == "TRUE":
                self.deleteUnmountable.setChecked(true)
              else:
                  self.deleteUnmountable.setChecked(true)
                 


# initiate sub program to choose formats when button is clicked      
       
  def choose_formats(self):
    
    self.addTypes = chooseFormats.addTypes()
    self.addTypes.show()
    
# function below takes input from create images button and creates the images

  
  def create_images(self):
    global inpDirLoc
    
    global outDirLoc
    
    global dtcDirLoc
    
    with open('settings.json') as data_file:    
      data = json.load(data_file)
       
    # set input variables for the source and destination file directories and dtc directory
    
    source_dirname= inpDirLoc
    dest_dir = outDirLoc
    dtc_dir = dtcDirLoc
    commands = []
    
    outdir = ()
    
    # check the input folder and find all sub directories
    for dirname, dirnames, filenames in os.walk(source_dirname):
    
    # get the folder names for each sub directory
      for subdirname in dirnames:
    
    # create a variable to use for the sub directory paths
        indirname = os.path.join(dirname, subdirname)
      
    
    # check each sub directory to see if it has a stream file in it
        if os.path.isfile(os.path.join(indirname, "track00.0.raw")) == True:
    
    # define a variable equal to the path for the folder to put the images in. The path will be named with the stream file name
          outdir = os.path.join(dest_dir, subdirname)
    
    # if the directory to put the files in doesn't exist then create it
          if os.path.exists(outdir) == False:
            os.makedirs(outdir)
    
    # and make the directory readable and writeable by all
            os.chmod(outdir, 0o666)
    
    
          
  #setup a variable to form each command into    
          for format in data["outputFormats"]:
            command = set()
            filepath =  outdir + "/" + subdirname
      
            for param in format:
              if command != "":        
                command.add(format[param])
                filepath = filepath + format[param]
                                    
              else:
                command = format[param]   
                filepath = filepath + format[param]            
        
            commands.append((dtc_dir + "./dtc", "-f" + str(filepath) + ".img", "-m1", ", ".join([str(x) for x in command]), "-f" + indirname + "/track","-i0"))
   

    			
    # Now run the commands in paralell
    # set max concurrent instances from feild in gui
    max_workers = int(self.DTCInstances.text())  
    processes = (Popen(cmd, cwd=dtc_dir,stdout=subprocess.PIPE,stderr=subprocess.PIPE) for cmd in commands)

    running_processes = list(islice(processes, max_workers))  
    while running_processes:
      results = []
      for i, process in enumerate(running_processes):
        out, err = process.communicate()
        
#update the text browser with the status
        
        
        results.append(str(out) + str(err))
# process the update to the gui
        QtGui.QApplication.processEvents()
        if process.poll() is not None:  # the process has finished
          running_processes[i] = next(processes, None)  # start new process
          if running_processes[i] is None: # no new processes
            del running_processes[i]
            break
      for result in results:
        self.imageCreationResults.append(result)
    self.imageCreationResults.append(" ")
    self.imageCreationResults.append("------------------------------------------------")
    self.imageCreationResults.append("Creation of images complete")
    self.imageCreationResults.append("------------------------------------------------")
    

  def try_mounting(self):
    global outDirLoc
    dest_dir = outDirLoc
   
        # now try mounting the files you created and delete the ones that don't mount
    
    #select all directories in the destination directory
    for dirname, dirnames, filenames in os.walk(dest_dir):
    
    # for each of those find the files in them
      for subdirname in dirnames:
        indirname = os.path.join(dirname,subdirname)
    
    #for each disk image file in that directory
        for dirname2, dirnames2, filenames2 in os.walk(indirname):
          for filenm in filenames2:
    
    # for each file, mount it and put the resulting errors into a variable p.stderr
     #update the text browser with the status
            self.MountingResults.append("Trying to mount " + str(filenm))
# process the update to the gui
            QtGui.QApplication.processEvents()
            p = subprocess.Popen(["mount", "-O loop", os.path.join(dest_dir, indirname, filenm), "/mnt"], stderr=subprocess.PIPE)
    
    # if there is no error then umount the disk image
            if p.stderr.readline() == "":
     #update the text browser with the status
              self.MountingResults.append(str(filenm) + " mounted successfully")
# process the update to the gui
              QtGui.QApplication.processEvents()
              subprocess.call(["umount", "/mnt"])
              self.MountingResults.append(" ")
              self.MountingResults.append("------------------------------------------------")
              self.MountingResults.append(" ")
  
                   
            else:
#update the text browser with the status
              self.MountingResults.append(str(filenm) + " mounting failed")

# process the update to the gui
              QtGui.QApplication.processEvents()
              if self.deleteUnmountable.isChecked():
#update the text browser with the status
                self.MountingResults.append("Deleting " + str(filenm))
                self.MountingResults.append(" ")
                self.MountingResults.append("------------------------------------------------")
                self.MountingResults.append(" ")
# process the update to the gui
                QtGui.QApplication.processEvents()
                subprocess.call(["rm", os.path.join(dest_dir, indirname, filenm)])
              else:
                
                self.MountingResults.append(" ")
                self.MountingResults.append("------------------------------------------------")
                self.MountingResults.append(" ")
    self.MountingResults.append
    self.MountingResults.append("Creation of images complete")
    self.MountingResults.append(" ")
    self.MountingResults.append("------------------------------------------------")       
  
  def delete_unmountable_change(self):
    
    if os.stat('settings.json').st_size != 0:
# if it is not empty open it for reading
      with open('settings.json','r') as settings_file: 
        settings = json.load(settings_file)
        if self.deleteUnmountable.isChecked():
          for setting in settings["mainSettings"]:
            setting["Delete unmountable"] = "TRUE"
          
        else: 
          for setting in settings["mainSettings"]:
            setting["Delete unmountable"] = "FALSE"
        jsoutput = json.dumps(settings)
        outfile = open("settings.json", 'w')
        outfile.write(jsoutput)
        outfile.close()

  def browse_dtc_dir(self):
    
    global dtcDirLoc
    dtcDirLoc = QtGui.QFileDialog.getExistingDirectory(self,
                                                           "Select a folder") + "/"
    dtcDirLoc = str(dtcDirLoc)
    self.DTCDir.setText(dtcDirLoc)
    
    if os.stat('settings.json').st_size != 0:
# if it is not empty open it for reading
      with open('settings.json','r') as settings_file: 
        settings = json.load(settings_file)
        for setting in settings["mainSettings"]:
           setting["DTC directory"] = str(dtcDirLoc)

        jsoutput = json.dumps(settings)
        outfile = open("settings.json", 'w')
        outfile.write(jsoutput)
        outfile.close()

#This function processes the browse input directory button press
  def browse_inp_dir(self):
    global inpDirLoc
    
    inpDirLoc = QtGui.QFileDialog.getExistingDirectory(self,
                                                           "Select a folder") + "/"
    inpDirLoc = str(inpDirLoc)
    self.inputDir.setText(inpDirLoc)
    
    if os.stat('settings.json').st_size != 0:
# if it is not empty open it for reading
      with open('settings.json','r') as settings_file: 
        settings = json.load(settings_file)
        for setting in settings["mainSettings"]:
           setting["Input directory"] = str(inpDirLoc)

        jsoutput = json.dumps(settings)
        outfile = open("settings.json", 'w')
        outfile.write(jsoutput)
        outfile.close()
  
  def save_mounting_results(self):
    # get file path from user input browsing
    saveFilePath = QtGui.QFileDialog.getSaveFileName(self,'Choose save file location',str(outDirLoc),selectedFilter='*.txt')
    #make file extension .txt if not already
    if str(saveFilePath)[-4:] != '.txt':
      saveFilePath = saveFilePath + ".txt"
    #assing textbrowser contents to a variable and write it to the file selected above
    mountingResultsDialog = self.MountingResults.toPlainText()
    outfile = open(saveFilePath, 'w')
    outfile.write(mountingResultsDialog)
    outfile.close()
   



  def save_dtc_results(self):
     # get file path from user input browsing
    saveDTCPath = QtGui.QFileDialog.getSaveFileName(self,'Choose save file location',str(outDirLoc),selectedFilter='*.txt')
    #make file extension .txt if not already
    if str(saveDTCPath)[-4:] != '.txt':
      saveDTCPath = saveDTCPath + ".txt"
    #assing textbrowser contents to a variable and write it to the file selected above
    imageCreationResultsDialog = self.imageCreationResults.toPlainText()
    outfile = open(saveDTCPath, 'w')
    outfile.write(imageCreationResultsDialog)
    outfile.close()

  
  def browse_output_dir(self):
    global outDirLoc
    
    outDirLoc = QtGui.QFileDialog.getExistingDirectory(self,
                                                           "Select a folder") + "/"
    outDirLoc = str(outDirLoc)
    self.outputDir.setText(outDirLoc)
    
    if os.stat('settings.json').st_size != 0:
# if it is not empty open it for reading
      with open('settings.json','r') as settings_file: 
        settings = json.load(settings_file)
        for setting in settings["mainSettings"]:
           setting["Output directory"] = str(outDirLoc)
         
        jsoutput = json.dumps(settings)
        outfile = open("settings.json", 'w')
        outfile.write(jsoutput)
        outfile.close()

def main():
    app = QtGui.QApplication(sys.argv)
    form = kryoMain()
    form.show()
    app.exec_()
  

	

if __name__ == '__main__':
    main()
