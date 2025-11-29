"""A simple PySide6-based metronome application."""

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
