"""
Toggle helpers for Viewer.
Functions to update or reset toggle buttons based on Excel data or to clear them.
"""

from excel_processor import excel_read, excel_row_has_data, get_excel_path


def update_toggles(viewer, patient_id=None):
    """
    Update all ToggleButtons in the viewer based on Excel data.

    Args:
        viewer: The Viewer instance.
        patient_id: The ID of the patient to update. Defaults to viewer.current_patient.
    """
    if patient_id is None:
        patient_id = viewer.current_patient

    filename = get_excel_path()

    toggles = [
        viewer.ids.toggle_1,
        viewer.ids.toggle_2,
        viewer.ids.toggle_3,
        viewer.ids.toggle_4,
        viewer.ids.toggle_5,
    ]

    # Read values from Excel
    values = excel_read(filename, patient_id)

    # --------------------------------------------------
    # Case 1: No data for this patient → RESET UI
    # --------------------------------------------------
    if values is None or not excel_row_has_data(filename, patient_id):
        for t in toggles:
            t.state = "normal"
            t.background_color = (0.8, 0.8, 0.8, 1)  # gray

        viewer.dominance = 0  # Default (Right)
        viewer.update_dominance_ui()

        print(f"Patient {patient_id}: empty → buttons reset")
        return

    # --------------------------------------------------
    # Case 2: Data exists → RESTORE UI
    # --------------------------------------------------

    # values = [t1, t2, t3, t4, t5, dominance]
    toggle_values = values[:-1]
    dominance_value = values[-1]

    for toggle, value in zip(toggles, toggle_values):
        if value == 1:
            toggle.state = "down"
            toggle.background_color = (0.2, 0.7, 0.2, 1)  # green
        else:
            toggle.state = "normal"
            toggle.background_color = (0.8, 0.2, 0.2, 1)  # red

    viewer.dominance = dominance_value
    viewer.update_dominance_ui()

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
    ]

    for t in toggles:
        t.state = "normal"
        t.background_color = (0.8, 0.8, 0.8, 1)

    viewer.dominance = 0  # Default (Right)
    viewer.update_dominance_ui()

    print("All toggle buttons cleared")
