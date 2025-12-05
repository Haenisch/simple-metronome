# Copyright (c) 2025 Christoph Hänisch.
# This file is part of the "Metronome" application.
# It is licensed under the GNU General Public License v3.0 or higher.
# See the LICENSE file for more details.

"""A simple metronome application."""

# Note, the application is based on files created with the Qt Designer. These
# files have to be compiled to Python using pyside6-uic and pyside6-rcc,
# respectively. The generated Python files are then imported here or in other
# modules of the application.
#
# These files are:
#
#     main_window.ui      →  ui_main_window.py
#     settings_dialog.ui  →  ui_settings_dialog.py
#     resource_files.qrc  →  resource_files_rc.py
#
# The commands to do this are:
#
#     pyside6-uic main_window.ui -o ui_main_window.py
#     pyside6-uic settings_dialog.ui -o ui_settings_dialog.py
#     pyside6-rcc resource_files.qrc -o resource_files_rc.py
#
# If you are using Poetry, you can run these commands as follows:
#
#     poetry run pyside6-uic main_window.ui -o ui_main_window.py
#     poetry run pyside6-uic settings_dialog.qrc -o ui_settings_dialog.py
#     poetry run pyside6-rcc resource_files.qrc -o resource_files_rc.py

# pylint: disable=line-too-long
# pylint: disable=import-error

import os
import sys

from PySide6.QtWidgets import QApplication, QMessageBox  # pylint: disable=no-name-in-module
from PySide6.QtGui import QIcon  # pylint: disable=no-name-in-module

from . configuration import load_config
from . main_window import MainWindow


def main():
    """Main function."""
    # Load the configuration
    package_dir = os.path.dirname(os.path.abspath(__file__))
    config, status = load_config(config_dir=package_dir)

    # Set the GUI scale factor from the configuration        
    scale_factor = config["general_settings"]["gui_scale_factor"]
    os.environ["QT_SCALE_FACTOR"] = str(scale_factor)

    # Create the application and set the style
    app = QApplication(sys.argv)
    app.setStyle("Windows11")
    with open(os.path.join(package_dir, "style.qss"), "r", encoding="utf-8") as file:
        app.setStyleSheet(file.read())

    # Show message boxes in case of configuration loading issues
    if status.code == status.FILE_NOT_FOUND:
        QMessageBox.information(None, "Configuration File Not Found", status.message)
    elif status.code == status.PARSE_ERROR:
        QMessageBox.information(None, "Configuration File Parse Error", status.message)
    elif status.code == status.MISSING_SETTINGS:
        QMessageBox.information(None, "Missing Configuration Settings", status.message)

    # Create and show the main window
    window = MainWindow(config)
    icon = QIcon(os.path.join(package_dir, "images/metronome-icon.png"))
    window.setWindowIcon(icon)
    window.show()

    # Execute the application
    app.exec()


if __name__ == '__main__':
    main()
