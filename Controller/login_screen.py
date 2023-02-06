from View.LoginScreen.login_screen import LoginScreenView


class LoginScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.login_screen.LoginScreenModel
        self.view = LoginScreenView(controller=self, model=self.model)

    def get_view(self) -> LoginScreenView:
        return self.view

    def login_user(self, user_name, user_password):
        return self.model.login_user(str(user_name), str(user_password))
