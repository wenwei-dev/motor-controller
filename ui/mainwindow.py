# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Thu Jun 15 18:06:26 2017
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1041, 667)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.playPAUWidget = QtGui.QTabWidget(self.centralwidget)
        self.playPAUWidget.setObjectName(_fromUtf8("playPAUWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.frame = QtGui.QFrame(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.saveButton = QtGui.QPushButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/save.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.resetButton = QtGui.QPushButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/reset.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetButton.setIcon(icon1)
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.horizontalLayout_2.addWidget(self.resetButton)
        self.neutralButton = QtGui.QPushButton(self.frame)
        self.neutralButton.setObjectName(_fromUtf8("neutralButton"))
        self.horizontalLayout_2.addWidget(self.neutralButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.enableConfigMotorsCheckBox = QtGui.QCheckBox(self.frame)
        self.enableConfigMotorsCheckBox.setObjectName(_fromUtf8("enableConfigMotorsCheckBox"))
        self.horizontalLayout_2.addWidget(self.enableConfigMotorsCheckBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.motorConfigTableWidget = QtGui.QTableWidget(self.frame)
        self.motorConfigTableWidget.setLineWidth(0)
        self.motorConfigTableWidget.setAlternatingRowColors(True)
        self.motorConfigTableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.motorConfigTableWidget.setShowGrid(True)
        self.motorConfigTableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.motorConfigTableWidget.setObjectName(_fromUtf8("motorConfigTableWidget"))
        self.motorConfigTableWidget.setColumnCount(0)
        self.motorConfigTableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.motorConfigTableWidget)
        self.verticalLayout_7.addWidget(self.frame)
        self.playPAUWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.linkBlenderButton = QtGui.QPushButton(self.tab_2)
        self.linkBlenderButton.setCheckable(True)
        self.linkBlenderButton.setObjectName(_fromUtf8("linkBlenderButton"))
        self.horizontalLayout.addWidget(self.linkBlenderButton)
        self.loadFrameButton = QtGui.QPushButton(self.tab_2)
        self.loadFrameButton.setObjectName(_fromUtf8("loadFrameButton"))
        self.horizontalLayout.addWidget(self.loadFrameButton)
        self.shapekeyComboBox = QtGui.QComboBox(self.tab_2)
        self.shapekeyComboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.shapekeyComboBox.setObjectName(_fromUtf8("shapekeyComboBox"))
        self.horizontalLayout.addWidget(self.shapekeyComboBox)
        self.frameSlider = QtGui.QSlider(self.tab_2)
        self.frameSlider.setEnabled(False)
        self.frameSlider.setPageStep(10)
        self.frameSlider.setOrientation(QtCore.Qt.Horizontal)
        self.frameSlider.setObjectName(_fromUtf8("frameSlider"))
        self.horizontalLayout.addWidget(self.frameSlider)
        self.frameSpinBox = QtGui.QSpinBox(self.tab_2)
        self.frameSpinBox.setObjectName(_fromUtf8("frameSpinBox"))
        self.horizontalLayout.addWidget(self.frameSpinBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.splitter = QtGui.QSplitter(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.frame_2 = QtGui.QFrame(self.splitter)
        self.frame_2.setFrameShape(QtGui.QFrame.Panel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.trainButton = QtGui.QPushButton(self.frame_2)
        self.trainButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.trainButton.setObjectName(_fromUtf8("trainButton"))
        self.horizontalLayout_3.addWidget(self.trainButton)
        self.plotButton = QtGui.QPushButton(self.frame_2)
        self.plotButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.horizontalLayout_3.addWidget(self.plotButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.resetSavedMotorValuesButton = QtGui.QPushButton(self.frame_2)
        self.resetSavedMotorValuesButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.resetSavedMotorValuesButton.setObjectName(_fromUtf8("resetSavedMotorValuesButton"))
        self.horizontalLayout_3.addWidget(self.resetSavedMotorValuesButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pauValueTableWidget = QtGui.QTableWidget(self.frame_2)
        self.pauValueTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.pauValueTableWidget.setAlternatingRowColors(True)
        self.pauValueTableWidget.setObjectName(_fromUtf8("pauValueTableWidget"))
        self.pauValueTableWidget.setColumnCount(2)
        self.pauValueTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.pauValueTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.pauValueTableWidget.setHorizontalHeaderItem(1, item)
        self.pauValueTableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.pauValueTableWidget, 3, 0, 1, 1)
        self.savedMotorValueTableWidget = QtGui.QTableWidget(self.frame_2)
        self.savedMotorValueTableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.savedMotorValueTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.savedMotorValueTableWidget.setAlternatingRowColors(True)
        self.savedMotorValueTableWidget.setObjectName(_fromUtf8("savedMotorValueTableWidget"))
        self.savedMotorValueTableWidget.setColumnCount(2)
        self.savedMotorValueTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.savedMotorValueTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.savedMotorValueTableWidget.setHorizontalHeaderItem(1, item)
        self.savedMotorValueTableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.savedMotorValueTableWidget, 3, 1, 1, 1)
        self.keyMotorFrameCheckBox = QtGui.QCheckBox(self.frame_2)
        self.keyMotorFrameCheckBox.setObjectName(_fromUtf8("keyMotorFrameCheckBox"))
        self.gridLayout.addWidget(self.keyMotorFrameCheckBox, 0, 1, 1, 1)
        self.keyShapeFrameCheckBox = QtGui.QCheckBox(self.frame_2)
        self.keyShapeFrameCheckBox.setEnabled(False)
        self.keyShapeFrameCheckBox.setObjectName(_fromUtf8("keyShapeFrameCheckBox"))
        self.gridLayout.addWidget(self.keyShapeFrameCheckBox, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.frame1 = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setFrameShape(QtGui.QFrame.Panel)
        self.frame1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame1.setObjectName(_fromUtf8("frame1"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame1)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.defaultMapperButton = QtGui.QPushButton(self.frame1)
        self.defaultMapperButton.setCheckable(True)
        self.defaultMapperButton.setChecked(True)
        self.defaultMapperButton.setObjectName(_fromUtf8("defaultMapperButton"))
        self.horizontalLayout_6.addWidget(self.defaultMapperButton)
        self.trainedMapperButton = QtGui.QPushButton(self.frame1)
        self.trainedMapperButton.setCheckable(True)
        self.trainedMapperButton.setObjectName(_fromUtf8("trainedMapperButton"))
        self.horizontalLayout_6.addWidget(self.trainedMapperButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.saveMotorValuesButton = QtGui.QPushButton(self.frame1)
        self.saveMotorValuesButton.setEnabled(False)
        self.saveMotorValuesButton.setObjectName(_fromUtf8("saveMotorValuesButton"))
        self.horizontalLayout_6.addWidget(self.saveMotorValuesButton)
        self.enablePlayMotorsCheckBox = QtGui.QCheckBox(self.frame1)
        self.enablePlayMotorsCheckBox.setObjectName(_fromUtf8("enablePlayMotorsCheckBox"))
        self.horizontalLayout_6.addWidget(self.enablePlayMotorsCheckBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.motorValueTableWidget = QtGui.QTableWidget(self.frame1)
        self.motorValueTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.motorValueTableWidget.setAlternatingRowColors(True)
        self.motorValueTableWidget.setObjectName(_fromUtf8("motorValueTableWidget"))
        self.motorValueTableWidget.setColumnCount(3)
        self.motorValueTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.motorValueTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.motorValueTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.motorValueTableWidget.setHorizontalHeaderItem(2, item)
        self.motorValueTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.motorValueTableWidget.horizontalHeader().setStretchLastSection(True)
        self.motorValueTableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_5.addWidget(self.motorValueTableWidget)
        self.verticalLayout_8.addWidget(self.splitter)
        self.playPAUWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter_3 = QtGui.QSplitter(self.tab_5)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.pauTableWidget = QtGui.QTableWidget(self.splitter_3)
        self.pauTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.pauTableWidget.setAlternatingRowColors(True)
        self.pauTableWidget.setObjectName(_fromUtf8("pauTableWidget"))
        self.pauTableWidget.setColumnCount(2)
        self.pauTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.pauTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.pauTableWidget.setHorizontalHeaderItem(1, item)
        self.pauTableWidget.horizontalHeader().setStretchLastSection(True)
        self.motorMonitorTableWidget = QtGui.QTableWidget(self.splitter_3)
        self.motorMonitorTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.motorMonitorTableWidget.setAlternatingRowColors(True)
        self.motorMonitorTableWidget.setObjectName(_fromUtf8("motorMonitorTableWidget"))
        self.motorMonitorTableWidget.setColumnCount(2)
        self.motorMonitorTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.motorMonitorTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.motorMonitorTableWidget.setHorizontalHeaderItem(1, item)
        self.motorMonitorTableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.splitter_3)
        self.playPAUWidget.addTab(self.tab_5, _fromUtf8(""))
        self.verticalLayout_6.addWidget(self.playPAUWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.treeView = QtGui.QTreeView(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeView.setAnimated(True)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.verticalLayout_3.addWidget(self.treeView)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionExit = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/quit.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionEditMotors = QtGui.QAction(MainWindow)
        self.actionEditMotors.setObjectName(_fromUtf8("actionEditMotors"))
        self.actionSave_Motor_Settings = QtGui.QAction(MainWindow)
        self.actionSave_Motor_Settings.setIcon(icon)
        self.actionSave_Motor_Settings.setObjectName(_fromUtf8("actionSave_Motor_Settings"))
        self.actionLoad_Motor_Settings = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/open.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad_Motor_Settings.setIcon(icon3)
        self.actionLoad_Motor_Settings.setObjectName(_fromUtf8("actionLoad_Motor_Settings"))
        self.actionClearMotorValues = QtGui.QAction(MainWindow)
        self.actionClearMotorValues.setObjectName(_fromUtf8("actionClearMotorValues"))
        self.toolBar.addAction(self.actionLoad_Motor_Settings)
        self.toolBar.addAction(self.actionSave_Motor_Settings)
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.playPAUWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.frameSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.frameSpinBox.setValue)
        QtCore.QObject.connect(self.frameSpinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.frameSlider.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ServoController", None))
        self.saveButton.setText(_translate("MainWindow", "Save", None))
        self.resetButton.setText(_translate("MainWindow", "Reset", None))
        self.neutralButton.setText(_translate("MainWindow", "Neutral", None))
        self.enableConfigMotorsCheckBox.setText(_translate("MainWindow", "Enable Motors", None))
        self.motorConfigTableWidget.setSortingEnabled(True)
        self.playPAUWidget.setTabText(self.playPAUWidget.indexOf(self.tab), _translate("MainWindow", "Config", None))
        self.linkBlenderButton.setText(_translate("MainWindow", "Link Blender", None))
        self.loadFrameButton.setText(_translate("MainWindow", "Load Frames", None))
        self.trainButton.setText(_translate("MainWindow", "Train", None))
        self.plotButton.setText(_translate("MainWindow", "Plot", None))
        self.resetSavedMotorValuesButton.setText(_translate("MainWindow", "Reset", None))
        item = self.pauValueTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Key", None))
        item = self.pauValueTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value", None))
        item = self.savedMotorValueTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Motor Name", None))
        item = self.savedMotorValueTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Target", None))
        self.keyMotorFrameCheckBox.setText(_translate("MainWindow", "Key Frame", None))
        self.keyShapeFrameCheckBox.setText(_translate("MainWindow", "Key Frame", None))
        self.defaultMapperButton.setText(_translate("MainWindow", "Default Mapper", None))
        self.trainedMapperButton.setText(_translate("MainWindow", "Trained Mapper", None))
        self.saveMotorValuesButton.setText(_translate("MainWindow", "Save Motor Values", None))
        self.saveMotorValuesButton.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.enablePlayMotorsCheckBox.setText(_translate("MainWindow", "Enable Motors", None))
        item = self.motorValueTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Motor Name", None))
        item = self.motorValueTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value", None))
        item = self.motorValueTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Editor", None))
        self.playPAUWidget.setTabText(self.playPAUWidget.indexOf(self.tab_2), _translate("MainWindow", "Calibration", None))
        item = self.pauTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Key", None))
        item = self.pauTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value", None))
        item = self.motorMonitorTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Motor Name", None))
        item = self.motorMonitorTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value", None))
        self.playPAUWidget.setTabText(self.playPAUWidget.indexOf(self.tab_5), _translate("MainWindow", "Monitor", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionEditMotors.setText(_translate("MainWindow", "Edit Motors", None))
        self.actionEditMotors.setToolTip(_translate("MainWindow", "Edit Motors", None))
        self.actionSave_Motor_Settings.setText(_translate("MainWindow", "Save Motor Settings", None))
        self.actionLoad_Motor_Settings.setText(_translate("MainWindow", "Load Motor Settings", None))
        self.actionClearMotorValues.setText(_translate("MainWindow", "Clear Motor Values", None))
        self.actionClearMotorValues.setToolTip(_translate("MainWindow", "Clear Motor Values", None))

import res_rc
