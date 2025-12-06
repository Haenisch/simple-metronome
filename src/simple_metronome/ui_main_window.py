# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)
import resource_files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(528, 312)
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        self.action_Quit = QAction(MainWindow)
        self.action_Quit.setObjectName(u"action_Quit")
        self.action_Preferences = QAction(MainWindow)
        self.action_Preferences.setObjectName(u"action_Preferences")
        self.action_ToggleViewMode = QAction(MainWindow)
        self.action_ToggleViewMode.setObjectName(u"action_ToggleViewMode")
        self.action_OpenDownbeatSoundFile = QAction(MainWindow)
        self.action_OpenDownbeatSoundFile.setObjectName(u"action_OpenDownbeatSoundFile")
        self.action_OpenBackbeatSoundFile = QAction(MainWindow)
        self.action_OpenBackbeatSoundFile.setObjectName(u"action_OpenBackbeatSoundFile")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_presets = QGroupBox(self.centralwidget)
        self.groupBox_presets.setObjectName(u"groupBox_presets")
        self.verticalLayout = QVBoxLayout(self.groupBox_presets)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_selectDownbeatSound = QPushButton(self.groupBox_presets)
        self.pushButton_selectDownbeatSound.setObjectName(u"pushButton_selectDownbeatSound")
        self.pushButton_selectDownbeatSound.setMinimumSize(QSize(0, 32))
        self.pushButton_selectDownbeatSound.setMaximumSize(QSize(32, 48))
        self.pushButton_selectDownbeatSound.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon = QIcon()
        icon.addFile(u":/images/images/open-downbeat-sound-file-symbol.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_selectDownbeatSound.setIcon(icon)
        self.pushButton_selectDownbeatSound.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButton_selectDownbeatSound)

        self.pushButton_selectRegularBeatsSound = QPushButton(self.groupBox_presets)
        self.pushButton_selectRegularBeatsSound.setObjectName(u"pushButton_selectRegularBeatsSound")
        self.pushButton_selectRegularBeatsSound.setMinimumSize(QSize(0, 32))
        self.pushButton_selectRegularBeatsSound.setMaximumSize(QSize(32, 48))
        self.pushButton_selectRegularBeatsSound.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/images/images/open-backbeat-sound-file-symbol.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_selectRegularBeatsSound.setIcon(icon1)
        self.pushButton_selectRegularBeatsSound.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButton_selectRegularBeatsSound)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.pushButton_preset1 = QPushButton(self.groupBox_presets)
        self.pushButton_preset1.setObjectName(u"pushButton_preset1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_preset1.sizePolicy().hasHeightForWidth())
        self.pushButton_preset1.setSizePolicy(sizePolicy)
        self.pushButton_preset1.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_preset1.setFont(font)
        self.pushButton_preset1.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.verticalLayout.addWidget(self.pushButton_preset1)

        self.pushButton_preset2 = QPushButton(self.groupBox_presets)
        self.pushButton_preset2.setObjectName(u"pushButton_preset2")
        sizePolicy.setHeightForWidth(self.pushButton_preset2.sizePolicy().hasHeightForWidth())
        self.pushButton_preset2.setSizePolicy(sizePolicy)
        self.pushButton_preset2.setMinimumSize(QSize(0, 0))
        self.pushButton_preset2.setFont(font)
        self.pushButton_preset2.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.verticalLayout.addWidget(self.pushButton_preset2)

        self.pushButton_preset3 = QPushButton(self.groupBox_presets)
        self.pushButton_preset3.setObjectName(u"pushButton_preset3")
        sizePolicy.setHeightForWidth(self.pushButton_preset3.sizePolicy().hasHeightForWidth())
        self.pushButton_preset3.setSizePolicy(sizePolicy)
        self.pushButton_preset3.setMinimumSize(QSize(0, 0))
        self.pushButton_preset3.setFont(font)
        self.pushButton_preset3.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.verticalLayout.addWidget(self.pushButton_preset3)

        self.pushButton_preset4 = QPushButton(self.groupBox_presets)
        self.pushButton_preset4.setObjectName(u"pushButton_preset4")
        sizePolicy.setHeightForWidth(self.pushButton_preset4.sizePolicy().hasHeightForWidth())
        self.pushButton_preset4.setSizePolicy(sizePolicy)
        self.pushButton_preset4.setMinimumSize(QSize(0, 0))
        self.pushButton_preset4.setFont(font)
        self.pushButton_preset4.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.verticalLayout.addWidget(self.pushButton_preset4)

        self.pushButton_preset5 = QPushButton(self.groupBox_presets)
        self.pushButton_preset5.setObjectName(u"pushButton_preset5")
        sizePolicy.setHeightForWidth(self.pushButton_preset5.sizePolicy().hasHeightForWidth())
        self.pushButton_preset5.setSizePolicy(sizePolicy)
        self.pushButton_preset5.setMinimumSize(QSize(0, 0))
        self.pushButton_preset5.setFont(font)
        self.pushButton_preset5.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.verticalLayout.addWidget(self.pushButton_preset5)


        self.gridLayout.addWidget(self.groupBox_presets, 0, 0, 3, 1)

        self.groupBox_timeSignaturePresets = QGroupBox(self.centralwidget)
        self.groupBox_timeSignaturePresets.setObjectName(u"groupBox_timeSignaturePresets")
        self._2 = QHBoxLayout(self.groupBox_timeSignaturePresets)
        self._2.setObjectName(u"_2")
        self.pushButton_timeSignature_2_4 = QPushButton(self.groupBox_timeSignaturePresets)
        self.pushButton_timeSignature_2_4.setObjectName(u"pushButton_timeSignature_2_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_timeSignature_2_4.sizePolicy().hasHeightForWidth())
        self.pushButton_timeSignature_2_4.setSizePolicy(sizePolicy1)
        self.pushButton_timeSignature_2_4.setMinimumSize(QSize(42, 32))
        self.pushButton_timeSignature_2_4.setMaximumSize(QSize(60, 48))
        font1 = QFont()
        font1.setPointSize(9)
        self.pushButton_timeSignature_2_4.setFont(font1)
        self.pushButton_timeSignature_2_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self._2.addWidget(self.pushButton_timeSignature_2_4)

        self.horizontalSpacer_1 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self._2.addItem(self.horizontalSpacer_1)

        self.pushButton_timeSignature_3_4 = QPushButton(self.groupBox_timeSignaturePresets)
        self.pushButton_timeSignature_3_4.setObjectName(u"pushButton_timeSignature_3_4")
        sizePolicy1.setHeightForWidth(self.pushButton_timeSignature_3_4.sizePolicy().hasHeightForWidth())
        self.pushButton_timeSignature_3_4.setSizePolicy(sizePolicy1)
        self.pushButton_timeSignature_3_4.setMinimumSize(QSize(42, 32))
        self.pushButton_timeSignature_3_4.setMaximumSize(QSize(60, 48))
        self.pushButton_timeSignature_3_4.setFont(font1)
        self.pushButton_timeSignature_3_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self._2.addWidget(self.pushButton_timeSignature_3_4)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self._2.addItem(self.horizontalSpacer_2)

        self.pushButton_timeSignature_4_4 = QPushButton(self.groupBox_timeSignaturePresets)
        self.pushButton_timeSignature_4_4.setObjectName(u"pushButton_timeSignature_4_4")
        sizePolicy1.setHeightForWidth(self.pushButton_timeSignature_4_4.sizePolicy().hasHeightForWidth())
        self.pushButton_timeSignature_4_4.setSizePolicy(sizePolicy1)
        self.pushButton_timeSignature_4_4.setMinimumSize(QSize(42, 32))
        self.pushButton_timeSignature_4_4.setMaximumSize(QSize(60, 48))
        self.pushButton_timeSignature_4_4.setFont(font1)
        self.pushButton_timeSignature_4_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self._2.addWidget(self.pushButton_timeSignature_4_4)

        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self._2.addItem(self.horizontalSpacer_3)

        self.pushButton_timeSignature_6_8 = QPushButton(self.groupBox_timeSignaturePresets)
        self.pushButton_timeSignature_6_8.setObjectName(u"pushButton_timeSignature_6_8")
        sizePolicy1.setHeightForWidth(self.pushButton_timeSignature_6_8.sizePolicy().hasHeightForWidth())
        self.pushButton_timeSignature_6_8.setSizePolicy(sizePolicy1)
        self.pushButton_timeSignature_6_8.setMinimumSize(QSize(42, 32))
        self.pushButton_timeSignature_6_8.setMaximumSize(QSize(60, 48))
        self.pushButton_timeSignature_6_8.setFont(font1)
        self.pushButton_timeSignature_6_8.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self._2.addWidget(self.pushButton_timeSignature_6_8)


        self.gridLayout.addWidget(self.groupBox_timeSignaturePresets, 0, 2, 1, 1)

        self.verticalLayout_volumeSlider = QVBoxLayout()
        self.verticalLayout_volumeSlider.setObjectName(u"verticalLayout_volumeSlider")
        self.slider_volume = QSlider(self.centralwidget)
        self.slider_volume.setObjectName(u"slider_volume")
        self.slider_volume.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.slider_volume.setMaximum(125)
        self.slider_volume.setSliderPosition(80)
        self.slider_volume.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_volumeSlider.addWidget(self.slider_volume)

        self.pushButton_volumeSymbol = QPushButton(self.centralwidget)
        self.pushButton_volumeSymbol.setObjectName(u"pushButton_volumeSymbol")
        self.pushButton_volumeSymbol.setMaximumSize(QSize(16, 16))
        self.pushButton_volumeSymbol.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/images/images/volume-symbol.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_volumeSymbol.setIcon(icon2)
        self.pushButton_volumeSymbol.setFlat(True)

        self.verticalLayout_volumeSlider.addWidget(self.pushButton_volumeSymbol)


        self.gridLayout.addLayout(self.verticalLayout_volumeSlider, 0, 4, 3, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.groupBox_Tempo = QGroupBox(self.centralwidget)
        self.groupBox_Tempo.setObjectName(u"groupBox_Tempo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_Tempo.sizePolicy().hasHeightForWidth())
        self.groupBox_Tempo.setSizePolicy(sizePolicy2)
        self.groupBox_Tempo.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_Tempo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(13, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.spinBox_timeSignatureNumerator = QSpinBox(self.groupBox_Tempo)
        self.spinBox_timeSignatureNumerator.setObjectName(u"spinBox_timeSignatureNumerator")
        sizePolicy1.setHeightForWidth(self.spinBox_timeSignatureNumerator.sizePolicy().hasHeightForWidth())
        self.spinBox_timeSignatureNumerator.setSizePolicy(sizePolicy1)
        self.spinBox_timeSignatureNumerator.setMaximumSize(QSize(48, 48))
        font2 = QFont()
        font2.setPointSize(20)
        self.spinBox_timeSignatureNumerator.setFont(font2)
        self.spinBox_timeSignatureNumerator.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.spinBox_timeSignatureNumerator.setFrame(False)
        self.spinBox_timeSignatureNumerator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBox_timeSignatureNumerator.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_timeSignatureNumerator.setAccelerated(True)
        self.spinBox_timeSignatureNumerator.setMinimum(1)
        self.spinBox_timeSignatureNumerator.setMaximum(999)
        self.spinBox_timeSignatureNumerator.setValue(4)

        self.verticalLayout_5.addWidget(self.spinBox_timeSignatureNumerator)

        self.line = QFrame(self.groupBox_Tempo)
        self.line.setObjectName(u"line")
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMaximumSize(QSize(48, 20))
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_5.addWidget(self.line)

        self.spinBox_timeSignatureDenominator = QSpinBox(self.groupBox_Tempo)
        self.spinBox_timeSignatureDenominator.setObjectName(u"spinBox_timeSignatureDenominator")
        sizePolicy1.setHeightForWidth(self.spinBox_timeSignatureDenominator.sizePolicy().hasHeightForWidth())
        self.spinBox_timeSignatureDenominator.setSizePolicy(sizePolicy1)
        self.spinBox_timeSignatureDenominator.setMinimumSize(QSize(0, 0))
        self.spinBox_timeSignatureDenominator.setMaximumSize(QSize(48, 48))
        self.spinBox_timeSignatureDenominator.setFont(font2)
        self.spinBox_timeSignatureDenominator.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.spinBox_timeSignatureDenominator.setFrame(False)
        self.spinBox_timeSignatureDenominator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBox_timeSignatureDenominator.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_timeSignatureDenominator.setAccelerated(True)
        self.spinBox_timeSignatureDenominator.setMinimum(1)
        self.spinBox_timeSignatureDenominator.setMaximum(999)
        self.spinBox_timeSignatureDenominator.setValue(4)

        self.verticalLayout_5.addWidget(self.spinBox_timeSignatureDenominator)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_4 = QSpacerItem(25, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.spinBox_tempo = QSpinBox(self.groupBox_Tempo)
        self.spinBox_tempo.setObjectName(u"spinBox_tempo")
        sizePolicy1.setHeightForWidth(self.spinBox_tempo.sizePolicy().hasHeightForWidth())
        self.spinBox_tempo.setSizePolicy(sizePolicy1)
        self.spinBox_tempo.setMinimumSize(QSize(100, 0))
        font3 = QFont()
        font3.setPointSize(40)
        self.spinBox_tempo.setFont(font3)
        self.spinBox_tempo.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.spinBox_tempo.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.spinBox_tempo.setFrame(False)
        self.spinBox_tempo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBox_tempo.setReadOnly(True)
        self.spinBox_tempo.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_tempo.setAccelerated(True)
        self.spinBox_tempo.setMinimum(20)
        self.spinBox_tempo.setMaximum(260)
        self.spinBox_tempo.setValue(100)

        self.horizontalLayout_3.addWidget(self.spinBox_tempo)

        self.horizontalSpacer_7 = QSpacerItem(6, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.verticalLayout_IncreaseDecreaseButtons = QVBoxLayout()
        self.verticalLayout_IncreaseDecreaseButtons.setSpacing(0)
        self.verticalLayout_IncreaseDecreaseButtons.setObjectName(u"verticalLayout_IncreaseDecreaseButtons")
        self.pushButton_increaseTempo = QPushButton(self.groupBox_Tempo)
        self.pushButton_increaseTempo.setObjectName(u"pushButton_increaseTempo")
        sizePolicy1.setHeightForWidth(self.pushButton_increaseTempo.sizePolicy().hasHeightForWidth())
        self.pushButton_increaseTempo.setSizePolicy(sizePolicy1)
        self.pushButton_increaseTempo.setMinimumSize(QSize(28, 28))
        self.pushButton_increaseTempo.setMaximumSize(QSize(32, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setKerning(False)
        self.pushButton_increaseTempo.setFont(font4)
        self.pushButton_increaseTempo.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.verticalLayout_IncreaseDecreaseButtons.addWidget(self.pushButton_increaseTempo)

        self.verticalSpacer_5 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_IncreaseDecreaseButtons.addItem(self.verticalSpacer_5)

        self.pushButton_decreaseTempo = QPushButton(self.groupBox_Tempo)
        self.pushButton_decreaseTempo.setObjectName(u"pushButton_decreaseTempo")
        sizePolicy1.setHeightForWidth(self.pushButton_decreaseTempo.sizePolicy().hasHeightForWidth())
        self.pushButton_decreaseTempo.setSizePolicy(sizePolicy1)
        self.pushButton_decreaseTempo.setMinimumSize(QSize(28, 28))
        self.pushButton_decreaseTempo.setMaximumSize(QSize(32, 16777215))
        self.pushButton_decreaseTempo.setFont(font4)
        self.pushButton_decreaseTempo.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.verticalLayout_IncreaseDecreaseButtons.addWidget(self.pushButton_decreaseTempo)


        self.horizontalLayout_3.addLayout(self.verticalLayout_IncreaseDecreaseButtons)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.slider_tempo = QSlider(self.groupBox_Tempo)
        self.slider_tempo.setObjectName(u"slider_tempo")
        self.slider_tempo.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.slider_tempo.setMinimum(20)
        self.slider_tempo.setMaximum(260)
        self.slider_tempo.setSliderPosition(100)
        self.slider_tempo.setOrientation(Qt.Orientation.Horizontal)
        self.slider_tempo.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_tempo.setTickInterval(60)

        self.verticalLayout_2.addWidget(self.slider_tempo)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_5 = QSpacerItem(13, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.gridLayout.addWidget(self.groupBox_Tempo, 1, 2, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(10, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_13, 1, 3, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(10, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_14, 1, 5, 1, 1)

        self.groupBox_playStopTap = QGroupBox(self.centralwidget)
        self.groupBox_playStopTap.setObjectName(u"groupBox_playStopTap")
        self.groupBox_playStopTap.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_playStopTap)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_playStop = QPushButton(self.groupBox_playStopTap)
        self.pushButton_playStop.setObjectName(u"pushButton_playStop")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_playStop.sizePolicy().hasHeightForWidth())
        self.pushButton_playStop.setSizePolicy(sizePolicy3)
        self.pushButton_playStop.setMinimumSize(QSize(0, 40))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI Symbol"])
        font5.setPointSize(12)
        font5.setBold(False)
        self.pushButton_playStop.setFont(font5)
        self.pushButton_playStop.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon3 = QIcon()
        icon3.addFile(u":/images/images/play-stop-symbol.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_playStop.setIcon(icon3)
        self.pushButton_playStop.setIconSize(QSize(80, 32))

        self.horizontalLayout_5.addWidget(self.pushButton_playStop)

        self.horizontalSpacer_10 = QSpacerItem(6, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.pushButton_tapTempo = QPushButton(self.groupBox_playStopTap)
        self.pushButton_tapTempo.setObjectName(u"pushButton_tapTempo")
        sizePolicy3.setHeightForWidth(self.pushButton_tapTempo.sizePolicy().hasHeightForWidth())
        self.pushButton_tapTempo.setSizePolicy(sizePolicy3)
        self.pushButton_tapTempo.setMinimumSize(QSize(0, 40))
        self.pushButton_tapTempo.setFont(font)
        self.pushButton_tapTempo.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_5.addWidget(self.pushButton_tapTempo)

        self.horizontalSpacer_9 = QSpacerItem(6, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.pushButton_downbeat = QPushButton(self.groupBox_playStopTap)
        self.pushButton_downbeat.setObjectName(u"pushButton_downbeat")
        sizePolicy3.setHeightForWidth(self.pushButton_downbeat.sizePolicy().hasHeightForWidth())
        self.pushButton_downbeat.setSizePolicy(sizePolicy3)
        self.pushButton_downbeat.setMinimumSize(QSize(0, 40))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.pushButton_downbeat.setFont(font6)
        self.pushButton_downbeat.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon4 = QIcon()
        icon4.addFile(u":/images/images/note-accent-symbol.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_downbeat.setIcon(icon4)
        self.pushButton_downbeat.setIconSize(QSize(80, 32))

        self.horizontalLayout_5.addWidget(self.pushButton_downbeat)

        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(3, 1)

        self.gridLayout.addWidget(self.groupBox_playStopTap, 2, 2, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 528, 33))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menu_Application = QMenu(self.menubar)
        self.menu_Application.setObjectName(u"menu_Application")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_Application.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.action_About)
        self.menu_Application.addAction(self.action_Quit)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.action_Preferences)
        self.menuSettings.addAction(self.action_ToggleViewMode)

        self.retranslateUi(MainWindow)
        self.spinBox_tempo.valueChanged.connect(self.slider_tempo.setValue)
        self.slider_tempo.valueChanged.connect(self.spinBox_tempo.setValue)
        self.pushButton_increaseTempo.clicked.connect(self.spinBox_tempo.stepUp)
        self.action_Quit.triggered.connect(MainWindow.showMinimized)
        self.pushButton_decreaseTempo.clicked.connect(self.spinBox_tempo.stepDown)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Metronome", None))
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"&About", None))
#if QT_CONFIG(shortcut)
        self.action_About.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.action_Quit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
#if QT_CONFIG(shortcut)
        self.action_Quit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_Preferences.setText(QCoreApplication.translate("MainWindow", u"&Preferences", None))
#if QT_CONFIG(shortcut)
        self.action_Preferences.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.action_ToggleViewMode.setText(QCoreApplication.translate("MainWindow", u"Compact Mode", None))
        self.action_OpenDownbeatSoundFile.setText(QCoreApplication.translate("MainWindow", u"Open Downbeat Sound File", None))
#if QT_CONFIG(shortcut)
        self.action_OpenDownbeatSoundFile.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.action_OpenBackbeatSoundFile.setText(QCoreApplication.translate("MainWindow", u"Open Backbeat Sound File", None))
#if QT_CONFIG(shortcut)
        self.action_OpenBackbeatSoundFile.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButton_selectDownbeatSound.setToolTip(QCoreApplication.translate("MainWindow", u"Select the sound for the downbeat.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_selectDownbeatSound.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_selectRegularBeatsSound.setToolTip(QCoreApplication.translate("MainWindow", u"Select the sound for regular beats.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_selectRegularBeatsSound.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_preset1.setToolTip(QCoreApplication.translate("MainWindow", u"Hold Long to Overwrite", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_preset1.setText(QCoreApplication.translate("MainWindow", u"Preset 1", None))
#if QT_CONFIG(tooltip)
        self.pushButton_preset2.setToolTip(QCoreApplication.translate("MainWindow", u"Hold Long to Overwrite", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_preset2.setText(QCoreApplication.translate("MainWindow", u"Preset 2", None))
#if QT_CONFIG(tooltip)
        self.pushButton_preset3.setToolTip(QCoreApplication.translate("MainWindow", u"Hold Long to Overwrite", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_preset3.setText(QCoreApplication.translate("MainWindow", u"Preset 3", None))
#if QT_CONFIG(tooltip)
        self.pushButton_preset4.setToolTip(QCoreApplication.translate("MainWindow", u"Hold Long to Overwrite", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_preset4.setText(QCoreApplication.translate("MainWindow", u"Preset 4", None))
#if QT_CONFIG(tooltip)
        self.pushButton_preset5.setToolTip(QCoreApplication.translate("MainWindow", u"Hold Long to Overwrite", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_preset5.setText(QCoreApplication.translate("MainWindow", u"Preset 5", None))
#if QT_CONFIG(tooltip)
        self.pushButton_timeSignature_2_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_timeSignature_2_4.setText(QCoreApplication.translate("MainWindow", u"2/4", None))
#if QT_CONFIG(tooltip)
        self.pushButton_timeSignature_3_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_timeSignature_3_4.setText(QCoreApplication.translate("MainWindow", u"3/4", None))
#if QT_CONFIG(tooltip)
        self.pushButton_timeSignature_4_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_timeSignature_4_4.setText(QCoreApplication.translate("MainWindow", u"4/4", None))
#if QT_CONFIG(tooltip)
        self.pushButton_timeSignature_6_8.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_timeSignature_6_8.setText(QCoreApplication.translate("MainWindow", u"6/8", None))
#if QT_CONFIG(tooltip)
        self.slider_volume.setToolTip(QCoreApplication.translate("MainWindow", u"Volume", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_Tempo.setTitle("")
        self.pushButton_increaseTempo.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_decreaseTempo.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(tooltip)
        self.slider_tempo.setToolTip(QCoreApplication.translate("MainWindow", u"Tempo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_playStop.setToolTip(QCoreApplication.translate("MainWindow", u"Start/Stop", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_tapTempo.setToolTip(QCoreApplication.translate("MainWindow", u"Tap to set tempo", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_tapTempo.setText(QCoreApplication.translate("MainWindow", u"TAP", None))
#if QT_CONFIG(tooltip)
        self.pushButton_downbeat.setToolTip(QCoreApplication.translate("MainWindow", u"Enable/Disable Downbeat", None))
#endif // QT_CONFIG(tooltip)
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.menu_Application.setTitle(QCoreApplication.translate("MainWindow", u"&Application", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

