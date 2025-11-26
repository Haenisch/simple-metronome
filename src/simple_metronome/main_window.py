# Copyright (c) 2025 Christoph Hänisch.
# This file is part of the "Metronome" application.
# It is licensed under the GNU General Public License v3.0 or higher.
# See the LICENSE file for more details.

"""Main Window of the GUI."""

# pylint: disable=import-error
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=no-member
# pylint: disable=no-name-in-module
# pylint: disable=wrong-import-position

# Note, the main window is based on the Qt Designer file 'main_window.ui' from
# which the file 'ui_main_window.py' is generated using either of the commands:
#   pyside6-uic .\main_window.ui -o ui_main_window.py
#   poetry run pyside6-uic .\main_window.ui -o ui_main_window.py

import time

from PySide6.QtCore import Qt, QTimer, QUrl
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtWidgets import QMainWindow, QMessageBox
import toml

import default_config
from settings_dialog import SettingsDialog
from ui_main_window import Ui_MainWindow
from version import VERSION


##################################################################################################
# Helper Functions
##################################################################################################

def static_variables(**kwargs):
    """Decorator to add one or more static variables to a function.
    
    Example usage:

    ```python
    @static_variables(counter=0)
    def my_function():
        my_function.counter += 1
        print(my_function.counter)
    ```
    """
    def decorate(func):
        for key, value in kwargs.items():
            setattr(func, key, value)
        return func
    return decorate


##################################################################################################
# Main Window
##################################################################################################

class MainWindow(QMainWindow, Ui_MainWindow):
    """Main window of the metronome application.
    
    Since this application is simple enough, the main window also contains the main logic.
    """

    def __init__(self):
        """Initialize the main widget."""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Simple Metronome")
        self.menubar.hide()
        self.init_geometry()

        self.timer = QTimer()
        self.timer.setTimerType(Qt.PreciseTimer)  # type: ignore
        self.timer.timeout.connect(self.play_sound_callback)
        self.player_downbeat = QSoundEffect()
        self.player_downbeat.setLoopCount(1)
        self.player_backbeat = QSoundEffect()
        self.player_backbeat.setLoopCount(1)
        self.playing = False
        self.current_beat = 0
        self.next_beat_system_time_ns = 0  # system time for the next beat in nanoseconds

        # Load the configuration.
        self.config = {}
        self.load_config()

        # Initialize settings from the configuration.
        self.downbeat_accent = self.config["general_settings"]["downbeat_accent"]
        self.time_signature_numerator = int(self.config["general_settings"]["time_signature_numerator"])
        self.time_signature_denominator = int(self.config["general_settings"]["time_signature_denominator"])
        self.set_time_signature(self.time_signature_numerator, self.time_signature_denominator)
        self.tempo = int(self.config["general_settings"]["tempo"])
        self.slider_tempo.setValue(self.tempo)
        self.config["general_settings"]["tempo"] = self.tempo
        self.volume = int(self.config["general_settings"]["volume"])
        self.set_volume(self.volume)

        self.downbeat_volume = self.config["general_settings"]["downbeat_volume"]
        self.backbeat_volume = self.config["general_settings"]["backbeat_volume"]
        self.player_downbeat.setSource(QUrl.fromLocalFile(self.config["preset1"]["downbeat_sound_file"]))
        self.player_backbeat.setSource(QUrl.fromLocalFile(self.config["preset1"]["backbeat_sound_file"]))
        self.preset_downbeat_volume = self.config["preset1"]["downbeat_volume"]  # allows for correcting volume levels per preset
        self.preset_backbeat_volume = self.config["preset1"]["backbeat_volume"]  # allows for correcting volume levels per preset

        # Connect the GUI elements.
        self.pushButton_downbeatAccent.clicked.connect(self.toggle_downbeat_accent)
        self.pushButton_playStop.clicked.connect(self.on_play_stop_clicked)
        self.pushButton_preset1.clicked.connect(self.on_preset1_clicked)
        self.pushButton_preset2.clicked.connect(self.on_preset2_clicked)
        self.pushButton_preset3.clicked.connect(self.on_preset3_clicked)
        self.pushButton_preset4.clicked.connect(self.on_preset4_clicked)
        self.pushButton_preset5.clicked.connect(self.on_preset5_clicked)
        self.pushButton_tapTempo.clicked.connect(self.on_tap_tempo_clicked)
        self.pushButton_timeSignature_2_4.clicked.connect(self.on_time_signature_2_4_clicked)
        self.pushButton_timeSignature_3_4.clicked.connect(self.on_time_signature_3_4_clicked)
        self.pushButton_timeSignature_4_4.clicked.connect(self.on_time_signature_4_4_clicked)
        self.pushButton_timeSignature_6_8.clicked.connect(self.on_time_signature_6_8_clicked)
        self.slider_volume.valueChanged.connect(self.on_volume_changed)
        self.spinBox_tempo.valueChanged.connect(self.set_tempo)
        self.spinBox_timeSignatureDenominator.valueChanged.connect(self.on_time_signature_denominator_changed)
        self.spinBox_timeSignatureNumerator.valueChanged.connect(self.on_time_signature_numerator_changed)

        # Set up the menu bar.
        self.action_About.triggered.connect(lambda: QMessageBox.information(self, "About", f"A Simple Metronome\nVersion {VERSION}\n(c) 2025 Christoph Hänisch"))
        self.action_Preferences.triggered.connect(self.show_settings_dialog)
        self.action_Quit.triggered.connect(self.close)

        # Add global shortcuts.
        self.shortcut_about = QShortcut(QKeySequence("F1"), self)
        self.shortcut_about.activated.connect(lambda: QMessageBox.information(self, "About", f"A Simple Metronome\nVersion {VERSION}\n(c) 2025 Christoph Hänisch"))
        self.shortcut_preferences = QShortcut(QKeySequence("Ctrl+P"), self)
        self.shortcut_preferences.activated.connect(self.show_settings_dialog)
        self.shortcut_quit = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut_quit.activated.connect(self.close)

        self.shortcut_start_stop = QShortcut(QKeySequence("Space"), self)
        self.shortcut_start_stop.activated.connect(self.on_play_stop_clicked)
        self.shortcut_toggle_downbeat_accent = QShortcut(QKeySequence("<"), self)
        self.shortcut_toggle_downbeat_accent.activated.connect(self.toggle_downbeat_accent)
        self.shortcut_toggle_downbeat_accent = QShortcut(QKeySequence("a"), self)
        self.shortcut_toggle_downbeat_accent.activated.connect(self.toggle_downbeat_accent)

        self.shortcut_decrease_tempo = QShortcut(QKeySequence("-"), self)
        self.shortcut_decrease_tempo.activated.connect(self.pushButton_decreaseTempo.click)
        self.shortcut_increase_tempo = QShortcut(QKeySequence("+"), self)
        self.shortcut_increase_tempo.activated.connect(self.pushButton_increaseTempo.click)
        self.shortcut_fast_decrease_tempo = QShortcut(QKeySequence("PgDown"), self)
        self.shortcut_fast_decrease_tempo.activated.connect(lambda: self.set_tempo(max(20, self.tempo - 10)))
        self.shortcut_fast_increase_tempo = QShortcut(QKeySequence("PgUp"), self)
        self.shortcut_fast_increase_tempo.activated.connect(lambda: self.set_tempo(min(260, self.tempo + 10)))

        self.shortcut_load_preset_1 = QShortcut(QKeySequence("1"), self)
        self.shortcut_load_preset_1.activated.connect(lambda:self.load_preset(1))
        self.shortcut_load_preset_1 = QShortcut(QKeySequence("2"), self)
        self.shortcut_load_preset_1.activated.connect(lambda:self.load_preset(2))
        self.shortcut_load_preset_1 = QShortcut(QKeySequence("3"), self)
        self.shortcut_load_preset_1.activated.connect(lambda:self.load_preset(3))
        self.shortcut_load_preset_1 = QShortcut(QKeySequence("4"), self)
        self.shortcut_load_preset_1.activated.connect(lambda:self.load_preset(4))
        self.shortcut_load_preset_1 = QShortcut(QKeySequence("5"), self)
        self.shortcut_load_preset_1.activated.connect(lambda:self.load_preset(5))

        # Set up the preferences dialog.
        self.setup_dialogs()


    def closeEvent(self, event):
        """Handle the close event of the main window."""
        self.save_config()
        event.accept()


    def init_geometry(self):
        """Initialize the geometry of the main window."""
        screen_geometry = self.screen().geometry()
        width, height = 470, 268
        x = (screen_geometry.width() - width) // 2
        y = (screen_geometry.height() - height) // 2
        self.setGeometry(x, y, width, height)


    def keyPressEvent(self, event):  # pylint: disable=invalid-name
        """Handle key press events. In particular, show the menu bar when the Alt key is pressed."""
        if event.key() == Qt.Key_Alt:  # type: ignore
            self.menubar.show()


    def keyReleaseEvent(self, event):  # pylint: disable=invalid-name
        """Handle key release events. In particular, hide the menu bar when the Alt key is released."""
        if event.key() == Qt.Key_Alt:  # type: ignore
            self.menubar.hide()


    def load_config(self):
        """Load the configuration from a TOML file."""
        try:
            self.config = toml.load("./config.toml")
        except FileNotFoundError:
            QMessageBox.warning(self, "Warning", "Configuration file './config.toml' not found. Using default settings.")
            self.config = default_config.config
        except toml.TomlDecodeError as e:
            QMessageBox.critical(self, "Error", f"Failed to parse configuration file './config.toml': {e}")

        # Check if all required tables along with key-value pairs are present; if not, use defaults.
        anything_missing = False
        for section, settings in default_config.config.items():
            if section not in self.config:
                self.config[section] = settings
                anything_missing = True
            else:
                for key, value in settings.items():
                    if key not in self.config[section]:
                        self.config[section][key] = value
                        anything_missing = True
        if anything_missing:
            QMessageBox.information(self, "Info", "Some configuration settings were missing in './config.toml'. Default values have been applied.")

        sound_file_downbeat = self.config['preset1']['downbeat_sound_file']
        sound_file_backbeat = self.config['preset1']['backbeat_sound_file']
        self.player_downbeat.setSource(QUrl.fromLocalFile(sound_file_downbeat))
        self.player_backbeat.setSource(QUrl.fromLocalFile(sound_file_backbeat))


    def load_preset(self, preset_number: int):
        """Load a preset configuration."""
        preset_key = f"preset{preset_number}"
        if preset_key not in self.config:
            QMessageBox.critical(self, "Error", f"Preset '{preset_key}' not found in configuration.")
            return

        preset = self.config[preset_key]
        sound_file_downbeat = preset["downbeat_sound_file"]
        sound_file_backbeat = preset["backbeat_sound_file"]
        self.player_downbeat.setSource(QUrl.fromLocalFile(sound_file_downbeat))
        self.player_backbeat.setSource(QUrl.fromLocalFile(sound_file_backbeat))
        self.preset_downbeat_volume = preset["downbeat_volume"]  # allows for correcting volume levels per preset
        self.preset_backbeat_volume = preset["backbeat_volume"]  # allows for correcting volume levels per preset
        self.downbeat_accent = preset["downbeat_accent"]
        numerator = int(preset["time_signature_numerator"])
        denominator = int(preset["time_signature_denominator"])
        self.set_time_signature(numerator, denominator)
        self.set_tempo(int(preset["tempo"]))
        self.set_volume(int(preset["volume"]))


    def on_play_stop_clicked(self):
        """Play or stop the metronome."""
        if not self.playing:
            # Start playing the metronome immediately.
            self.playing = True
            self.current_beat = 0  # reset beat counter
            self.play_beat_sound()
            # Calculate the system time for the next beat and setup a single-shot
            # timer for calling the callback function. Note, in each callback, we
            # will restart the timer as long as the metronome is playing.
            duration_between_beats_ns = 60_000_000_000 // self.tempo
            self.next_beat_system_time_ns = time.time() * 1_000_000_000 + duration_between_beats_ns
            QTimer.singleShot(duration_between_beats_ns//1_000_000, self.play_sound_callback)
            # TODO: visual beat indication
        else:
            self.playing = False
            self.timer.stop()


    def on_preset1_clicked(self):
        """Load the preset 1 configuration."""
        self.load_preset(1)

    def on_preset2_clicked(self):
        """Load the preset 2 configuration."""
        self.load_preset(2)


    def on_preset3_clicked(self):
        """Load the preset 3 configuration."""
        self.load_preset(3)


    def on_preset4_clicked(self):
        """Load the preset 4 configuration."""
        self.load_preset(4)


    def on_preset5_clicked(self):
        """Load the preset 5 configuration."""
        self.load_preset(5)


    def on_tap_tempo_clicked(self):
        """Handle clicks on the 'Tap Tempo' button."""
        pass


    def on_time_signature_2_4_clicked(self):
        """Handle clicks on the '2/4' time signature button."""
        self.set_time_signature(2, 4)


    def on_time_signature_3_4_clicked(self):
        """Handle clicks on the '3/4' time signature button."""
        self.set_time_signature(3, 4)


    def on_time_signature_4_4_clicked(self):
        """Handle clicks on the '4/4' time signature button."""
        self.set_time_signature(4, 4)


    def on_time_signature_6_8_clicked(self):
        """Handle clicks on the '6/8' time signature button."""
        self.set_time_signature(6, 8)


    def on_time_signature_numerator_changed(self, value: int):
        """Handle changes of the time signature numerator spin box."""
        self.set_time_signature(value, self.time_signature_denominator)


    def on_time_signature_denominator_changed(self, value: int):
        """Handle changes of the time signature denominator spin box."""
        self.set_time_signature(self.time_signature_numerator, value)


    def on_volume_changed(self, value: int):
        """Handle changes of the volume slider."""
        self.set_volume(value)


    def play_beat_sound(self):
        """Play the metronome clicking sound."""
        # With each call, play either the downbeat or backbeat sound depending on
        # the current beat counter. After that, increase the counter accordingly.
        # Also, take the volume settings into account.
        print(f"Playing beat {self.current_beat+1} of {self.time_signature_numerator}")
        if self.current_beat == 0 and self.downbeat_accent:  # downbeat
            volume = self.downbeat_volume / 100 * self.preset_downbeat_volume / 100 * self.volume / 100
            self.player_downbeat.setVolume(volume)
            self.player_downbeat.play()
        else:  # backbeat
            volume = self.backbeat_volume / 100 * self.preset_backbeat_volume / 100 * self.volume / 100
            self.player_backbeat.setVolume(volume)
            self.player_backbeat.play()
        self.current_beat = (self.current_beat + 1) % self.time_signature_numerator


    def play_sound_callback(self):
        """Play the metronome clicking sound."""
        # This function is called by a single-shot timer at each beat. The timer
        # interval is set according to the tempo. To account for inaccuracies in
        # the timer, scheduling etc., we use the system clock to determine the
        # exact timing of each beat (thus errors do not accumulate).

        if not self.playing:
            return

        self.play_beat_sound()

        # Schedule the next call of this function according to the system time.
        duration_between_beats_ns = 60_000_000_000 // self.tempo
        self.next_beat_system_time_ns += duration_between_beats_ns
        time_left_to_next_beat_ns = self.next_beat_system_time_ns - time.time() * 1_000_000_000
        if time_left_to_next_beat_ns > 0:
            QTimer.singleShot(time_left_to_next_beat_ns // 1_000_000, self.play_sound_callback)  # type: ignore
        else:
            # If we are already late, schedule the next beat immediately.
            QTimer.singleShot(0, self.play_sound_callback)


    def save_config(self):
        """Save the configuration to a TOML file."""
        try:
            with open("./config.toml", "w", encoding="utf-8") as file:
                toml.dump(self.config, file)
        except Exception as e:  # pylint: disable=broad-except
            QMessageBox.critical(self, "Error", f"Failed to save configuration to './config.toml': {e}")


    def set_time_signature(self, numerator: int, denominator: int):
        """Set the time signature."""
        self.time_signature_numerator = numerator
        self.time_signature_denominator = denominator
        self.spinBox_timeSignatureNumerator.setValue(numerator)
        self.spinBox_timeSignatureDenominator.setValue(denominator)
        self.config["general_settings"]["time_signature_numerator"] = numerator
        self.config["general_settings"]["time_signature_denominator"] = denominator


    def set_tempo(self, tempo: int):
        """Set the tempo."""
        self.tempo = tempo
        self.slider_tempo.setValue(tempo)
        self.config["general_settings"]["tempo"] = tempo


    def set_volume(self, volume: int):
        """Set the volume."""
        self.volume = volume
        self.slider_volume.setValue(volume)
        self.config["general_settings"]["volume"] = volume


    def show_settings_dialog(self):
        """Show the settings dialog."""
        self.settings_dialog.show()
        self.settings_dialog.raise_()


    def setup_dialogs(self):
        """Setup the settings dialog."""
        self.settings_dialog = SettingsDialog(parent=self)
        self.settings_dialog.hide()


    def toggle_downbeat_accent(self):
        """Toggle the downbeat accent setting."""
        self.downbeat_accent = not self.downbeat_accent
        self.config["general_settings"]["downbeat_accent"] = self.downbeat_accent
