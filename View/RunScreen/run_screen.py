from View.base_screen import BaseScreenView

from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from View.RunScreen.components import CircularProgressBar


class RunScreenView(BaseScreenView):
    '''Implements the login start screen in the user application.'''

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.ids.maintopbar.title = self.app.serial_number
        self._progress_bar = self.ids.progress_bar
        self._all_time = 100
        self._passed_time = 0
        self._progress_bar.max = self._all_time
        self._progress_bar.value = self._passed_time

    def model_is_changed(self) -> None:

        '''
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        '''
        self._all_time = int(self.model.all_time)
        self._passed_time = int(self.model.passed_time)
        self._progress_bar.max = self._all_time
        try:
            self.ids.temperature.text = f'Температура термоблока: \
                {self.model.tb_temperature[0]}°C'
            self.ids.cycles.text = f'Циклов прошло: \
                {self.model.cycles}'
            self.ids.time_left.text = f'Времени осталось: \
                {self.model.time_left}'
        except Exception:
            print(Exception)

    def on_enter(self, *args):
        """
        Event called when the screen is displayed: the entering animation is
        complete.
        """
        self.set_screen_is_active(True)
        self.controller.start_device_survey()

        self.animation = Clock.schedule_interval(self.animate, 0.2)

    def set_screen_is_active(self, state):
        self.controller.set_screen_is_active(state)

    def stop_run(self):
        self.controller.stop_run()

    def animate(self, dt):
        if self._progress_bar.value < self._progress_bar.max:
            self._progress_bar.value = self._passed_time

        else:
            Clock.unschedule(self.animation)
            self.set_screen_is_active(False)

            content = Label(text='Программа закончила свое выполнение.\nЧтобы посмотреть результаты запустите DTmaster\nи прочитайте последний запуск в приборе.',
                            color='#F0FFFF',
                            pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            font_size='26sp',
                            font_name='assets/fonts/futuralightc.otf')

            popup = Popup(title='Информация', content=content,
                          pos_hint={'center_x': 0.5, 'center_y': 0.5},
                          size_hint=(0.7, 0.4),
                          background='assets/images/bg_3.png',
                          title_color='white',
                          title_size='28sp',
                          title_font='assets/fonts/futuralightc.otf')

            popup.open()
            self.switch_screen('main screen')
