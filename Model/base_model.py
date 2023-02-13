class BaseScreenModel:
    """Implements a base class for model modules."""

    def __init__(self) -> None:
        self.serial_number = ''

    _observers = []

    def add_observer(self, observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self, name_screen: str) -> None:
        """
        Method that will be called by the observer when the model data changes.

        :param name_screen:
            name of the view for which the method should be called
            :meth:`model_is_changed`.
        """

        for observer in self._observers:
            if observer.name == name_screen:
                observer.model_is_changed()
                break
