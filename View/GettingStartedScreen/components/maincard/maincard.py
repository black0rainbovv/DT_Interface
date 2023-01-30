from kivymd.uix.card import MDCard


class MainCard(MDCard):
    '''Implements the specified properties of MDCard'''
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orientation = "vertical"
        self.line_color = (0.2, 0.2, 0.2, 0.8)
        self.style = "filled"
        self.md_bg_color = "#E2E2E5"
        self.size_hint_y = 0.85
        self.size_hint_x = 0.5
        self.pos_hint = {"center_x": .5, "center_y": .5}
        self.radius = 24
        self.ripple_behavior = True
        self.unfocus_color = "darkgrey"
        self.focus_color = "grey"
