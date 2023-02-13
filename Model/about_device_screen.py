from Model.base_model import BaseScreenModel
from Model.device_communication import Device
from threading import Thread


class AboutDeviceScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.AboutDeviceScreen.AboutDeviceScreenView` class.
    """

    def __init__(self) -> None:
        super().__init__()
        self._observers = []
        self._device = Device()
        self.firmware_version = []
        self.tb_number = ''
        self.tb_type = ''
        self.runtime = ''
        self.serial_number = ''

    def start_device_survey(self):
        Thread(target=self.device_survey).start()

    def device_survey(self):
        self.firmware_version = self._get_firmware_verison()
        self.serial_number = self._get_device_serial_number()
        self.tb_number = self._get_tb_number()
        self.tb_type = self._get_tb_type()
        self.runtime = self._get_runtime()
        self.notify_observers('about device screen')

    def _get_device_serial_number(self):
        return self._device.get_serial_number()

    def _get_firmware_verison(self):
        return self._device.get_firmware_verison()

    def _get_tb_number(self):
        return self._device.get_tb_number()

    def _get_tb_type(self):
        return self._device.get_tb_type()

    def _get_runtime(self):
        return self._device.get_runtime()
