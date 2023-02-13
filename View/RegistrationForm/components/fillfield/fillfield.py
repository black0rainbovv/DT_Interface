from kivymd.uix.textfield import MDTextField


class FillField(MDTextField):
    """It is just a base class for a text field with common parameters."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = None
        self.width = "320dp"
        self.mode = "fill"
        self.fill_color_normal = (1, 1, 1, 0.1)
        self.fill_color_focus = (1, 1, 1, 0.3)
