"""
CP1404/CP5632 Practical
Dynamic Labels
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Kivy app for dynamic labels."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.label_names = ["1","2","3","4"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add to GUI"""
        for name in self.label_names:
            temp_label = Label(text=name)
            temp_label.background_color = (1, 0, 1, 1)
            self.root.ids.main.add_widget(temp_label)

    def clear_all(self):
        """Clear all labels in "main" layout widget."""
        self.root.ids.main.clear_widgets()


DynamicLabelsApp().run()