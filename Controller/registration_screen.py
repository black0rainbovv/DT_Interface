from View.RegistrationForm.registration_screen import RegistrationScreenView


class RegistrationScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.login_screen.LoginScreenModel
        self.view = RegistrationScreenView(controller=self, model=self.model)

    def get_view(self) -> RegistrationScreenView:
        return self.view

    def registration_user(self, user_name: str, user_password: str, user_second_pasword: str):
        if self.password_verification(user_password, user_second_pasword):
            if self.model.user_registration(user_name, user_password):
                return True

    def password_verification(self, user_password, user_second_pasword):
        return user_password == user_second_pasword and len(user_password) != 0

