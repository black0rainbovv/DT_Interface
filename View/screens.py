# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController
from Model.setting_screen import SettingScreenModel
from Controller.setting_screen import SettingScreenController
from Model.about_device_screen import AboutDeviceScreenModel
from Controller.about_device_screen import AboudDeviceController
from Model.registration_screen import RegistrationScreenModel
from Controller.registration_screen import RegistrationScreenController
from Model.getting_started_screen import GettingStartedModel
from Controller.gettin_started_screen import GettingStartedController

screens = {
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },

    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController
    },

    "setting screen": {
        "model": SettingScreenModel,
        "controller": SettingScreenController
    },

    "about device screen": {
        "model": AboutDeviceScreenModel,
        "controller": AboudDeviceController
    },

    "registration screen": {
        "model": RegistrationScreenModel,
        "controller": RegistrationScreenController
    },

    "getting started screen": {
        "model": GettingStartedModel,
        "controller": GettingStartedController
    }
}