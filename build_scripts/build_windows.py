# build_windows.py
import os
import shutil
import subprocess

# ================= CONFIG =================
# Output folder for the final exe
OUTPUT_FOLDER = os.path.join(os.getcwd(), "dist_win")
# Temporary PyInstaller work folder
WORKPATH = os.path.join(os.getcwd(), "build_win")
# Application name
NAME = "SimpleImageGrader"
# Main entry script
MAIN = "main.py"
# Application icon for Windows
ICON = "assets/SimpleImageGrader.ico"
# Windowed = True will hide the console window
WINDOWED = True
# Additional files/folders to include (format: "source;destination")
ADD_DATA = [
    "viewer.kv;.",        # KV file to the root of exe folder
    "assets;assets",      # Copy assets folder
]
# PyInstaller spec file (will be auto-created)
SPEC_FILE = f"{NAME}.spec"
# ========================================

def clean_paths(paths):
    """Remove files or folders if they exist."""
    for path in paths:
        if os.path.exists(path):
            if os.path.isdir(path):
                print(f"Removing folder: {path}")
                shutil.rmtree(path)
            else:
                print(f"Removing file: {path}")
                os.remove(path)

# ------------------ WINDOWS BUILD ------------------
print("Building Windows .exe...")

# Clean previous builds
clean_paths([OUTPUT_FOLDER, WORKPATH, SPEC_FILE])

# Build command
cmd = [
    "pyinstaller",
    "--noconfirm",      # Remove old outputs automatically
    "--clean",          # Clean PyInstaller cache/temp files
    "--onedir",        # Build a one-folder bundle
    f"--name={NAME}",   # Name of the exe
]

if WINDOWED:
    cmd.append("--windowed")  # Hide console window

# Set icon
cmd += ["--icon", ICON]

# Add data files/folders
for data in ADD_DATA:
    cmd += ["--add-data", data]

# Set output/dist and work paths
cmd += ["--distpath", OUTPUT_FOLDER, "--workpath", WORKPATH, MAIN]

# Print and run PyInstaller
print("Running PyInstaller command:")
print(" ".join(cmd))
subprocess.run(cmd, check=True)

# Clean spec file and build folder after successful build
clean_paths([SPEC_FILE, WORKPATH])

print(f"\n✓ Windows build complete!")
print(f"Executable is ready at: {os.path.join(OUTPUT_FOLDER, NAME+'.exe')}")
print("Remember to keep the 'data' folder next to the exe for your images and Excel results.")
