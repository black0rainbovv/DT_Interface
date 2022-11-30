from View.base_screen import BaseScreenView

import os


class MainScreenView(BaseScreenView):
    '''Implements the login start screen in the user application.'''

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.ids.maintopbar.title = self.model.set_serial_number()

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

    def callback(self, instance):
        # if instance.icon == 'power':
            pass
            # winpath = os.environ['windir']
            # os.system(winpath + r'\system32\rundll32 user32.dll, LockWorkStation') 
