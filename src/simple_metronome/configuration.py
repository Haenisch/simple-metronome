# Copyright (c) 2025 Christoph Hänisch.
# This file is part of the "Metronome" application.
# It is licensed under the GNU General Public License v3.0 or higher.
# See the LICENSE file for more details.

"""Functions to load and save the configuration from/to a TOML file.

If no configuration file is found, or if it is malformed, default settings
are used instead.

Functions:

    load_config() -> dict:
        Load the configuration from a TOML file.

    save_config(config: dict) -> None:
        Save the configuration to a TOML file.
"""

# pylint: disable=line-too-long

import os
import toml


default_config ={
    'general_settings': {
        'gui_scale_factor': 1.25,
        'downbeat_volume': 100,
        'regular_beats_volume': 80},
    'program_state': {
        'first_run': True,
        'active_preset_index': 1,
        'active_preset_altered': False,
        'enable_downbeat': True,
        'downbeat_sound': 'click',
        'downbeat_volume': 100,
        'regular_beats_sound': 'click',
        'regular_beats_volume': 80,
        'time_signature_numerator': 4,
        'time_signature_denominator': 4,
        'tempo': 100,
        'volume': 80},
    'preset1': {
        'enable_downbeat': True,
        'downbeat_sound': 'click',
        'downbeat_volume': 100,
        'regular_beats_sound': 'click',
        'regular_beats_volume': 80,
        'time_signature_numerator': 4,
        'time_signature_denominator': 4,
        'tempo': 100,
        'volume': 80},
    'preset2': {
        'enable_downbeat': True,
        'downbeat_sound': 'click',
        'downbeat_volume': 100,
        'regular_beats_sound': 'click',
        'regular_beats_volume': 80,
        'time_signature_numerator': 4,
        'time_signature_denominator': 4,
        'tempo': 100,
        'volume': 80},
    'preset3': {
        'enable_downbeat': True,
        'downbeat_sound': 'click',
        'downbeat_volume': 100,
        'regular_beats_sound': 'click',
        'regular_beats_volume': 80,
        'time_signature_numerator': 4,
        'time_signature_denominator': 4,
        'tempo': 100,
        'volume': 80},
    'preset4': {
        'enable_downbeat': True,
        'downbeat_sound': 'click',
        'downbeat_volume': 100,
        'regular_beats_sound': 'click',
        'regular_beats_volume': 80,
        'time_signature_numerator': 4,
        'time_signature_denominator': 4,
        'tempo': 100,
        'volume': 80},
    'preset5': {
        'enable_downbeat': True,
        'downbeat_sound': 'click',
        'downbeat_volume': 100,
        'regular_beats_sound': 'click',
        'regular_beats_volume': 80,
        'time_signature_numerator': 4,
        'time_signature_denominator': 4,
        'tempo': 100,
        'volume': 80}
    }


class Status:
    """Class to represent the status of loading the configuration.
    
    This class contains a status code and an optional message. If the loading
    was successful, the status code is SUCCESS. Otherwise, it indicates the type
    of error that occurred.

    The class follows the "truthy" convention, where an instance evaluates to
    True if the loading was successful, and False otherwise.

    Attributes:
        SUCCESS: Status code indicating successful loading.
        MISSING_SETTINGS: Status code indicating that some configuration settings were missing and default values were applied.
        FILE_NOT_FOUND: Status code indicating that the configuration file was not found.
        PARSE_ERROR: Status code indicating that there was an error parsing the configuration file.

        code: The actual status code of the loading operation.
        message: An optional message providing additional information about the loading status.
    """
    SUCCESS = 0
    MISSING_SETTINGS = 1
    FILE_NOT_FOUND = 2
    PARSE_ERROR = 3

    def __init__(self, code: int = SUCCESS, message: str = ""):
        """Initialize the Status instance."""
        self.code = code
        self.message = message

    def __bool__(self):
        return self.code == self.SUCCESS


def load_config(config_dir: str = "") -> tuple[dict, Status]:
    """Load the configuration from a TOML file.
    
    Arguments:
        config_dir: Optional directory path where the configuration file is
          located. Default is the current directory.

    Returns:
        A tuple containing the configuration dictionary and a Status object
        indicating the result of the loading operation.
    """
    status = Status()

    try:
        config_file_path = os.path.join(config_dir, "config.toml") if config_dir else "config.toml"
        config = toml.load(config_file_path)
    except FileNotFoundError:
        status.code = Status.FILE_NOT_FOUND
        status.message = "Configuration file 'config.toml' not found. Using default settings."
        return default_config, status
    except toml.TomlDecodeError as e:
        status.code = Status.PARSE_ERROR
        status.message = f"Failed to parse configuration file 'config.toml': {e}"
        return default_config, status

    # Check if all required tables along with key-value pairs are present; if not, use defaults.
    anything_missing = False
    for table, default_key_value_pairs in default_config.items():
        if table not in config:
            print(f"Missing table '{table}' in configuration. Applying default values.")
            config[table] = default_key_value_pairs
            anything_missing = True
        else:
            for key, value in default_key_value_pairs.items():
                if key not in config[table]:
                    print(f"Missing key '{key}' in table '{table}'. Applying default value.")
                    config[table][key] = value
                    anything_missing = True
    if anything_missing:
        status.code = Status.MISSING_SETTINGS
        status.message = "Some configuration settings were missing in 'config.toml'. Default values have been applied."

    return config, status


def save_config(config: dict, config_dir: str = "") -> None:
    """Save the configuration to a TOML file.
    
    Arguments:
        config: The configuration dictionary to save.
        config_dir: Optional directory path where the configuration file is
          located. Default is the current directory.

    Exceptions:
        Raises an exception if saving the configuration fails.
    """
    config_file_path = os.path.join(config_dir, "config.toml") if config_dir else "config.toml"
    with open(config_file_path, "w", encoding="utf-8") as file:
        toml.dump(config, file)
