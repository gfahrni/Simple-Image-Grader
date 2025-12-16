import sys
from pathlib import Path

# ============================================================================
# DETERMINE DATA FOLDER PATH
# 
# Data files location depends on execution context:
# - Packaged app: Data lives in same folder as executable (.app/.exe)
# - Development mode: Data lives in "data" subfolder of project
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
