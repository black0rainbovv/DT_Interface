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
        self.device_status = '0'

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
        Thread(target=self.device_status_thread).start()

    def device_status_thread(self):
        data = '1'
        try:
            while int(data) != 5:
                data = self.device.get_device_status()
                print('From device: ', data)
                self.device_status = data
                self.notify_observers()
                sleep(1)
            
        except ValueError:
            print('Model: ' ,ValueError)
