# helpers/icon_setup.py = script to set window icon based on platform (macOS and Windows)
import os
import sys
from kivy.core.window import Window

def set_window_icon():
    """Set window icon for macOS and Windows only"""
    # Define icon_path based on platform
    if sys.platform == 'darwin':  # macOS
        icon_path = 'assets/icon.icns'
    elif sys.platform == 'win32':  # Windows
        icon_path = 'assets/icon.ico'
    else:
        # Not macOS or Windows, don't set icon
        return False
    
    # Try platform-specific icon
    if os.path.exists(icon_path):
        Window.set_icon(icon_path)
        return True
    
    return False