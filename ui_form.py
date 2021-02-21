# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BeeTCEMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(450, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(450, 350))
        MainWindow.setMaximumSize(QSize(450, 350))
        MainWindow.setAnimated(True)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.p2_lineEdit = QLineEdit(self.centralwidget)
        self.p2_lineEdit.setObjectName(u"p2_lineEdit")
        self.p2_lineEdit.setGeometry(QRect(10, 30, 341, 22))
        self.p2_label = QLabel(self.centralwidget)
        self.p2_label.setObjectName(u"p2_label")
        self.p2_label.setGeometry(QRect(10, 10, 341, 16))
        self.p2_browse = QPushButton(self.centralwidget)
        self.p2_browse.setObjectName(u"p2_browse")
        self.p2_browse.setGeometry(QRect(360, 30, 81, 24))
        self.p2ce_lineEdit = QLineEdit(self.centralwidget)
        self.p2ce_lineEdit.setObjectName(u"p2ce_lineEdit")
        self.p2ce_lineEdit.setGeometry(QRect(10, 80, 341, 22))
        self.p2ce_label = QLabel(self.centralwidget)
        self.p2ce_label.setObjectName(u"p2ce_label")
        self.p2ce_label.setGeometry(QRect(10, 60, 341, 16))
        self.p2ce_browse = QPushButton(self.centralwidget)
        self.p2ce_browse.setObjectName(u"p2ce_browse")
        self.p2ce_browse.setGeometry(QRect(360, 80, 81, 24))
        self.vmf_browse = QPushButton(self.centralwidget)
        self.vmf_browse.setObjectName(u"vmf_browse")
        self.vmf_browse.setGeometry(QRect(360, 130, 81, 24))
        self.vmf_label = QLabel(self.centralwidget)
        self.vmf_label.setObjectName(u"vmf_label")
        self.vmf_label.setGeometry(QRect(10, 110, 341, 16))
        self.vmf_lineEdit = QLineEdit(self.centralwidget)
        self.vmf_lineEdit.setObjectName(u"vmf_lineEdit")
        self.vmf_lineEdit.setGeometry(QRect(10, 130, 341, 22))
        self.speedrun_toggle = QCheckBox(self.centralwidget)
        self.speedrun_toggle.setObjectName(u"speedrun_toggle")
        self.speedrun_toggle.setGeometry(QRect(10, 160, 411, 20))
        self.speedrun_toggle.setAcceptDrops(False)
        self.speedrun_toggle.setCheckable(True)
        self.speedrun_toggle.setDisabled(True)
        self.speedrun_toggle.setChecked(False)
        self.speedrun_toggle.setTristate(False)
        self.compile_label = QLabel(self.centralwidget)
        self.compile_label.setObjectName(u"compile_label")
        self.compile_label.setGeometry(QRect(10, 190, 111, 16))
        self.setting_full = QRadioButton(self.centralwidget)
        self.setting_full.setObjectName(u"setting_full")
        self.setting_full.setGeometry(QRect(10, 210, 101, 20))
        self.setting_fast = QRadioButton(self.centralwidget)
        self.setting_fast.setObjectName(u"setting_fast")
        self.setting_fast.setGeometry(QRect(120, 210, 171, 20))
        self.setting_fast_fullbright = QRadioButton(self.centralwidget)
        self.setting_fast_fullbright.setObjectName(u"setting_fast_fullbright")
        self.setting_fast_fullbright.setGeometry(QRect(230, 210, 171, 20))
        self.compile_button = QPushButton(self.centralwidget)
        self.compile_button.setObjectName(u"compile_button")
        self.compile_button.setGeometry(QRect(10, 280, 431, 61))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BeeToCE Converter", None))
        self.p2_label.setText(QCoreApplication.translate("MainWindow", u"Path to your Portal 2 Folder:", None))
        self.p2_browse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.p2ce_label.setText(QCoreApplication.translate("MainWindow", u"Path to your Portal 2: Community Edition Folder:", None))
        self.p2ce_browse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.vmf_browse.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.vmf_label.setText(QCoreApplication.translate("MainWindow", u"Path to your exported puzzlemaker VMF:", None))
        self.speedrun_toggle.setText(QCoreApplication.translate("MainWindow", u"Disable \"Speedrunner\" Glitches.", None))
        self.compile_label.setText(QCoreApplication.translate("MainWindow", u"Compile Options:", None))
        self.setting_full.setText(QCoreApplication.translate("MainWindow", u"Full Compile", None))
        self.setting_fast.setText(QCoreApplication.translate("MainWindow", u"Fast Compile", None))
        self.setting_fast_fullbright.setText(QCoreApplication.translate("MainWindow", u"Fast Compile (Fullbright)", None))
        self.compile_button.setText(QCoreApplication.translate("MainWindow", u"Compile Map", None))
    # retranslateUi

