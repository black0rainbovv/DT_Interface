from View.base_screen import BaseScreenView
from Model.main_screen import MainScreenModel
from kivy.clock import Clock
from time import sleep
from threading import Thread


import serial
import os


class MainScreenView(BaseScreenView):
    '''Implements the login start screen in the user application.'''
    # can = serial.Serial()
    # can.baudrate = 115200
    # can.timeout = 0.5
    # can.port = 'COM11'
    # motor_cmd = (b'hopen\r', b'hclose\r')
    # motor_state = 0

    main_screen_model = MainScreenModel()

    def __init__(self, **kw):
        super().__init__(**kw)
        global timer_status
        timer_status = Clock.schedule_interval(self.get_status, 2)
        
        

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
        # self.get_status()

    def open_close(self):
        self.main_screen_model.open_close_thermalblock()

    def callback(self, instance):
        if instance.icon == 'arrow-up-drop-circle-outline':
            self.open_close()
        if instance.icon == 'power':
            winpath = os.environ['windir']
            os.system(winpath + r'\system32\rundll32 user32.dll, LockWorkStation')

    def read_number(self):
        return self.main_screen_model.read_device_number()

    def run_last(self):
        # self.can.open()
        # self.can.write(b'$3\r')
        # self.can.write(b'RN\r')
        # data = self.can.read_until(expected='\x00')
        # self.can.write(b'$$\r')
        # sleep(3)
        # self.can.close()
        # self.switch_screen('run screen')     
        rn_answer = self.main_screen_model.run_last()
        if rn_answer == True:
            self.switch_screen('run screen') 

    def get_status(self, *args):
        if status := self.main_screen_model.read_device_status():
            self.ids['device_status'].text = 'Состояние прибора: готов'
            timer_status.cancel()
        else:
            self.ids['device_status'].text = 'Состояние прибора: прогрев'
        
