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
        self.all_time: str
        self.passed_time: str
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
        self._screen_is_active = False
        sleep(2)
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
                self._device_survey()
        except Exception:
            if self._screen_is_active:
                self.start_device_status_thread()

    def _device_survey(self):
        self.tb_temperature = self._device.get_tb_temperature()
        self.cycles = self._device.get_cycles_passed()
        self.time_left = self._device.get_time_left()
        self.all_time = self._device.all_time
        self.passed_time = self._device.passed_time
        self.time_left = self.convert_to_preferred_format(int(self.time_left))
        self.notify_observers('run screen')
