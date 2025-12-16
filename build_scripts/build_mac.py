# build_mac.py = Build script for packaging the app for macOS only
import os
import shutil
import subprocess
import sys

# ================= CONFIG =================
OUTPUT_FOLDER = "/Users/guillaumefahrni/Desktop/APPTEST" # Change this to your desired output folder
# ========================================

# Application specific settings
NAME = "SimpleImageGrader"
ICON = "assets/SimpleImageGrader.icns"
MAIN = "main.py"
WORKPATH = os.path.join(os.getcwd(), "build")  # temporary PyInstaller folder
WINDOWED = True       # True = no terminal window
ADD_DATA = [
    "viewer.kv:.", 
    "assets:assets",
    ]  # Add any extra files/folders here
SPEC_FILE = f"{NAME}.spec"

# Function to clean old build/dist
def clean_paths(paths):
    """Remove files or folders from the given list of paths."""
    for path in paths:
        if os.path.exists(path):
            if os.path.isdir(path):
                print(f"Removing folder: {path}")
                shutil.rmtree(path)
            else:
                print(f"Removing file: {path}")
                os.remove(path)

# ------------------ MAC BUILD ------------------
print("Building macOS .app...")

# Clean previous builds
clean_paths([OUTPUT_FOLDER, WORKPATH, SPEC_FILE])

# Build command for macOS
cmd = [
    "pyinstaller",
    "--noconfirm",  # Remove previous output without asking
    "--clean",      # Clean PyInstaller cache and temp files before building
    "--onedir",     # Create a one-folder bundle (required for .app)
    f"--name={NAME}",
]

if WINDOWED:
    cmd.append("--windowed")

cmd += ["--icon", ICON]
cmd += ["--distpath", OUTPUT_FOLDER, "--workpath", WORKPATH, MAIN]

# Add extra data files
for data in ADD_DATA:
    cmd += ["--add-data", data]

print("Running PyInstaller command:")
print(" ".join(cmd))

# Execute PyInstaller
subprocess.run(cmd, check=True) # check=True to raise error if fails

# Keep only the .app, remove other files/folders in OUTPUT_FOLDER
app_path = os.path.join(OUTPUT_FOLDER, f"{NAME}.app")

for item in os.listdir(OUTPUT_FOLDER):
    full_path = os.path.join(OUTPUT_FOLDER, item)
    if full_path != app_path:
        if os.path.isdir(full_path):
            shutil.rmtree(full_path)
        else:
            os.remove(full_path)

# Clean up build folder and spec file
clean_paths([SPEC_FILE, WORKPATH])

print(f"\n✓ macOS build complete!")
print(f"Application is ready at: {OUTPUT_FOLDER}")
print(f"App location: {app_path}")