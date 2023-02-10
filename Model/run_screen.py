from Model.base_model import BaseScreenModel

from Model.device_communication import Device

from threading import Thread
from time import sleep


class RunScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    def __init__(self) -> None:
        super().__init__()
        self._observers = []
        self._device = Device()
        self.tb_temperature = []
        self.cycles: str
        self.time_left: int
        self._screen_is_active = False

    @property
    def screen_is_active(self):
        return self._screen_is_active

    @screen_is_active.setter
    def screen_is_active(self, state):
        self._screen_is_active = state

    def start_device_status_thread(self):
        Thread(target=self.device_survey).start()

    def last_run(self):
        return self._device.start_run()

    def stop_run(self):
        self._device.stop_run()

    def convert_to_preferred_format(self, sec): 
        if sec == 0:
            sec = 1

        sec = sec % (24 * 3600)
        sec %= 3600
        minut = sec // 60
        sec %= 60
        return "%02d:%02d" % (minut, sec)

    def device_survey(self):
        try:
            while self._screen_is_active:
                self.tb_temperature = self._device.get_tb_temperature()
                self.time_left = self._device.get_time_left()
                self.time_left = self.convert_to_preferred_format(int(self.time_left))
                self.notify_observers('run screen')
        except Exception:
            self.start_device_status_thread()