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

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for x in self._observers:
            x.model_is_changed()

    device = Device()
