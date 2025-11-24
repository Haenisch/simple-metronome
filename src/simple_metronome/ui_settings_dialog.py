# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QLabel, QSizePolicy, QSpinBox, QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(237, 110)
        self.gridLayout_3 = QGridLayout(Settings)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_Volume = QGroupBox(Settings)
        self.groupBox_Volume.setObjectName(u"groupBox_Volume")
        self.gridLayout_2 = QGridLayout(self.groupBox_Volume)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinBox_backbeatVolume = QSpinBox(self.groupBox_Volume)
        self.spinBox_backbeatVolume.setObjectName(u"spinBox_backbeatVolume")
        self.spinBox_backbeatVolume.setMaximum(100)
        self.spinBox_backbeatVolume.setSingleStep(1)
        self.spinBox_backbeatVolume.setValue(80)

        self.gridLayout.addWidget(self.spinBox_backbeatVolume, 1, 1, 1, 1)

        self.label_backbeatVolume = QLabel(self.groupBox_Volume)
        self.label_backbeatVolume.setObjectName(u"label_backbeatVolume")
        self.label_backbeatVolume.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_backbeatVolume, 1, 0, 1, 1)

        self.spinBox_downbeatVolume = QSpinBox(self.groupBox_Volume)
        self.spinBox_downbeatVolume.setObjectName(u"spinBox_downbeatVolume")
        self.spinBox_downbeatVolume.setMaximum(100)
        self.spinBox_downbeatVolume.setSingleStep(1)
        self.spinBox_downbeatVolume.setValue(100)

        self.gridLayout.addWidget(self.spinBox_downbeatVolume, 0, 1, 1, 1)

        self.label_downbeatVolume = QLabel(self.groupBox_Volume)
        self.label_downbeatVolume.setObjectName(u"label_downbeatVolume")
        self.label_downbeatVolume.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_downbeatVolume, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_Volume, 0, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.label_backbeatVolume.setBuddy(self.spinBox_backbeatVolume)
        self.label_downbeatVolume.setBuddy(self.spinBox_downbeatVolume)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.groupBox_Volume.setTitle(QCoreApplication.translate("Settings", u"Volume", None))
        self.spinBox_backbeatVolume.setSuffix(QCoreApplication.translate("Settings", u" %", None))
        self.label_backbeatVolume.setText(QCoreApplication.translate("Settings", u"&Backbeat Volume:", None))
        self.spinBox_downbeatVolume.setSuffix(QCoreApplication.translate("Settings", u" %", None))
        self.label_downbeatVolume.setText(QCoreApplication.translate("Settings", u"&Downbeat Volume:", None))
    # retranslateUi

