from kivy.clock import Clock
from threading import Thread
from time import sleep
from View.base_screen import BaseScreenView


import serial



    
class RunScreenView(BaseScreenView):
    """Implements the run start screen in the user application."""
    can = serial.Serial()
    can.baudrate = 115200
    can.timeout = 0.5
    can.port = 'COM11'
    

    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self, *args):
        """
        Event called when the screen is displayed: the entering animation is
        complete.
        """
        self.ids['time_passed'].opacity = '1'
        self.ids['temperature_label'].opacity = '1'
        self.ids['run_box'].opacity = '0'
        th = Thread(target=self.start_timer())
        th.start()

    def read_number(self):
        self.ids['progress_bar'].start()
        self.can.open()

        self.can.write(b'$2\r')
        self.can.write(b'FSN\r')
        data = self.can.read_until(expected='\x00')
        self.can.write(b'$$\r')

        self.can.close()

        serial_number = data[4:10]

        return serial_number.decode('UTF-8')

    def stop_run(self):        
        self.can.open()

        self.can.write(b'$3\r')
        self.can.write(b'ST\r')
        self.can.write(b'$$\r')

        self.can.close()

        self.switch_screen('main screen')

    def update_data(self, *args):
        temperature = self.get_xm()
        self.ids['temperature_label'].text = f'Температура\nтермоблока: {temperature}°C'

        time_left = self.get_time()
        
        if int(time_left[0]) <= 0:
            self.stop_timer()
            self.ids['time_passed'].opacity = '0'
            self.ids['progress_bar'].stop()
            self.ids['run_box'].opacity = '1'
            self.ids['temperature_label'].opacity = '0'

        else:
            self.ids['time_passed'].text = f'Осталось времени:\n{time_left[0]} сек.'
            self.ids['time_left'].text = f'Времени прошло:\n{time_left[1]} сек.'

    def get_xm(self):
        self.can.open()
        self.can.write(b'$3\r')
        self.can.write(b'XM\r')
        data = self.can.read_until(expected='\x00')
        self.can.write(b'$$\r')
        self.can.close()

        data = data[4:6]
        return data.decode('UTF-8')

    def get_time(self):
        self.can.open()
        self.can.write(b'$3\r')
        self.can.write(b'TI\r')
        data = self.can.read_until(expected='\x00')
        self.can.write(b'$$\r')
        self.can.close()

        data = data.decode('UTF-8')
        data = data.split(' ')
        return [data[0][4:], data[1]]

    def start_timer(self):
        global timer
        timer = Clock.schedule_interval(self.update_data, 1)

    def stop_timer(self):
        timer.cancel()

    def exit_run(self):
        self.stop_run()
        self.switch_screen('main screen')
