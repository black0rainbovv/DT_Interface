from View.RunScreen.run_screen import RunScreenView


class RunScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = RunScreenView(controller=self, model=self.model)

    def get_view(self) -> RunScreenView:
        return self.view

    def set_screen_is_active(self, state):
        self.model.screen_is_active = state

    def start_device_survey(self):
        self.model.start_device_status_thread()

    def tb_movement(self):
        self.model.tb_movement()

    def last_run(self):
        return self.model.last_run() == '0'

    def stop_run(self):
        self.model.stop_run()
