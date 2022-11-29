from View.base_screen import BaseScreenView

import serial
import os


class MainScreenView(BaseScreenView):
    '''Implements the login start screen in the user application.'''       
        

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
        if instance.icon == 'power':
            winpath = os.environ['windir']
            os.system(winpath + r'\system32\rundll32 user32.dll, LockWorkStation')        
