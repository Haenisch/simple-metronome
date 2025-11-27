"""A simple PySide6-based metronome application."""

import os
import sys

from PySide6.QtWidgets import QApplication  # pylint: disable=no-name-in-module
from PySide6.QtGui import QIcon  # pylint: disable=no-name-in-module
from main_window import MainWindow  # pylint: disable=import-error

def main():
    """Main function."""
    os.environ["QT_SCALE_FACTOR"] = "1.25"
    app = QApplication(sys.argv)
    with open("style.qss", "r", encoding="utf-8") as file:
        app.setStyleSheet(file.read())
    window = MainWindow()
    icon = QIcon("images/metronome-icon.png")  # Use your icon file path here
    window.setWindowIcon(icon)
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
