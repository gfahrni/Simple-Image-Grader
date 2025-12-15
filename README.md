# Simple Image Grader

**Simple Image Grader** is a lightweight Python/Kivy application for quickly reviewing and grading images associated with patients. It provides a simple interface to toggle multiple grading criteria, navigate between patients, and save results to an Excel file.

---

## Features

- Display images for each patient in a scrollable view.
- Grade images using 5 toggle buttons:
  1. Bad image quality
  2. Small segmentation error
  3. Large segmentation error
  4. Artifact
  5. Infarct
- Keyboard shortcuts for fast navigation:
  - `Q` → Previous patient
  - `E` → Next patient
  - `Space` → Validate and save
  - `C` → Clear toggles
  - `G` → Go to specific patient
  - `1-5` → Toggle corresponding button
- Automatic Excel file creation and backup.
- Validation sound feedback.
- Popup support for "Go To Patient".

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Simple-Image-Grader.git
cd Simple-Image-Grader
```

2. Create a Python virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the app with:

```bash
python main.py
```

- Ensure an `images/` folder exists with patient images named like `001_p1.png`, `001_p2.png`, etc.
- The first run will create a `results.xlsx` Excel file to store grading results.
- Use the toggle buttons or keyboard shortcuts to grade images.
- Use the "Validate" button (or Space key) to save results and move to the next patient.
- Backups of Excel data are automatically created if data for a patient is overwritten.

---

## Directory Structure

```
Simple-Image-Grader/
├── main.py
├── viewer.py
├── viewer.kv
├── paths.py
├── excel_processor.py
├── images_processor.py
├── helpers/
│   ├── sounds.py
│   ├── popups.py
│   ├── keyboard_handler.py
│   └── toggle_helpers.py
├── sounds/
│   └── validate.wav
├── images/
│   └── *.png
├── requirements.txt
└── SimpleImageGrader.icns
```

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## Notes

- Works on **macOS** and **Windows**.
- Compatible with Python 3.10+.
- Uses Kivy for the GUI and OpenPyXL for Excel manipulation.

