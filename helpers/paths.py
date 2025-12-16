import sys
from pathlib import Path

# ============================================================================
# DETERMINE DATA FOLDER PATH AND RUNTIME PATH
# 
# Data files location depends on execution context:
# - Packaged app: Data lives in same folder as executable (.app/.exe)
# - Development mode: Data lives in "data" subfolder of project.
#
# RUNTIME_PATH function helps locate assets during runtime (such as icons, sounds, kv files).
# ============================================================================

DATA_FOLDER = (
    # Packaged macOS app
    Path(sys.executable).parent.parent.parent.parent # for MacOs, the data folder is the folder containing the .app
    if getattr(sys, 'frozen', False) and sys.platform == 'darwin' and 'Contents/MacOS' in sys.executable
    
    # Other packaged apps (Windows, Linux)
    else Path(sys.executable).parent if getattr(sys, 'frozen', False) # the data folder is the executable's folder
    
    # Development mode (default)
    else Path(__file__).parent.parent / "data" # Path to 'data' folder in development
)

def RUNTIME_PATH(*parts):
    """
    Path helper for runtime assets (icons, sounds, kv, etc.)

    DEV:
        <project_root>/<parts>

    PyInstaller (--onedir / --onefile):
        _MEIPASS/<parts>
    """
    if getattr(sys, "frozen", False): # frozen = packaged by PyInstaller
        return Path(sys._MEIPASS).joinpath(*parts) # MEIPASS is the temp folder created by PyInstaller
    return Path(__file__).parent.parent.joinpath(*parts) 
