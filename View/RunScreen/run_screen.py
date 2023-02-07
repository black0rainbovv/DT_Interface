from View.base_screen import BaseScreenView
from View.RunScreen.components import CircularProgressBar

from kivy.clock import Clock


class RunScreenView(BaseScreenView):
    '''Implements the login start screen in the user application.'''

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.ids.maintopbar.title = self.app.serial_number
        self._progress_bar = self.ids.layout.children[0]

    def model_is_changed(self) -> None:

        '''
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        '''
        
    def on_enter(self, *args):
        """
        Event called when the screen is displayed: the entering animation is
        complete.
        """ 
        print(self.ids.layout.children[0].set_norm_value(1))
        # Clock.schedule_interval(self.animate, 0.05)

    def animate(self, dt):
        for bar in self._progress_bar:
            if bar.value < bar.max:
                bar.value += 1
            else:
                bar.value = bar.min

        bar = self._progress_bar
        if bar.value < bar.max:
            bar.value_normalized += 0.01
        else:
            bar.value_normalized = 0

    

