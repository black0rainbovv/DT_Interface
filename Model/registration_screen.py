from Model.base_model import BaseScreenModel

import shelve


class RegistrationScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    def __init__(self) -> None:
        super().__init__()
        self._observers = []
        self._file = 'data.txt'
        self.data = shelve
        

    def user_registration(self, user_name, user_password):
        if self.is_user_exests(user_name) == False:
            self.add_user(user_name, user_password)
            return True
            # self.notify_observers('registration screen')

    def is_user_exests(self, user_name):
        with self.data.open(self._file) as states:
            return user_name in states

    def add_user(self, user_name, user_password):
        with self.data.open(self._file) as states:
            states[user_name] = user_password