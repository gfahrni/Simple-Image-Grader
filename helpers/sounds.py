# helpers/sounds.py

from kivy.core.audio import SoundLoader
from helpers.paths import RUNTIME_PATH

class Sounds:
    def __init__(self):
        # Load validate sound
        sound_path = RUNTIME_PATH("assets", "validate.wav") # Path to validate.wav sound file
        self.validate_sound = SoundLoader.load(str(sound_path))
        if self.validate_sound:
            print(f"Validate sound loaded: {sound_path}")
        else:
            print(f"Failed to load sound: {sound_path}")

    def play_validate(self):
        print("Playing validate sound...")
        if self.validate_sound:
            self.validate_sound.play()
