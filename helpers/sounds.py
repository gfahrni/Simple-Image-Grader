# helpers/sounds.py

import os
from kivy.core.audio import SoundLoader
from helpers.paths import DATA_FOLDER

class Sounds:
    def __init__(self):
        # Load validate sound
        sound_path = os.path.join('assets','validate.wav') # Relative path to sounds folder
        self.validate_sound = SoundLoader.load(sound_path)
        if self.validate_sound:
            print(f"Validate sound loaded: {sound_path}")
        else:
            print(f"Failed to load sound: {sound_path}")

    def play_validate(self):
        print("Playing validate sound...")
        if self.validate_sound:
            self.validate_sound.play()
