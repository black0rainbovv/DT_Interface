from View.base_screen import BaseScreenView


class MainScreenView(BaseScreenView):
    '''Implements the login start screen in the user application.'''

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.ids.maintopbar.title = self.controller.get_serial_number()
        self.controller.get_device_status()

    def model_is_changed(self) -> None:

        '''
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        '''
        status = self.model.device_status

        if int(status) == 5:
            self.ids.device_status.text = 'Состояние прибора: готов'
        else:
            self.ids.device_status.text = 'Состояние прибора: прогрев'
        
    def on_enter(self, *args):
        """
        Event called when the screen is displayed: the entering animation is
        complete.
        """ 

    def callback(self, instance):
        if instance.icon == 'power':
            quit()
