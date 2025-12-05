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

from enum import Enum
import os
import time

from PySide6.QtCore import QPoint, Qt, QTimer, QUrl
from PySide6.QtGui import QIcon, QKeySequence, QMouseEvent, QShortcut
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtWidgets import QFileDialog, QMainWindow, QMessageBox

from . configuration import save_config
from . settings_dialog import SettingsDialog
from . ui_main_window import Ui_MainWindow
from . version import VERSION


##################################################################################################
# Style Constants
##################################################################################################

ACTIVE_ELEMENT_BG_COLOR = "#0067C0"
ACTIVE_ELEMENT_PRESSED_BG_COLOR = "#004A8F"
INACTIVE_ELEMENT_BG_COLOR = "#505050"

PRESET_ACTIVE_BG_COLOR = "#44505a"
PRESET_HOVER_BG_COLOR = "#505050"
PRESET_INACTIVE_BG_COLOR = "#3b3b3b"
PRESET_PRESSED_BG_COLOR = "#2b2b2b"

PRESET_ACTIVE_STYLE = f"QPushButton {{background: {PRESET_ACTIVE_BG_COLOR};}}" + \
                        f"QPushButton:hover {{background: {PRESET_HOVER_BG_COLOR};}}" + \
                        f"QPushButton:pressed {{background: {PRESET_PRESSED_BG_COLOR};}}" + \
                        f"QPushButton:disabled {{background: {PRESET_INACTIVE_BG_COLOR};}}"

PRESET_INACTIVE_STYLE = f"QPushButton {{background: {PRESET_INACTIVE_BG_COLOR};}}" + \
                        f"QPushButton:hover {{background: {PRESET_HOVER_BG_COLOR};}}" + \
                        f"QPushButton:pressed {{background: {PRESET_PRESSED_BG_COLOR};}}" + \
                        f"QPushButton:disabled {{background: {PRESET_INACTIVE_BG_COLOR};}}"


##################################################################################################
# Helper Functions
##################################################################################################

def shifted_range(start, stop=None, step=1, offset=0):
    """Like range(), but with an offset applied to start and stop."""
    if stop is None:  # called like range(n)
        start, stop = 0, start
    return range(start + offset, stop + offset, step)


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

    MAX_TEMPO = 260
    MIN_TEMPO = 20
    MAX_VOLUME = 100
    MIN_VOLUME = 0
    MAX_TAP_TIMES = 5  # maximum number of tap times to consider for tempo calculation
    TAP_TIMEOUT_MS = 5000  # timeout in milliseconds to end tap tempo mode
    LONG_PRESS_DURATION_MS = 400  # duration in milliseconds to consider a button press as long press

    class TapState(Enum):
        """State of the tap tempo functionality."""
        WAITING_FOR_FIRST_TAP = 1  # store current time, change button color, ...
        COLLECTING_TAPS = 2        # collect tap times, calculate tempo, ...
        ENDING_TAP_SEQUENCE = 3    # timeout reached; change button color, reset state, ...


    def __init__(self, config: dict):
        """Initialize the main widget."""

        # Initialize the UI
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Simple Metronome")
        self.menubar.hide()
        self.init_geometry()

        # Private variables.
        self._drag_position = QPoint()  # for moving the window by dragging

        # Initialize variables for metronome state.
        self.player_downbeat = QSoundEffect()
        self.player_downbeat.setLoopCount(1)
        self.player_backbeat = QSoundEffect()
        self.player_backbeat.setLoopCount(1)
        self.playing = False
        self.current_beat = 0
        self.next_beat_system_time_ns = 0  # system time for the next beat in nanoseconds

        # Tap tempo state variables.
        self.tap_state = MainWindow.TapState.WAITING_FOR_FIRST_TAP
        self.tap_times_ns = []  # list of system times at taps in nanoseconds
        self.tap_timer = QTimer()
        self.tap_timer.setSingleShot(True)
        self.tap_timer.setTimerType(Qt.PreciseTimer)  # type: ignore
        self.tap_timer.timeout.connect(self.on_tap_tempo_timeout)

        # Preset related variables
        self.num_presets = 5
        self.active_preset_index = 1
        self.preset_pressed_times = [0] * self.num_presets
        self.active_preset_altered = False

        # View mode state variable.
        self.view_mode_expanded = True

        # Resources needed for the GUI (symbol of the downbeat accent on/off button).
        self.icon_note = QIcon(":images/images/note-symbol.svg")
        self.icon_note_accent = QIcon(":images/images/note-accent-symbol.svg")

        # Restore the program state from the configuration.
        self.config = config
        self.restore_program_state()
        self.init_with_config_values()  # TODO: merge with restore_program_state()

        # Connect the GUI elements.
        self.connect_signals()

        # Set up the menu bar.
        self.setup_menubar()

        # Add global shortcuts.
        self.add_shortcuts()

        # Set up the preferences dialog.
        self.setup_dialogs()


    def add_shortcuts(self):
        """Add global keyboard shortcuts."""
        self.shortcut_about = QShortcut(QKeySequence("F1"), self)
        self.shortcut_about.activated.connect(lambda: QMessageBox.information(self, "About", f"A Simple Metronome\nVersion {VERSION}\n(c) 2025 Christoph Hänisch"))
        self.shortcut_preferences = QShortcut(QKeySequence("Ctrl+P"), self)
        self.shortcut_preferences.activated.connect(self.show_settings_dialog)
        self.shortcut_quit = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut_quit.activated.connect(self.close)

        self.shortcut_start_stop = QShortcut(QKeySequence("Space"), self)
        self.shortcut_start_stop.activated.connect(self.pushButton_playStop.animateClick)
        self.shortcut_tap = QShortcut(QKeySequence("T"), self)
        self.shortcut_tap.activated.connect(self.pushButton_tapTempo.animateClick)
        self.shortcut_toggle_downbeat_accent = QShortcut(QKeySequence("<"), self)
        self.shortcut_toggle_downbeat_accent.activated.connect(self.pushButton_downbeatAccent.animateClick)
        self.alternative_shortcut_toggle_downbeat_accent = QShortcut(QKeySequence("a"), self)
        self.alternative_shortcut_toggle_downbeat_accent.activated.connect(self.pushButton_downbeatAccent.animateClick)

        self.shortcut_decrease_time_signature_denominator = QShortcut(QKeySequence("F9"), self)
        self.shortcut_decrease_time_signature_denominator.activated.connect(lambda: self.spinBox_timeSignatureDenominator.setValue(self.spinBox_timeSignatureDenominator.value() - 1))
        self.shortcut_increase_time_signature_denominator = QShortcut(QKeySequence("F10"), self)
        self.shortcut_increase_time_signature_denominator.activated.connect(lambda: self.spinBox_timeSignatureDenominator.setValue(self.spinBox_timeSignatureDenominator.value() + 1))
        self.shortcut_decrease_time_signature_numerator = QShortcut(QKeySequence("F11"), self)
        self.shortcut_decrease_time_signature_numerator.activated.connect(lambda: self.spinBox_timeSignatureNumerator.setValue(self.spinBox_timeSignatureNumerator.value() - 1))
        self.shortcut_increase_time_signature_numerator = QShortcut(QKeySequence("F12"), self)
        self.shortcut_increase_time_signature_numerator.activated.connect(lambda: self.spinBox_timeSignatureNumerator.setValue(self.spinBox_timeSignatureNumerator.value() + 1))

        self.alternative_shortcut_decrease_tempo = QShortcut(QKeySequence("Left"), self)
        self.alternative_shortcut_decrease_tempo.activated.connect(self.pushButton_decreaseTempo.click)
        self.alternative_shortcut_increase_tempo = QShortcut(QKeySequence("Right"), self)
        self.alternative_shortcut_increase_tempo.activated.connect(self.pushButton_increaseTempo.click)
        self.shortcut_decrease_tempo = QShortcut(QKeySequence("-"), self)
        self.shortcut_decrease_tempo.activated.connect(self.pushButton_decreaseTempo.click)
        self.shortcut_increase_tempo = QShortcut(QKeySequence("+"), self)
        self.shortcut_increase_tempo.activated.connect(self.pushButton_increaseTempo.click)
        self.shortcut_fast_decrease_tempo = QShortcut(QKeySequence("PgDown"), self)
        self.shortcut_fast_decrease_tempo.activated.connect(lambda: self.set_tempo(max(20, self.tempo - 10)))
        self.shortcut_fast_increase_tempo = QShortcut(QKeySequence("PgUp"), self)
        self.shortcut_fast_increase_tempo.activated.connect(lambda: self.set_tempo(min(260, self.tempo + 10)))

        self.shortcut_decrease_volume = QShortcut(QKeySequence("Down"), self)
        self.shortcut_decrease_volume.activated.connect(lambda: self.slider_volume.setValue(max(0, self.volume - 1)))
        self.shortcut_increase_volume = QShortcut(QKeySequence("Up"), self)
        self.shortcut_increase_volume.activated.connect(lambda: self.slider_volume.setValue(min(125, self.volume + 1)))
        self.shortcut_volume_25 = QShortcut(QKeySequence("F5"), self)
        self.shortcut_volume_25.activated.connect(lambda: self.slider_volume.setValue(25))
        self.shortcut_volume_50 = QShortcut(QKeySequence("F6"), self)
        self.shortcut_volume_50.activated.connect(lambda: self.slider_volume.setValue(50))
        self.shortcut_volume_75 = QShortcut(QKeySequence("F7"), self)
        self.shortcut_volume_75.activated.connect(lambda: self.slider_volume.setValue(75))
        self.shortcut_volume_100 = QShortcut(QKeySequence("F8"), self)
        self.shortcut_volume_100.activated.connect(lambda: self.slider_volume.setValue(100))

        for i in range(1, self.num_presets + 1):
            setattr(self, f"shortcut_load_preset_{i}", QShortcut(QKeySequence(str(i)), self))
            getattr(self, f"shortcut_load_preset_{i}").activated.connect(lambda i=i: self.load_preset(i))  # capture current value of i to avoid cell-var-from-loop problem

        self.shortcut_toggle_view_mode = QShortcut(QKeySequence("M"), self)
        self.shortcut_toggle_view_mode.activated.connect(self.on_toggle_view_mode)


    def closeEvent(self, event):
        """Handle the close event of the main window."""
        try:
            package_dir = os.path.dirname(os.path.abspath(__file__))
            save_config(self.config, config_dir=package_dir)
        except Exception as e:  # pylint: disable=broad-except
            QMessageBox.critical(self, "Error", f"Failed to save configuration to 'config.toml': {e}")
        event.accept()


    def connect_signals(self):
        """Connect GUI elements to their callback functions."""
        self.pushButton_openDownbeatSoundFile.clicked.connect(self.on_open_downbeat_sound_file)
        self.pushButton_openBackbeatSoundFile.clicked.connect(self.on_open_backbeat_sound_file)

        self.pushButton_playStop.clicked.connect(self.on_play_stop_clicked)
        self.pushButton_tapTempo.clicked.connect(self.on_tap_tempo_clicked)
        self.pushButton_downbeatAccent.clicked.connect(self.on_toggle_downbeat_accent)

        self.pushButton_timeSignature_2_4.clicked.connect(self.on_time_signature_2_4_clicked)
        self.pushButton_timeSignature_3_4.clicked.connect(self.on_time_signature_3_4_clicked)
        self.pushButton_timeSignature_4_4.clicked.connect(self.on_time_signature_4_4_clicked)
        self.pushButton_timeSignature_6_8.clicked.connect(self.on_time_signature_6_8_clicked)
        self.spinBox_timeSignatureDenominator.valueChanged.connect(self.on_time_signature_denominator_changed)
        self.spinBox_timeSignatureNumerator.valueChanged.connect(self.on_time_signature_numerator_changed)

        self.spinBox_tempo.valueChanged.connect(self.set_tempo)

        self.slider_volume.valueChanged.connect(self.on_volume_changed)

        # for i in range(1, self.num_presets + 1):
        #     getattr(self, f"pushButton_preset{i}").pressed.connect(getattr(self, f"on_preset{i}_pressed"))
        #     getattr(self, f"pushButton_released{i}").pressed.connect(getattr(self, f"on_preset{i}_released"))
        self.pushButton_preset1.pressed.connect(getattr(self, f"on_preset1_pressed"))
        self.pushButton_preset1.pressed.connect(getattr(self, f"on_preset1_released"))


    def init_with_config_values(self):
        """Initialize the main window with configuration values."""
        self.downbeat_accent = self.config["program_state"]["downbeat_accent"]
        self.pushButton_downbeatAccent.setIcon(self.icon_note_accent if self.downbeat_accent else self.icon_note)
        self.time_signature_numerator = int(self.config["program_state"]["time_signature_numerator"])
        self.time_signature_denominator = int(self.config["program_state"]["time_signature_denominator"])
        self.set_time_signature(self.time_signature_numerator, self.time_signature_denominator)
        self.tempo = int(self.config["program_state"]["tempo"])
        self.slider_tempo.setValue(self.tempo)
        self.config["program_state"]["tempo"] = self.tempo
        self.volume = int(self.config["program_state"]["volume"])
        self.set_volume(self.volume)

        self.downbeat_volume = self.config["general_settings"]["global_downbeat_volume"]
        self.backbeat_volume = self.config["general_settings"]["global_backbeat_volume"]
        self.current_downbeat_sound_file = self.config["preset1"]["downbeat_sound_file"] + ".wav"
        self.current_backbeat_sound_file = self.config["preset1"]["backbeat_sound_file"] + ".wav"
        package_dir = os.path.dirname(os.path.abspath(__file__))
        self.player_downbeat.setSource(QUrl.fromLocalFile(os.path.join(package_dir, self.current_downbeat_sound_file)))
        self.player_backbeat.setSource(QUrl.fromLocalFile(os.path.join(package_dir, self.current_backbeat_sound_file)))
        self.preset_downbeat_volume = self.config["preset1"]["downbeat_volume"]  # allows for correcting volume levels per preset
        self.preset_backbeat_volume = self.config["preset1"]["backbeat_volume"]  # allows for correcting volume levels per preset


    def init_geometry(self):
        """Initialize the geometry of the main window."""
        screen_geometry = self.screen().geometry()
        width, height = 500, 268
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


    def mousePressEvent(self, event: QMouseEvent) -> None:
        """Handle mouse press events for moving the window by dragging."""
        if event.button() == Qt.LeftButton:  # type: ignore
            self._drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()


    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """Handle mouse move events for moving the window by dragging."""
        if event.buttons() & Qt.LeftButton:  # type: ignore
            self.move(event.globalPosition().toPoint() - self._drag_position)
            event.accept()


    def on_open_backbeat_sound_file(self):
        """Open a file dialog to select a backbeat sound file."""
        file_dialog = QFileDialog(self, "Select Backbeat Sound File", os.getcwd(), "Audio Files (*.wav *.mp3 *.ogg)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                sound_file = selected_files[0]
                self.current_backbeat_sound_file = sound_file
                self.player_backbeat.setSource(QUrl.fromLocalFile(sound_file))


    def on_open_downbeat_sound_file(self):
        """Open a file dialog to select a downbeat sound file."""
        file_dialog = QFileDialog(self, "Select Downbeat Sound File", os.getcwd(), "Audio Files (*.wav);;All Files (*.*)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                sound_file = selected_files[0]
                self.current_downbeat_sound_file = sound_file
                self.player_downbeat.setSource(QUrl.fromLocalFile(sound_file))


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


    def on_preset1_clicked(self):
        """Load the preset 1 configuration."""
        self.load_preset(1)
        print("Preset 1 loaded.")


    def on_preset1_pressed(self):
        """Store the time when preset 1 button is pressed."""
        self.preset1_pressed_time = time.time()


    def on_preset1_released(self):
        """Store the time when preset 1 button is pressed."""
        delta = time.time() - self.preset1_pressed_time
        if delta >= MainWindow.LONG_PRESS_DURATION_MS / 1000:
            # Long press: save current configuration to preset 1.
            # self.save_current_configuration_to_preset(1)
            QMessageBox.information(self, "Info", "Current configuration saved to Preset 1.")


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
        # Clicking the tap tempo button multiple times sets the tempo according
        # to the average interval between the last few clicks. With the first
        # click, the button color changes to indicate that the application is in
        # tap tempo mode. If no further taps occur within a timeout period, the
        # mode ends. The logic is implemented using a simple state machine.
        # See MainWindow.TappingState for the states.

        # Note, there is the unlikely possibility of a race condition here if
        # the timeout occurs exactly when the button is clicked again. In that
        # case, the timeout handler and the click handler could both try to
        # change the state and button color simultaneously. However, since this
        # is a simple application, we ignore this possibility for the sake of
        # simplicity.

        if self.tap_state == MainWindow.TapState.WAITING_FOR_FIRST_TAP:
            # First tap: store the current time and change the button color.
            self.tap_times_ns = [time.time_ns()]
            # Change the button color to indicate tap tempo mode.
            style = "QPushButton {background-color:" + ACTIVE_ELEMENT_BG_COLOR + ";} " + \
                    "QPushButton:pressed {background-color: " + ACTIVE_ELEMENT_PRESSED_BG_COLOR + ";}"
            self.pushButton_tapTempo.setStyleSheet(style)
            self.tap_state = MainWindow.TapState.COLLECTING_TAPS
            # Start a single-shot timer to end the tap sequence after a timeout.
            self.tap_timer.start(self.TAP_TIMEOUT_MS)
        elif self.tap_state == MainWindow.TapState.COLLECTING_TAPS:
            # Subsequent taps: store the current time and calculate the tempo.
            current_time_ns = time.time_ns()
            self.tap_times_ns.append(current_time_ns)
            if len(self.tap_times_ns) > MainWindow.MAX_TAP_TIMES:
                self.tap_times_ns.pop(0)  # remove the oldest tap time
            # Calculate the average interval between taps.
            intervals_ns = [t2 - t1 for t1, t2 in zip(self.tap_times_ns[:-1], self.tap_times_ns[1:])]
            average_interval_ns = sum(intervals_ns) // len(intervals_ns)
            # Calculate the tempo in BPM.
            if average_interval_ns > 0:
                tempo = 60_000_000_000 // average_interval_ns
                tempo = max(MainWindow.MIN_TEMPO, min(MainWindow.MAX_TEMPO, tempo))
                self.set_tempo(tempo)
            # Restart the single-shot timer to end the tap sequence after a timeout.
            self.tap_timer.start(self.TAP_TIMEOUT_MS)
        elif self.tap_state == MainWindow.TapState.ENDING_TAP_SEQUENCE:
            # Restore color of the button and reset the state.
            self.pushButton_tapTempo.setStyleSheet("")
            self.tap_state = MainWindow.TapState.WAITING_FOR_FIRST_TAP


    def on_tap_tempo_timeout(self):
        """Handle the end of the tap tempo sequence due to timeout."""
        self.tap_state = MainWindow.TapState.ENDING_TAP_SEQUENCE
        self.on_tap_tempo_clicked()


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


    def on_toggle_downbeat_accent(self):
        """Toggle the downbeat accent setting."""
        self.downbeat_accent = not self.downbeat_accent
        self.config["general_settings"]["downbeat_accent"] = self.downbeat_accent
        self.pushButton_downbeatAccent.setIcon(self.icon_note_accent if self.downbeat_accent else self.icon_note)


    def on_toggle_view_mode(self):
        """Toggle the visibility of the preset and time signature buttons."""
        if self.view_mode_expanded:
            # switch to compact view
            self.view_mode_expanded = False
            self.setWindowFlags(Qt.FramelessWindowHint)  # type: ignore
            self.groupBox_presets.hide()
            self.groupBox_timeSignaturePresets.hide()
            self.slider_volume.setFocus()
            self.adjustSize()  # Let layout re-calculate size...
            self.resize(371, 210)
            self.show()
            QTimer.singleShot(0, lambda: self.resize(371, 210))  # ... and override it afterwards.
        else:
            # switch to expanded view
            self.view_mode_expanded = True
            self.setWindowFlags(Qt.Window)  # type: ignore
            self.groupBox_presets.show()
            self.groupBox_timeSignaturePresets.show()
            self.slider_volume.setFocus()
            self.adjustSize()
            self.resize(500, 268)  # former size: 478x268
            self.show()
            QTimer.singleShot(0, lambda: self.resize(500, 268))


    def on_volume_changed(self, value: int):
        """Handle changes of the volume slider."""
        self.set_volume(value)


    def play_beat_sound(self):
        """Play the metronome clicking sound."""
        # With each call, play either the downbeat or backbeat sound depending on
        # the current beat counter. After that, increase the counter accordingly.
        # Also, take the volume settings into account.
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


    def restore_program_state(self):
        """Restore the program state from the configuration."""
        sound_file_downbeat = self.config['preset1']['downbeat_sound_file']
        sound_file_backbeat = self.config['preset1']['backbeat_sound_file']
        self.player_downbeat.setSource(QUrl.fromLocalFile(sound_file_downbeat))
        self.player_backbeat.setSource(QUrl.fromLocalFile(sound_file_backbeat))
        self.pushButton_preset1.setStyleSheet(PRESET_ACTIVE_STYLE)  # TODO


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


    def setup_menubar(self):
        """Setup the menu bar."""
        self.action_About.triggered.connect(lambda: QMessageBox.information(self, "About", f"A Simple Metronome\nVersion {VERSION}\n(c) 2025 Christoph Hänisch"))
        self.action_Preferences.triggered.connect(self.show_settings_dialog)
        self.action_Quit.triggered.connect(self.close)
        self.action_ToggleViewMode.triggered.connect(self.on_toggle_view_mode)


    def show_settings_dialog(self):
        """Show the settings dialog."""
        self.settings_dialog.show()
        self.settings_dialog.raise_()


    def setup_dialogs(self):
        """Setup the settings dialog."""
        self.settings_dialog = SettingsDialog(parent=self)
        self.settings_dialog.hide()
