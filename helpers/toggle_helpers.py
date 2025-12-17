"""
Toggle helpers for Viewer.
Functions to update or reset toggle buttons based on Excel data or to clear them.
"""

from excel_processor import excel_read, excel_row_has_data, get_excel_name

def update_toggles(viewer, patient_id=None):
    """
    Update all ToggleButtons in the viewer based on Excel data.

    Args:
        viewer: The Viewer instance.
        patient_id: The ID of the patient to update. Defaults to viewer.current_patient.
    """
    if patient_id is None:
        patient_id = viewer.current_patient

    filename = get_excel_name()

    toggles = [
        viewer.ids.toggle_1,
        viewer.ids.toggle_2,
        viewer.ids.toggle_3,
        viewer.ids.toggle_4,
        viewer.ids.toggle_5,
        viewer.ids.dominance_toggle
    ]

    # Case 1: No data → reset UI
    if not excel_row_has_data(filename, patient_id):
        for t in toggles:
            t.state = "normal"
            t.background_color = (0.8, 0.8, 0.8, 1)  # gray
        print(f"Patient {patient_id}: empty → buttons reset")
        return

    # Case 2: Data exists → restore state
    values = excel_read(filename, patient_id)

    for toggle, value in zip(toggles, values):
        if value == 1:
            toggle.state = "down"
            toggle.background_color = (0.2, 0.7, 0.2, 1)  # green
        else:
            toggle.state = "normal"
            toggle.background_color = (0.8, 0.2, 0.2, 1)  # red

    print(f"Patient {patient_id}: buttons restored from Excel")


def clear_toggles(viewer):
    """
    Reset all toggle buttons to 'normal' state and gray background.

    Args:
        viewer: The Viewer instance.
    """
    toggles = [
        viewer.ids.toggle_1,
        viewer.ids.toggle_2,
        viewer.ids.toggle_3,
        viewer.ids.toggle_4,
        viewer.ids.toggle_5,
        viewer.ids.dominance_toggle
    ]
    for t in toggles:
        t.state = "normal"
        t.background_color = (0.8, 0.8, 0.8, 1)
    print("All toggle buttons cleared")
