from View.base_screen import BaseScreenView
from View.AboutDeviceScreen.components import AboutDeviceLabel


class AboutDeviceScreenView(BaseScreenView):
    '''Implements the device info screen in the user application.'''

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def model_is_changed(self) -> None:

        '''
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        '''

        # if self.controller.firmware_version[0] == '':
        #     self.controller.get_device_survey()
        # else:   
        temp_verison, motor_version, optic_version, display_version = self.model.firmware_version

        self.ids.fver_temperature.text = temp_verison
        self.ids.fver_motor.text = motor_version
        self.ids.fver_optical.text = optic_version
        self.ids.fver_display.text = display_version

        self.ids.serial_number.text = self.model.serial_number
        self.ids.tb_number.text = self.model.tb_number
        self.ids.tb_number.text = self.model.tb_type
        self.ids.runtime.text = f'{self.model.runtime} часов'
        
    def on_enter(self, *args):
        """
        Event called when the screen is displayed: the entering animation is
        complete.
        """ 
        self.controller.get_device_survey()
