# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
from Model.edit_screen import EditScreenModel
from Controller.edit_screen import EditScreenController
from Model.settings_screen import SettingsScreenModel
from Controller.settings_screen import SettingsScreenController
from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController
from Model.run_screen import RunScreenModel
from Controller.run_screen import RunScreenController

screens = {
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },

    "edit screen": {
        "model": EditScreenModel,
        "controller": EditScreenController
    },

    "settings screen": {
        "model": SettingsScreenModel,
        "controller": SettingsScreenController
    },

    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController
    },

    "run screen": {
        "model": RunScreenModel,
        "controller": RunScreenController
    }

}