from View.EditScreen.edit_screen import EditScreenView


class EditScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.edit_screen.EditScreenModel
        self.view = EditScreenView(controller=self, model=self.model)

    def get_view(self) -> EditScreenView:
        return self.view
