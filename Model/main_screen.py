from Model.base_model import BaseScreenModel
from Model.device_communication import Device
from kivy.clock import Clock
from threading import Thread
from time import sleep

import serial


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """
    communication = Device()
    can = serial.Serial()
    can.baudrate = 115200
    can.timeout = 0.5
    can.port = 'COM11'

    temperature_controller = '3'
    motor_controller = '4'
    optical_controller = '2'
    display_controller = '5'

    motor_cmd = (b'hopen\r', b'hclose\r')
    motor_state = 0

    def read_device_number(self):
        ser_num = self.communication.can_message('FSN', self.optical_controller)
        return ser_num[4:10]

    def read_device_status(self, *args):
        data = self.communication.can_message('RDEV', self.temperature_controller)
        data = data[4:6]
        
        return int(data) == 5

    def open_close_thermalblock(self):
        self.can.open()

        self.can.write(b'$4\r')

        data = int.from_bytes(self.can.read(1), 'big', signed=True)

        if data != 1:
            self.can.write(b'$$\r')
            data = self.can.read(1)

        self.can.write(self.motor_cmd[self.motor_state])
        self.motor_state = (self.motor_state + 1) % len(self.motor_cmd)

        data = self.can.read_until(expected='\x00')

        self.can.write(b'$$\r')
        data = self.can.read(1)
        self.can.close()

    def run_last(self):
        answer = self.communication.can_message('RN', self.temperature_controller)
        sleep(3)
        # print(answer)
        answer = answer[4:6]
        # print(int(answer))
        if answer == '0':
            return True
