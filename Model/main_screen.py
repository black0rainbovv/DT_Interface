from Model.base_model import BaseScreenModel
from Model.device_communication import Device
from threading import Thread
from time import sleep


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    def __init__(self) -> None:
        super().__init__()
        self._observers = []
        self.device_status = ''
        self.tb_temperature = []
        self._device = Device()
        self._screen_is_active = True

    @property
    def screen_is_active(self):
        return self._screen_is_active

    @screen_is_active.setter
    def screen_is_active(self, state):
        self._screen_is_active = state

    def get_device_serial_number(self):
        return self._device.get_serial_number()

    def start_device_status_thread(self):
        Thread(target=self.device_info).start()

    def device_info(self):
        try:
            while self._screen_is_active:
                self.tb_temperature = self._device.get_tb_temperature()
                sleep(0.05)
                self.device_status = self._device.get_device_status()
                self.notify_observers('main screen')

        except Exception():
            if self._screen_is_active:
                self.start_device_status_thread()

    def tb_movement(self):
        self._device.open_close_tb()

    def run_last_prog(self):
        return self._device.start_run()
