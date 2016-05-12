# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diskIDMainGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_kryoMain(object):
    def setupUi(self, kryoMain):
        kryoMain.setObjectName(_fromUtf8("kryoMain"))
        kryoMain.resize(770, 600)
        self.centralwidget = QtGui.QWidget(kryoMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.chooseFormats = QtGui.QPushButton(self.centralwidget)
        self.chooseFormats.setGeometry(QtCore.QRect(30, 10, 201, 27))
        self.chooseFormats.setObjectName(_fromUtf8("chooseFormats"))
        self.createImages = QtGui.QPushButton(self.centralwidget)
        self.createImages.setGeometry(QtCore.QRect(30, 50, 201, 71))
        self.createImages.setObjectName(_fromUtf8("createImages"))
        self.tryMounting = QtGui.QPushButton(self.centralwidget)
        self.tryMounting.setGeometry(QtCore.QRect(30, 330, 191, 27))
        self.tryMounting.setObjectName(_fromUtf8("tryMounting"))
        self.imageCreationResults = QtGui.QTextBrowser(self.centralwidget)
        self.imageCreationResults.setGeometry(QtCore.QRect(30, 140, 711, 181))
        self.imageCreationResults.setObjectName(_fromUtf8("imageCreationResults"))
        self.MountingResults = QtGui.QTextBrowser(self.centralwidget)
        self.MountingResults.setGeometry(QtCore.QRect(31, 360, 711, 192))
        self.MountingResults.setObjectName(_fromUtf8("MountingResults"))
        self.deleteUnmountable = QtGui.QCheckBox(self.centralwidget)
        self.deleteUnmountable.setGeometry(QtCore.QRect(225, 333, 171, 22))
        self.deleteUnmountable.setChecked(False)
        self.deleteUnmountable.setObjectName(_fromUtf8("deleteUnmountable"))
        self.browseOutputDir = QtGui.QPushButton(self.centralwidget)
        self.browseOutputDir.setGeometry(QtCore.QRect(250, 80, 141, 27))
        self.browseOutputDir.setObjectName(_fromUtf8("browseOutputDir"))
        self.browseInpDir = QtGui.QPushButton(self.centralwidget)
        self.browseInpDir.setGeometry(QtCore.QRect(250, 46, 141, 27))
        self.browseInpDir.setObjectName(_fromUtf8("browseInpDir"))
        self.browseDTCDir = QtGui.QPushButton(self.centralwidget)
        self.browseDTCDir.setGeometry(QtCore.QRect(250, 10, 141, 27))
        self.browseDTCDir.setObjectName(_fromUtf8("browseDTCDir"))
        self.inputDir = QtGui.QLineEdit(self.centralwidget)
        self.inputDir.setGeometry(QtCore.QRect(410, 46, 331, 27))
        self.inputDir.setObjectName(_fromUtf8("inputDir"))
        self.outputDir = QtGui.QLineEdit(self.centralwidget)
        self.outputDir.setGeometry(QtCore.QRect(410, 80, 331, 27))
        self.outputDir.setObjectName(_fromUtf8("outputDir"))
        self.DTCDir = QtGui.QLineEdit(self.centralwidget)
        self.DTCDir.setGeometry(QtCore.QRect(410, 11, 331, 27))
        self.DTCDir.setObjectName(_fromUtf8("DTCDir"))
        self.saveMountingResults = QtGui.QPushButton(self.centralwidget)
        self.saveMountingResults.setGeometry(QtCore.QRect(601, 330, 141, 27))
        self.saveMountingResults.setObjectName(_fromUtf8("saveMountingResults"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 319, 711, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.saveDTCResults = QtGui.QPushButton(self.centralwidget)
        self.saveDTCResults.setGeometry(QtCore.QRect(601, 109, 141, 27))
        self.saveDTCResults.setObjectName(_fromUtf8("saveDTCResults"))
        self.DTCInstances = QtGui.QLineEdit(self.centralwidget)
        self.DTCInstances.setGeometry(QtCore.QRect(503, 109, 41, 27))
        self.DTCInstances.setObjectName(_fromUtf8("DTCInstances"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(253, 115, 261, 17))
        self.label.setObjectName(_fromUtf8("label"))
        kryoMain.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(kryoMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        kryoMain.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(kryoMain)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        kryoMain.setStatusBar(self.statusbar)

        self.retranslateUi(kryoMain)
        QtCore.QObject.connect(self.chooseFormats, QtCore.SIGNAL(_fromUtf8("clicked()")), kryoMain.choose_formats)
        QtCore.QObject.connect(self.createImages, QtCore.SIGNAL(_fromUtf8("clicked()")), kryoMain.create_images)
        QtCore.QObject.connect(self.tryMounting, QtCore.SIGNAL(_fromUtf8("clicked()")), kryoMain.try_mounting)
        QtCore.QObject.connect(self.browseDTCDir, QtCore.SIGNAL(_fromUtf8("clicked()")), kryoMain.browse_dtc_dir)
        QtCore.QObject.connect(self.browseInpDir, QtCore.SIGNAL(_fromUtf8("clicked()")), kryoMain.browse_inp_dir)
        QtCore.QObject.connect(self.browseOutputDir, QtCore.SIGNAL(_fromUtf8("clicked()")), kryoMain.browse_output_dir)
        QtCore.QObject.connect(self.deleteUnmountable, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), kryoMain.delete_unmountable_change)
        QtCore.QObject.connect(self.saveMountingResults, QtCore.SIGNAL(_fromUtf8("clicked()")), kryoMain.save_mounting_results)
        QtCore.QObject.connect(self.saveDTCResults, QtCore.SIGNAL(_fromUtf8("clicked()")), kryoMain.save_dtc_results)
        QtCore.QMetaObject.connectSlotsByName(kryoMain)

    def retranslateUi(self, kryoMain):
        kryoMain.setWindowTitle(_translate("kryoMain", "Disk format identifier", None))
        self.chooseFormats.setText(_translate("kryoMain", "Choose formats to create", None))
        self.createImages.setText(_translate("kryoMain", "Create images", None))
        self.tryMounting.setText(_translate("kryoMain", "Try mounting", None))
        self.deleteUnmountable.setText(_translate("kryoMain", "Delete unmountable", None))
        self.browseOutputDir.setText(_translate("kryoMain", "Output Directory", None))
        self.browseInpDir.setText(_translate("kryoMain", "Input Directory", None))
        self.browseDTCDir.setText(_translate("kryoMain", "DTC Directory", None))
        self.saveMountingResults.setText(_translate("kryoMain", "Save Results", None))
        self.saveDTCResults.setText(_translate("kryoMain", "Save Results", None))
        self.label.setText(_translate("kryoMain", "Maximum concurrent DTC instances:", None))

