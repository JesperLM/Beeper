# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 609)
        MainWindow.setMinimumSize(QtCore.QSize(500, 600))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(-1, 9, -1, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(250, 20))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.entryNoice = QtWidgets.QLineEdit(self.centralwidget)
        self.entryNoice.setMinimumSize(QtCore.QSize(100, 0))
        self.entryNoice.setMaximumSize(QtCore.QSize(250, 16777215))
        self.entryNoice.setObjectName("entryNoice")
        self.verticalLayout.addWidget(self.entryNoice)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 9, 3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnStart.setFlat(True)
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout_3.addWidget(self.btnStart)
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setEnabled(True)
        self.btnStop.setCheckable(False)
        self.btnStop.setFlat(True)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout_3.addWidget(self.btnStop)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphFFT = FFTWidget(self.centralwidget)
        self.graphFFT.setMinimumSize(QtCore.QSize(500, 0))
        self.graphFFT.setBaseSize(QtCore.QSize(500, 200))
        self.graphFFT.setObjectName("graphFFT")
        self.verticalLayout_2.addWidget(self.graphFFT)
        self.graphdB = dBWidget(self.centralwidget)
        self.graphdB.setMinimumSize(QtCore.QSize(500, 0))
        self.graphdB.setBaseSize(QtCore.QSize(500, 200))
        self.graphdB.setObjectName("graphdB")
        self.verticalLayout_2.addWidget(self.graphdB)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Beeper"))
        self.label.setText(_translate("MainWindow", "Beep Level [dB]:"))
        self.entryNoice.setText(_translate("MainWindow", "55"))
        self.btnStart.setText(_translate("MainWindow", "Run"))
        self.btnStop.setText(_translate("MainWindow", "Stop"))


from Plotter import FFTWidget, dBWidget
