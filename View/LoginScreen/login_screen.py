from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import NumericProperty

from View.base_screen import BaseScreenView
from View.LoginScreen.components import FillField, CommonLabel

class LoginScreenView(BaseScreenView):
    """Implements the login start screen in the user application."""

    OPACITY = NumericProperty(0)
    SHIFT_Y = NumericProperty(dp(0))
    FIELD_WIDTH = NumericProperty(dp(320))
    FIELD_HEIGHT = NumericProperty(dp(52))
    PADDING = NumericProperty(dp(24))

    def on_enter(self, *args):        
        if not self.app.enable_animation:
            animation = Animation(SHIFT_Y=dp(140), d=1, t="in_out_quart")
            animation.start(self)
        else:
            super().on_enter()

        Animation(OPACITY=1, d=3).start(self)

    def back_to_first_screen(self):
        self.manager_screens.current_hero = self.ids.hero.tag
        self.manager_screens.current = "main screen"
        self.switch_screen("main screen")

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
