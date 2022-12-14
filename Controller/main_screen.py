from View.MainScreen.main_screen import MainScreenView

import serial

class MainScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = MainScreenView(controller=self, model=self.model)

    def get_view(self) -> MainScreenView:
        return self.view

    def get_serial_number(self):
        return self.model.get_device_serial_number()

    def get_device_status(self):
        self.model.start_device_status_thread()

    def tb_movement(self):
        self.model.tb_movement()

    def run_last_prog(self):
        return self.model.run_last_prog()

    def set_screen_is_active(self, state):
        self.model.screen_is_active = state
