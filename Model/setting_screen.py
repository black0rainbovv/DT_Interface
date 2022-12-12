from Model.base_model import BaseScreenModel
from Model.device_communication import Device


class SettingScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    def __init__(self) -> None:
        super().__init__()
        self._observers = []

    device = Device()
