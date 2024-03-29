from View.GettingStartedScreen.getting_started_screen import GettingStartedView


class GettingStartedController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = GettingStartedView(controller=self, model=self.model)

    def get_view(self) -> GettingStartedView:
        return self.view

    def tb_movement(self):
        self.model.tb_movement()

    def last_run(self):
        status = self.model.last_run()
        if len(status) == 4:
            return True
        else:
            False
