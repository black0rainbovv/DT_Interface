from kivymd.uix.label import MDLabel


class CommonLabel(MDLabel):

    """It is just a base class for a label with common parameters."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (1, 1, 1, 1)
        self.font_style = "H4"
        self.font_name = "assets/fonts/futuralightc.otf"
        self.adaptive_height = True
        self.markup = True
