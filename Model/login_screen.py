from Model.base_model import BaseScreenModel

import shelve


class LoginScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    def __init__(self) -> None:
        super().__init__()
        self._file = 'data.txt'
        self.data = shelve

    def login_user(self, user_name, user_password):
        if self.is_user_exests(user_name) and self.user_verification(
            user_name, user_password
        ):
            return True

    def user_verification(self, name, password):
        with self.data.open(self._file) as states:
            return states[name] == password

    def is_user_exests(self, user_name):
        with self.data.open(self._file) as states:
            return user_name in states
