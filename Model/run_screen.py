from Model.base_model import BaseScreenModel

from Model.device_communication import Device


class RunScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    def __init__(self) -> None:
        super().__init__()
        self._observers = []
        self._device = Device()

    def tb_movement(self):
        self._device.open_close_tb()

    def last_run(self):
        return self._device.start_run()