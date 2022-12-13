from kivymd.uix.label import MDLabel


class SettingLabel(MDLabel):
    '''Implements the specified properties of MDLabel'''
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size_hint_y = 2
        self.padding_x = 12
        self.font_size = "18sp"
        self.font_name = "assets/fonts/futuralightc.otf"
        self.color = "454749"
