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
        self.device_status = '1'
        self.tb_temperature = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for x in self._observers:
            x.model_is_changed()

    device = Device()

    def get_serial_number(self):
        return self.device.get_serial_number()

    def start_device_status_thread(self):
        Thread(target=self.device_readiness).start()
        Thread(target=self.device_tb_temperature).start()

    def device_readiness(self):
        try:
            while int(self.device_status) != 5:
                self.device_status = self.device.get_device_status()
                self.notify_observers()
                sleep(1)
            
        except ValueError:
            print('Model: ' ,ValueError)

    def device_tb_temperature(self):
        try:
            while True:
                self.tb_temperature = self.device.get_tb_temperature()
                self.notify_observers()
                sleep(1)

        except ValueError:
            print('Model: ' ,ValueError)

    def tb_movement(self):
        self.device.open_close_tb()

    def run_last_prog(self):
        return self.device.start_run()
