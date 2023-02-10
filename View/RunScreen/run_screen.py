from View.base_screen import BaseScreenView
from View.RunScreen.components import CircularProgressBar

from kivy.clock import Clock


class RunScreenView(BaseScreenView):
    '''Implements the login start screen in the user application.'''

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.ids.maintopbar.title = self.app.serial_number
        self.progress_bar = self.ids.progress_bar

    def model_is_changed(self) -> None:

        '''
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        '''

        self.ids.temperature.text = f'Температура термоблока: {self.model.tb_temperature[0]}°C'
        self.ids.time_left.text = f'Времени осталось: {self.model.time_left}'
        
    def on_enter(self, *args):
        """
        Event called when the screen is displayed: the entering animation is
        complete.
        """ 
        self.set_screen_is_active(True)
        self.controller.start_device_survey()

        Clock.schedule_interval(self.animate, 0.2)

    def set_screen_is_active(self, state):
        self.controller.set_screen_is_active(state)

    def stop_run(self):
        self.controller.stop_run()

    def animate(self, dt):
        if self.progress_bar.value < self.progress_bar.max:
            self.progress_bar.value_normalized += 0.01
        else:
            self.progress_bar.value_normalized = 0
