# helpers/sounds.py

import os
from kivy.core.audio import SoundLoader
from paths import runtime_path

class Sounds:
    def __init__(self):
        # Load validate sound
        sound_path = runtime_path("sounds", "validate.wav")  # path to the validate sound file
        self.validate_sound = SoundLoader.load(sound_path)
        if self.validate_sound:
            print(f"Validate sound loaded: {sound_path}")
        else:
            print(f"Failed to load sound: {sound_path}")

    def play_validate(self):
        if self.validate_sound:
            self.validate_sound.play()
