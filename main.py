"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""
from kivy.config import Config

Config.set("graphics", "resizable", False)
Config.set("graphics", "height", "480")
Config.set("graphics", "width", "800")
# Config.set("graphics", "fullscreen", "1")
# Config.set("graphics", "borderless", "1")
Config.set('kivy', 'keyboard_mode', 'systemanddock')

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from View.screens import screens


class DtUiKivy(MDApp):
    user_login = None
    serial_number = None
    enable_animation = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = MDScreenManager()

    def build(self) -> MDScreenManager:
        self.generate_application_screens()
        # self.manager_screens.current = "login screen"
        return self.manager_screens

    def generate_application_screens(self) -> None:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """

        for name_screen in screens.keys():
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)


if __name__ == "__main__":
    DtUiKivy().run()
