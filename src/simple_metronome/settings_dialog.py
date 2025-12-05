# Copyright (c) 2025 Christoph Hänisch.
# This file is part of the "Metronome" application.
# It is licensed under the GNU General Public License v3.0 or higher.
# See the LICENSE file for more details.

"""Settings dialog of the main window."""

# pylint: disable=line-too-long
# pylint: disable=no-name-in-module
# pylint: disable=invalid-name

# Note, the settings dialog is based on the Qt Designer file
# 'settings_dialog.ui' from which the file 'ui_settings_dialog.py' is generated
# using either of the commands:
#   pyside6-uic .\settings_dialog.ui -o ui_settings_dialog.py
#   poetry run pyside6-uic .\settings_dialog.ui -o ui_settings_dialog.py

from PySide6.QtWidgets import QDialog, QMainWindow, QWidget
from PySide6.QtCore import Signal
from . ui_settings_dialog import Ui_Settings


##################################################################################################
# SettingsDialog
##################################################################################################

class SettingsDialog(QDialog, Ui_Settings):
    """Settings dialog for the GUI."""

    settingsChanged = Signal()


    def __init__(self, parent: QWidget | QMainWindow = None):
        """Initialize the settings dialog."""
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setWindowTitle("Settings")

        self.backbeat_volume = 80  # default value
        self.downbeat_volume = 100  # default value

        self.spinBox_backbeatVolume.valueChanged.connect(self.on_spinBox_backbeatVolume_valueChanged)
        self.spinBox_downbeatVolume.valueChanged.connect(self.on_spinBox_downbeatVolume_valueChanged)


    def on_spinBox_backbeatVolume_valueChanged(self, value: int):
        """Handle changes of the backbeat volume spin box."""
        self.backbeat_volume = value
        self.settingsChanged.emit()


    def on_spinBox_downbeatVolume_valueChanged(self, value: int):
        """Handle changes of the downbeat volume spin box."""
        self.downbeat_volume = value
        self.settingsChanged.emit()
