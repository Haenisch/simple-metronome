# Copyright (c) 2025 Christoph Hänisch.
# This file is part of the "Metronome" application.
# It is licensed under the GNU General Public License v3.0 or higher.
# See the LICENSE file for more details.

"""A simple metronome application."""

# Note, the application is based on files created with the Qt Designer. These
# files have to be compiled to Python using pyside6-uic and pyside6-rcc,
# respectively. The generated Python files are then imported here.
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

import os
import sys

from PySide6.QtWidgets import QApplication  # pylint: disable=no-name-in-module
from PySide6.QtGui import QIcon  # pylint: disable=no-name-in-module
from main_window import MainWindow  # pylint: disable=import-error

def main():
    """Main function."""
    os.environ["QT_SCALE_FACTOR"] = "1.25"

    # Change current working directory to application directory
    application_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(application_directory)

    # Create the application and set the style
    app = QApplication(sys.argv)
    app.setStyle("Windows11")
    with open("style.qss", "r", encoding="utf-8") as file:
        app.setStyleSheet(file.read())

    # Create and show the main window
    window = MainWindow()
    icon = QIcon("images/metronome-icon.png")
    window.setWindowIcon(icon)
    window.show()

    # Execute the application
    app.exec()


if __name__ == '__main__':
    main()
