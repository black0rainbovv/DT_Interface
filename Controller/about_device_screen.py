from View.AboutDeviceScreen.about_device_screen import AboutDeviceScreenView

class AboudDeviceController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.settung_screen.SettingScreenModel
        self.view = AboutDeviceScreenView(controller=self, model=self.model)

    def get_view(self) -> AboutDeviceScreenView:
        return self.view
