from kivymd.uix.label import MDLabel


class AboutDeviceLabel(MDLabel):
    '''Implements the specified properties of MDLabel'''
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = "white"
        self.font_size = "24sp"
        self.font_name = "assets/fonts/futuralightc.otf"
        self.font_style = "H6"
