import os
import sys
from helpers.paths import DATA_FOLDER    # Import DATA_FOLDER constant from helpers.path
from helpers.icon_setup import set_window_icon  # Import set_window_icon function
from kivy.app import App
from viewer import Viewer

# set window icon based on platform
set_window_icon()

# ==========================
# Define MainApp
# ==========================
class MainApp(App):
    def build(self):
        # Ensure the 'images' folder exists
        images_folder = os.path.join(DATA_FOLDER, 'images') # Path to 'images' folder
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)
            print(f"Created folder: {images_folder}")

        # Return main UI
        return Viewer()

# ==========================
# Run the app
# ==========================
if __name__ == "__main__":
    MainApp().run()
