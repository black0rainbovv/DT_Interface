from View.base_screen import BaseScreenView
from View.MainScreen.components import MainLabel, MainCard

from kivy.uix.popup import Popup
from kivy.uix.label import Label


class GettingStartedView(BaseScreenView):
    '''Implements the login start screen in the user application.'''

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.ids.maintopbar.title = self.app.serial_number
        self.popup = Popup()

    def model_is_changed(self) -> None:

        '''
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        '''
        
    def on_enter(self, *args):
        """
        Event called when the screen is displayed: the entering animation is
        complete.
        """ 

    def callback(self, instance):
        if instance.icon == 'power':
            quit()
        if instance.icon == 'arrow-up-drop-circle-outline':
            self.controller.tb_movement()

    def last_run(self):  # sourcery skip: remove-pass-body
        if self.controller.last_run():
            print('run')                           #swicth screen на экран выполнения протокола 
        else:
            self.popup = Popup(title='Внимание', 
                            content=Label(text='Непредвиденная ошибка.',
                                            color = "white",
                                            font_size = "22sp",
                                            font_name = "assets/fonts/futuralightc.otf"),
                            pos_hint = {'center_x': 0.5,'center_y': 0.5},
                            size_hint = (0.4, 0.3),
                            background = 'assets/images/bg_3.png',
                            title_color = 'white',
                            title_size = '28sp',
                            title_font = 'assets/fonts/futuralightc.otf')
