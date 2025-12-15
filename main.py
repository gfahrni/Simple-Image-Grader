import os
import sys
from paths import runtime_path

# ==========================
# Set window icon
# ==========================
icon_path = runtime_path("SimpleImageGrader.icns")
from kivy.config import Config
if os.path.exists(icon_path):
    Config.set('kivy', 'window_icon', icon_path) # Set icon before importing Window
from kivy.core.window import Window # Import after Config
if os.path.exists(icon_path):
    Window.icon = icon_path # Set icon for the window

# ==========================
# Helper to get app root
# ==========================
def app_root():
    """
    Returns the directory where the app executable lives.
    Works for:
    - normal Python
    - PyInstaller one-folder
    - macOS .app
    """
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

# Force a stable working directory
os.chdir(app_root())

# ==========================
# Import Kivy App and Viewer
# ==========================
from kivy.app import App
from viewer import Viewer

# ==========================
# Define MainApp
# ==========================
class MainApp(App):
    def build(self):
        # Ensure the 'images' folder exists
        images_folder = runtime_path("images")
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
