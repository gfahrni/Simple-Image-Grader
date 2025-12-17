"""
Keyboard handler for Viewer.
Provides a function to process key presses and trigger the appropriate Viewer actions.
"""

def handle_key_press(viewer, key):
    """
    Handles keyboard input for the Viewer.

    Args:
        viewer: The instance of the Viewer class.
        key: The key code from the keyboard event.

    Returns:
        True if the key was handled, False otherwise.
    """

    # Previous / Next / Validate / Clear / Go To / Mute Sound
    if key == 113:  # Q
        viewer.ids.previous_button.trigger_action(duration=0.1) # Trigger Previous button
        return True
    elif key == 101:  # E
        viewer.ids.next_button.trigger_action(duration=0.1) # Trigger Next button
        return True
    elif key == 32:   # Space
        viewer.ids.validate_button.trigger_action(duration=0.1) # Trigger Validate button
        return True
    elif key == 99:   # C
        viewer.ids.clear_button.trigger_action(duration=0.1) # Trigger Clear button
        return True
    elif key == 103:  # G
        viewer.ids.goto_button.trigger_action(duration=0.1) # Trigger Go To button
        return True
    elif key == 109:  # M
        viewer.ids.sound_toggle.trigger_action(duration=0.1) # Trigger Mute Sound button
        return True
    elif key == 100:  # D
        viewer.ids.dominance_toggle.trigger_action(duration=0.1) # Trigger Dominance toggle button
        return True

    # Toggle buttons 1-5
    toggle_mapping = {
        49: 'toggle_1',  # 1
        50: 'toggle_2',  # 2
        51: 'toggle_3',  # 3
        52: 'toggle_4',  # 4
        53: 'toggle_5',  # 5
    }

    if key in toggle_mapping:
        toggle = viewer.ids[toggle_mapping[key]]
        # Toggle the button state
        toggle.state = 'normal' if toggle.state == 'down' else 'down'
        return True

    # Key not handled
    return False
