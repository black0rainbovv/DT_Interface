from kivy.properties import ObjectProperty

from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import CardTransition

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.screen import MDScreen

from Utility.observer import Observer

class BaseScreenView(ThemableBehavior, MDScreen, Observer):
    """
    A base class that implements a visual representation of the model data.
    The view class must be inherited from this class.
    """

    controller = ObjectProperty()
    """
    Controller object - :class:`~Controller.controller_screen.ClassScreenControler`.

    :attr:`controller` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    model = ObjectProperty()
    """
    Model object - :class:`~Model.model_screen.ClassScreenModel`.

    :attr:`model` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    manager_screens = ObjectProperty()
    """
    Screen manager object - :class:`~kivymd.uix.screenmanager.MDScreenManager`.

    :attr:`manager_screens` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    SHIFT_Y = NumericProperty(dp(0))

    next_screen = None

    def __init__(self, **kw):
        super().__init__(**kw)
        # Often you need to get access to the application object from the view
        # class. You can do this using this attribute.
        self.app = MDApp.get_running_app()
        # Adding a view class as observer.
        self.model.add_observer(self)
        

    def on_enter(self, *args):
        """
        Event called when the screen is displayed: the entering animation is
        complete.
        """
        # SHIFT_Y=dp(140)
        # self.animation_bg_zoom()

        if not self.app.enable_animation:
            return

        animation = Animation(SHIFT_Y=dp(140), d=2, t="in_out_quart")
        animation.bind(on_complete=self.animation_bg_zoom_in)
        animation.start(self)

    def animation_bg_zoom_in(self, *args):
        Animation(
            height=self.ids.bg.height + self.SHIFT_Y, d=2, t="in_out_quart"
        ).start(self.ids.bg)

    def animation_bg_zoom_out(self, *args):
        if not self.app.enable_animation:
            self.manager_screens.current = self.next_screen
            return

        animation = Animation(height=self.ids.bg.height - self.SHIFT_Y, d=2, t="in_out_quart")
        animation.bind(on_complete=self.change_screen)
        animation.start(self.ids.bg)

    def change_screen(self, animation, animated_instance):
        self.manager.transition = CardTransition()
        self.manager_screens.current = self.next_screen

    def switch_screen(self, next):
        self.next_screen = next
        self.animation_bg_zoom_out()

    def set_animation(self, enable):
        self.app.enable_animation = enable