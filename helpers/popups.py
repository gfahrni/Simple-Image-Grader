"""
Popup helpers for Viewer.
Contains functions to create and handle popups like 'Go To Patient'.
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock

def go_to_patient_popup(viewer):
    """Open a popup to jump to a specific patient."""
    # Disable global shortcuts while popup is open
    viewer.shortcuts_enabled = False

    # --- Layout ---
    main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
    label = Label(text="Enter Patient ID:")

    input_layout = BoxLayout(orientation='horizontal', spacing=10)
    input_box = TextInput(
        multiline=False,
        input_filter='int',
        background_color=(0.9, 0.9, 0.9, 1),
        font_size=54,
        halign='center',
        padding_y=(20, 20),
    )

    go_button = Button(text="Go", size_hint_x=None, width=200)

    input_layout.add_widget(input_box)
    input_layout.add_widget(go_button)

    main_layout.add_widget(label)
    main_layout.add_widget(input_layout)

    popup = Popup(title="Go To Patient", content=main_layout, size_hint=(0.5, 0.3))

    # --- Button action ---
    def go_pressed(instance=None):
        try:
            patient_id = int(input_box.text)
            if patient_id < 1:
                print("Patient ID must be >= 1")
                return
            viewer.current_patient = patient_id
            from helpers.toggle_helpers import update_toggles
            update_toggles(viewer)
            viewer.ids.patient_label.text = f"Current Patient: {viewer.current_patient}"
            popup.dismiss()
        except ValueError:
            print("Invalid input, must be a number")

    go_button.bind(on_release=go_pressed)

    # --- Bind Enter key for this popup ---
    def on_key_down(window, key, scancode, codepoint, modifiers):
        if key == 13:  # Enter
            go_pressed()
            return True
        return False

    Window.bind(on_key_down=on_key_down)

    # --- Re-enable shortcuts and unbind Enter when popup closes ---
    def on_popup_dismiss(instance):
        viewer.shortcuts_enabled = True
        Window.unbind(on_key_down=on_key_down)

    popup.bind(on_dismiss=on_popup_dismiss)

    # --- Open popup and focus input ---
    popup.open()
    Clock.schedule_once(lambda dt: setattr(input_box, 'focus', True), 0.1)
