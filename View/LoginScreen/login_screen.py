from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

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

    def login_user(self):
        user_login = self.ids.field_login.text
        user_password = self.ids.field_password.text

        if status := self.controller.login_user(user_login, user_password):
            self.app.user_login = user_login
            self.popup = Popup(title='Информация', 
                            content=Label(text='Успешно.',
                                            color = "white",
                                            font_size = "22sp",
                                            font_name = "assets/fonts/futuralightc.otf"),
                            pos_hint = {'center_x': 0.5,'center_y': 0.5},
                            size_hint = (0.4, 0.3),
                            background = 'assets/images/bg_3.png',
                            title_color = 'white',
                            title_size = '28sp',
                            title_font = 'assets/fonts/futuralightc.otf')

        else:
            self.popup = Popup(title='Внимание', 
                            content=Label(text='Ошибка',
                                            color = "white",
                                            font_size = "22sp",
                                            font_name = "assets/fonts/futuralightc.otf"),
                            pos_hint = {'center_x': 0.5,'center_y': 0.5},
                            size_hint = (0.4, 0.3),
                            background = 'assets/images/bg_3.png',
                            title_color = 'white',
                            title_size = '28sp',
                            title_font = 'assets/fonts/futuralightc.otf',)

        self.popup.open()
        self.switch_screen('main screen')

