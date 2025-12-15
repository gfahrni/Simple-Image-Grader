# Helper functions to manage runtime paths

import os
import sys

# Get the directory where the app executable lives
def runtime_dir():
    if getattr(sys, "frozen", False):
        # macOS .app → escape the bundle
        if sys.platform == "darwin":
            return os.path.abspath(
                os.path.join(os.path.dirname(sys.executable), "../../..")
            )
        # Windows → stay next to the .exe
        return os.path.dirname(sys.executable)

    # Normal Python execution
    return os.path.dirname(os.path.abspath(__file__))



# Get the full path to a resource relative to the runtime directory
def runtime_path(*parts):
    return os.path.join(runtime_dir(), *parts)
