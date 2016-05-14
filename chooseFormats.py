from PyQt4 import QtGui
import sys
import os
import json
import chooseFormatsGUI


imageTypes = {"CT Raw":"-i2","FM Sector":"-i3","FM XFD":"-i3a","MFM":"-i4","Amiga DOS":"-i5","CBM DOS":"-i6","CBM DOS ErrMap":"-i7","Apple DOS 3.2":"-i8","Apple DOS 3.3":"-i8a","DSK":"-i9","Apple DOS 400/800K":"-i10","EMU":"-i11","EMU2":"-i12","Amiga Disk Spare":"-i13","DEC RX01":"-i14","DEC RX02":"-i15","CBM Micro Prose":"-i16","CBM RapidLok":"-i17","CBM Datasoft":"-i18","CBM Vorpal":"-i19","CBM V-MAX":"-i20","CBM Teque":"-i21","CBM TDP":"-i22","CBM GCR":"-i22a","CBM Big5":"-i23","CBM DOS":"-i24","CBM OziSoft":"-i25"}
imageFmts = {'-i3a': 'FM XFD', '-i24': 'CBM DOS', '-i25': 'CBM OziSoft', '-i20': 'CBM V-MAX', '-i21': 'CBM Teque', '-i22': 'CBM TDP', '-i23': 'CBM Big5', '-i22a': 'CBM GCR', '-i9': 'DSK', '-i8': 'Apple DOS 3.2', '-i3': 'FM Sector', '-i2': 'CT Raw', '-i5': 'Amiga DOS', '-i4': 'MFM', '-i7': 'CBMDOS  ErrMap', '-i15': 'DEC RX02', '-i14': 'DEC RX01', '-i17': 'CBM RapidLok', '-i16': 'CBM MicroProse', '-i11': 'EMU', '-i10': 'Apple DOS 400/800K', '-i13': 'Amiga Disk Spare', '-i12': 'EMU2', '-i19': 'CBM Vorpal', '-i18': 'CBM Datasoft', '-i8a': 'AppleDOS3.3'}

endTracks = ("x","-e73","-e72","-e79","-e39","-e34","-e76","-e81")

sideModes = {"Both sides":"-g2","Side 0":"-g0","Side 1":"-g1"}
sideModesRv = {'-g2': 'Both sides', '-g1': 'Side 1', '-g0': 'Side 0'}

sectorSizes = {"128":"-z0","256":"-z1","512":"-z3","1024":"-z2"}
sectorSizesRv = {'-z0': '128', '-z1': '256', '-z2': '1024', '-z3': '512'} 

sectorCounts = {"Exactly":"+","At most":"-"}
sectorCountsRv = {'+': 'Exactly', '-': 'At most'}

trackDistances = {"80":"-k1","40":"-k2"}
trackDistancesRv = {"-k1":"80","-k2":"40"}

targetRPMsBasic = {"300":"-v300","288":"-v288","360":"-v360","150":"-v150"}
targetRPMsBasicRv = {'-v150': '150', '-v288': '288', '-v300': '300', '-v360': '360'}

driveDensities = {"High":"-dd0","Low":"-dd1"}
driveDensitiesRv = {"-dd0":"High","-dd1":"Low"}

outputTrackOrders = {"Side 0 descending":"-oo1","Side 1 descending":"-oo2","Side 1 then side 0":"-oo4","Side oriented":"-oo8"}
outputTrackOrdersRv = {'-oo1': 'Side 0 descending', '-oo8': 'Side oriented', '-oo2': 'Side 1 descending', '-oo4': 'Side 1 then side 0'}

global spath
spath = os.getenv("HOME") + '/.diskFormatID/settings.json'

class addTypes(QtGui.QMainWindow, chooseFormatsGUI.Ui_addTypes):
  def __init__(self, parent=None):
    global spath
    super(addTypes, self).__init__(parent)
    self.setupUi(self)
    self.imageTypeCB.clear()
# populate the combo box with the keys in the image variables defined above
    self.imageTypeCB.addItems(imageTypes.keys())
#set the default value actual defaults
#set most of the combo boxes to not editable/greyed out by default (that will be changed if the check box is unchecked
    self.imageTypeCB.setCurrentIndex(self.imageTypeCB.findText('MFM'))
    self.trackDistanceCB.addItems(trackDistances.keys())
    self.trackDistanceCB.setCurrentIndex(self.trackDistanceCB.findText('40'))

    self.trackDistanceCB.setEnabled(False)

    self.sectorCountCB.addItems(sectorCounts.keys())
    self.sectorCountCB.setEnabled(False)

    self.sideModeCB.addItems(sideModes.keys())
    self.sideModeCB.setCurrentIndex(self.sideModeCB.findText('Both sides'))
    self.sideModeCB.setEnabled(False)

    self.sectorSizeCB.addItems(sectorSizes.keys())
    self.sectorSizeCB.setCurrentIndex(self.sectorSizeCB.findText('512'))
    self.sectorSizeCB.setEnabled(False)
    
    self.startTrack.setEnabled(False)
    self.endTrack.setEnabled(False)
    self.sectorCount.setEnabled(False)

    self.targetRPMCB.addItems(targetRPMsBasic.keys())
    self.targetRPMCB.setEnabled(False)


 # if the reset all button is clicked launch that function    
    self.resetTypes.clicked.connect(self.reset_types)

     
#open the spath file for reading
    if os.stat(spath).st_size != 0:  
      self.updateTextBrowserFromJSON()
    else:
     #pass if file is empty
      pass

  def reset_types(self):
    global spath
#open the json file and get the contents
    
    with open(spath ,'r') as settings_file:   
     
      settings = json.load(settings_file)
# try deleting the  outputFormats element/key
      try:
        del settings['outputFormats']
      except KeyError:
        pass
#write back the remaining json      
      jsoutput = json.dumps(settings)
      outfile = open("spath", 'w')
      outfile.write(jsoutput)
      outfile.close()
     
# clear what is in the text browser in the gui
    self.settingsDisplay.clear()
# process that clearance event
    QtGui.QApplication.processEvents()

  def save_and_add(self):
 # this function adds what is in each setting to the json file
    global spath

#check to see if the spath file is empty

    if os.stat(spath).st_size != 0:
# if it is not empty open it for reading
      with open(spath,'r') as settings_file:    
        settings = json.load(settings_file)
#create a variable to store the current input in the image type comobo box        
        imgType = imageTypes[str(self.imageTypeCB.currentText())]
        #print imgType
#create a dictionary to store the set of settings for one disk (if needed)
        diskSetting = {}
        diskSetting.update({"Image type":imgType})
#Check to see  if the side mode combo box is set to default
        if not self.sideModeDefault.isChecked():
# if the side mode combo box is not set to default add the contents of it to the diskSetting dictionary          
          diskSetting.update({"Side mode":sideModes[str(self.sideModeCB.currentText())]})
        if self.flippyMode.isChecked():
          diskSetting.update({"Flippy mode":"-y"})

        if not self.sectorSizeDefault.isChecked():
# if the sector size combo box is not set to default add the contents of it to the diskSetting dictionary          
          diskSetting.update({"Sector size":sectorSizes[str(self.sectorSizeCB.currentText())]})

        if not self.sectorCountDefault.isChecked():
# if the sector count combo box is not set to default add the contents of it to the diskSetting dictionary          
          diskSetting.update({"Sector count":sectorCounts[str(self.sectorCountCB.currentText())] + str(self.sectorCount.text())})

        if not self.trackDistanceDefault.isChecked():
# if the track distance combo box is not set to default add the contents of it to the diskSetting dictionary          
          diskSetting.update({"Track Distance":trackDistances[str(self.trackDistanceCB.currentText())]})
 
        if not self.tracksDefault.isChecked():
          starttr = "-os" + str(self.startTrack.text())
          endtr = "-oe" + str(self.endTrack.text())
          diskSetting.update({"Start track":str(starttr)})
          diskSetting.update({"End track":str(endtr)})

        if not self.targetRPMDefault.isChecked():
# if the target RPM combo box is not set to default add the contents of it to the diskSetting dictionary          
          diskSetting.update({"Target RPM":targetRPMsBasic[str(self.targetRPMCB.currentText())]})

# append the contents of disk settings to the format json element
        if "outputFormats" in settings:
          settings["outputFormats"].append(diskSetting)
        else:
          settings["outputFormats"] = [diskSetting]
#Clear the json file and write back the updated json
        jsoutput = json.dumps(settings)
        outfile = open("spath", 'w')
        outfile.write(jsoutput)
        outfile.close()
      self.settingsDisplay.clear()
#clear the settings text browser in the GUI
#open the spath file and print the contents to the text browser in the gui, one per format instance
  
      self.updateTextBrowserFromJSON()

    else:
#if the spath file is empty you should put something into it     

#this is a hangover from earlier versions where I needed to id/process the imagetype ina a unique way 
      imgType = imageTypes[str(self.imageTypeCB.currentText())]
        #print imgType
#create a dictionary to store the set of settings for one disk (if needed)
      diskSetting = {}
      diskSetting.update({"Image type":imgType})
#Check to see  if the side mode combo box is set to default
      if not self.sideModeDefault.isChecked():
# if the side mode combo box is not set to default add the contents of it to the diskSetting dictionary          
        diskSetting.update({"Side mode":sideModes[str(self.sideModeCB.currentText())]})

      if not self.sectorSizeDefault.isChecked():
# if the sector size combo box is not set to default add the contents of it to the diskSetting dictionary          
        diskSetting.update({"Sector size":sectorSizes[str(self.sectorSizeCB.currentText())]})
      if self.flippyMode.isChecked():
        diskSetting.update({"Flippy mode":"-y"})

      if not self.sectorCountDefault.isChecked():
# if the sector count combo box is not set to default add the contents of it to the diskSetting dictionary          
        diskSetting.update({"Sector count":sectorCounts[str(self.sectorCountCB.currentText())] + str(self.sectorCount.text())})

      if not self.trackDistanceDefault.isChecked():
# if the track distance combo box is not set to default add the contents of it to the diskSetting dictionary          
        diskSetting.update({"Track Distance":trackDistances[str(self.trackDistanceCB.currentText())]})

      if not self.tracksDefault.isChecked():
        starttr = "-os" + str(self.startTrack.text())
        endtr = "-oe" + str(self.endTrack.text())
        diskSetting.update({"Start track":starttr})
        diskSetting.update({"End track":endtr})


      if not self.targetRPMDefault.isChecked():
# if the target RPM combo box is not set to default add the contents of it to the diskSetting dictionary          
        diskSetting.update({"Target RPM":targetRPMsBasic[str(self.targetRPMCB.currentText())]})

#now write this all back
      settings = {"outputFormats":[diskSetting]}
      jsoutput = json.dumps(settings)
      outfile = open("spath", 'w')
      outfile.write(jsoutput)
      outfile.close()
      self.settingsDisplay.clear()
      self.updateTextBrowserFromJSON()

  def updateTextBrowserFromJSON(self):

    global spath
#used to update what is in the textbrowser box in the GUI from the JSON file
    with open(spath) as settings_file:    
      num = 0
      settings = json.load(settings_file)
# get all the formats already stored in the file
      if "outputFormats" in settings:
        for format in settings["outputFormats"]:
          num = num + 1
#create a variable to add content to be put into the text browser in the gui       
          setting = ""
       
          for x in format:
#For each format add the information to the setting variable, starting with Image type
            if x == "Image type":        
              setting =  x + ": " + imageFmts[str(format[x])] + setting
            elif x == "Sector size":
              setting = setting + ", " + x + ": " + sectorSizesRv[str(format[x])]  
        
            elif x == "Side mode":
              setting = setting + ", " + x + ": " + sideModesRv[str(format[x])]          

            elif x == "Sector count":
              setting = setting + ", " + x + ": " + sectorCountsRv[str(format[x])[0]] + str(self.sectorCount.text())          

            elif x == "Track distance":
              setting = setting + ", " + x + ": " + trackDistancesRv[str(format[x])]          

            elif x == "Target RPM":
              setting = setting + ", " + x + ": " + targetRPMsBasicRv[str(format[x])]         

            elif x == "Flippy mode": 
              setting = setting + ", " + x + ": " + str(format[x])

            elif x == "Start track": 
              setting = setting + ", " + x + ": " + str(format[x])[2:]

            elif x == "End track": 
              setting = setting + ", " + x + ": " + str(format[x])[2:]

#update the text browser with the information in each format
          self.settingsDisplay.append("Image " + str(num) + ": " + setting)
# process the update
        QtGui.QApplication.processEvents()

      
      settings_file.close()


# set up functions to change the editablility of the various widgets when the checkboxes change to unchecked
  def tracks_default_change(self):
    if self.tracksDefault.isChecked():
      self.startTrack.setEnabled(False)
      self.endTrack.setEnabled(False)
    else:
      self.startTrack.setEnabled(True)
      self.endTrack.setEnabled(True)
    

  def side_mode_default_change(self):
    
    if self.sideModeDefault.isChecked():
      self.sideModeCB.setEnabled(False)
    else:
      self.sideModeCB.setEnabled(True)
  
  def sector_count_default_change(self):
   
    if self.sectorCountDefault.isChecked():
      self.sectorCountCB.setEnabled(False)
      self.sectorCount.setEnabled(False)
    else:
      self.sectorCountCB.setEnabled(True)
      self.sectorCount.setEnabled(True)

  def sector_size_default_change(self):
   
    if self.sectorSizeDefault.isChecked():
      self.sectorSizeCB.setEnabled(False)
    else:
      self.sectorSizeCB.setEnabled(True)

  def track_distance_default_change(self):
    
    if self.trackDistanceDefault.isChecked():
      self.trackDistanceCB.setEnabled(False)
    else:
      self.trackDistanceCB.setEnabled(True)

  def target_RPM_default_change(self):
    if self.targetRPMDefault.isChecked():
      self.targetRPMCB.setEnabled(False)
    else:
      self.targetRPMCB.setEnabled(True)

# Don't think I strictly need this one
  def flippy_change(self):
    if self.flippyMode.isChecked(): 
      True
    else:
      False


def main():
    app = QtGui.QApplication(sys.argv)
    form = addTypes()
    form.show()
    app.exec_()
  

	

if __name__ == '__main__':
    main()
