from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from helpers.sounds import Sounds
import os


# Your functions
from excel_processor import (excel_process, excel_row_has_data, excel_read, get_excel_name,get_current_patient)
from helpers.keyboard_handler import handle_key_press
from helpers.toggle_helpers import update_toggles, clear_toggles
from helpers.popups import go_to_patient_popup
from images_processor import get_patient_images

# Load the KV file for the Viewer layout
Builder.load_file(os.path.join(os.path.dirname(__file__), "viewer.kv"))

# ==========================
# Define Viewer class
# ==========================
class Viewer(BoxLayout):
    current_patient = NumericProperty(1) # Track the current patient ID

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.current_patient = 1  # Initializedefault patient number
        self.shortcuts_enabled = True  # NEW: flag to enable/disable keyboard shortcuts       
        Window.bind(on_key_down=self._on_keyboard_down) # Bind keyboard event
        Clock.schedule_once(lambda dt: self.buttons_update(), 0)  # Initial button update, with Clock to wait for UI to be ready
        self.sounds_enabled = True  # Sound enabled by default
        self.sounds = Sounds()  # Initialize sounds handler

    # Handle keyboard input, delegating to the helpers/keyboard_handler.py
    def _on_keyboard_down(self, window, key, scancode, codepoint, modifiers):
        if not getattr(self, "shortcuts_enabled", True):
            return False  # Ignore key presses if shortcuts are disabled
        return handle_key_press(self, key)
    

    # Update toggle buttons based on current patient, delegating to the helpers/toggle_helpers.py
    def buttons_update(self):
        update_toggles(self)
        self.refresh_images() # Refresh images for the current patient

    def previous_item(self):
        """Called when Previous button is pressed or Q key is pressed"""
        if self.current_patient <= 1:
            print("Already at the first patient. Cannot go back further.")
            return  # Stop here, do not decrement

        print("Previous clicked… ")
        self.current_patient -= 1
        self.buttons_update() # Reset buttons for the new patient
        self.ids.patient_label.text = f"Current Patient: {self.current_patient}"

    def validate_item(self):
        """Called when Validate button is pressed or Space key is pressed"""
        print("Validate clicked… ")
        excel_process(self) # Write the results to the corresponding patient in the Excel file
        self.sounds.play_validate() if self.sounds_enabled else None # Play validate sound if enabled
        self.current_patient += 1
        self.buttons_update() # Reset buttons for the new patient
        self.ids.patient_label.text = f"Current Patient: {self.current_patient}"

    def next_item(self):
        """Called when Next button is pressed or E key is pressed"""
        print("Next clicked… ")
        self.current_patient += 1
        self.buttons_update() # Reset buttons for the new patient
        self.ids.patient_label.text = f"Current Patient: {self.current_patient}"
    
    # Clear all toggle buttons, delegating to the helpers/toggle_helpers.py
    def clear_togglebuttons(self):
        clear_toggles(self)

    # Go to a specific patient, delegating to the helpers/popups.py
    def goto_item(self):
        go_to_patient_popup(self)
            
    def refresh_images(self):
        """Populate the images_layout with all images of the current patient."""
        layout = self.ids.images_layout
        layout.clear_widgets()

        image_paths = get_patient_images(self.current_patient)

        if not image_paths:
            layout.add_widget(Label(text="No images for this patient", size_hint_y=None, height=50))
            return

        for img_path in image_paths:
            img_widget = Image(
                source=img_path,
                size_hint=(1, None),
                allow_stretch=True,
                keep_ratio=True
            )

            def update_height(instance, value):
                if not instance.texture:
                    return

                tex_w = instance.texture.width
                tex_h = instance.texture.height
                ratio = tex_h / tex_w

                # Do NOT upscale beyond native resolution
                display_width = min(instance.width, tex_w)
                instance.height = display_width * ratio


            img_widget.bind(width=update_height)
            img_widget.bind(texture=update_height)

            layout.add_widget(img_widget)

    def toggle_sound(self): # Switch sound on/off
        """Toggle sound on/off."""
        if self.sounds_enabled:
            self.sounds_enabled = False
            print("Sound disabled.")
        else:
            self.sounds_enabled = True
            print("Sound enabled.")
  
