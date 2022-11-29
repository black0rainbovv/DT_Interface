from time import sleep
from kivy.clock import Clock

from View.base_screen import BaseScreenView

import serial

    
class EditScreenView(BaseScreenView):
    """Implements the edit start screen in the user application."""
    can = serial.Serial()
    can.baudrate = 115200
    can.timeout = 0.5
    can.port = 'COM11'

    motor_cmd = (b'hopen\r', b'hclose\r')
    motor_state = 0

    box_ids = []
    prog_cmd = []
    box_number = 1

    def callback(self, instance):
        if instance.icon == 'plus-circle-outline':
            self.add_step()
        if instance.icon == 'minus-circle-outline':
            self.remove_step()
        if instance.icon == 'arrow-up-drop-circle-outline':
            self.open_close()
        if instance.icon == 'power':
            quit()

    def read_number(self):
        self.can.open()

        self.can.write(b'$2\r')
        self.can.write(b'FSN\r')
        data = self.can.read_until(expected='\x00')
        self.can.write(b'$$\r')

        self.can.close()

        serial_number = data[4:10]

        return serial_number.decode('UTF-8')

    def open_close(self):
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

    def add_step(self):
        self.box_ids.append(f'box_{self.box_number}')
        self.ids[f'box_{self.box_number}'].disabled = False
        self.ids[f'box_{self.box_number}'].opacity = '1'
        self.ids[f'box_{self.box_number}'].size_hint_X = 'None'
        self.box_number += 1


    def remove_step(self):
        if len(self.box_ids) != 0:
            self.box_ids.reverse()    
            self.ids[self.box_ids[0]].disabled = True
            self.ids[self.box_ids[0]].opacity = '0'
            self.ids[self.box_ids[0]].size_hint_X = '0'
            self.box_ids.remove(self.box_ids[0])
            self.box_number -= 1
            self.box_ids.reverse()

    def launch_prog(self):
        self.can.open()
        self.can.write(b'$3\r')
        self.can.write(b'XPRG 0 35 0\r')
        self.prog_cmd = self.get_steps()

        for counter, number in enumerate(range(len(self.prog_cmd)), start=1):
            cm = self.prog_cmd[number] + '\r'
            self.can.write(bytes(cm, 'UTF-8'))
            data = self.can.read_until(expected='\x00')
            if counter % 2 == 0 and counter >= 2:
                self.can.write(b'XCYC 5\r')

        # self.can.write(b'XHLD\r')
        # data = self.can.read_until(expected='\x00')
        self.can.write(b'XSAV Test_Run\r')
        sleep(3)
        data = self.can.read_until(expected='\x00')
        self.can.write(b'RN\r')
        data = self.can.read_until(expected='\x00')
        self.can.write(b'$$\r')

        self.can.close()

        data = data.decode('UTF-8')
        rn_answer = data[3:4]
        print('Run: ', rn_answer)

        if int(rn_answer) == 0:
            self.switch_screen('run screen')

    def get_steps(self):
        temp_0 = self.ids['temp_field_0'].text
        time_0 = self.ids['time_field_0'].text
        self.prog_cmd.append(self.create_command(temp_0, time_0))

        for number in range(len(self.box_ids)):
            box_id = self.box_ids[number]
            if self.ids[box_id].opacity == 1:
                box_temp = self.ids[box_id].children[1].text
                box_time = self.ids[box_id].children[0].text
                self.prog_cmd.append(self.create_command(box_temp, box_time))

        return self.prog_cmd


    def create_command(self, temp, time):
        return f'XLEV {temp}00 {time} 0 0 0 0'

    # def xgs_cmd(self):
    #     self.can.open()

    #     self.can.write(b'$3\r')
    #     self.can.write(b'XGS\r')
    #     data = self.can.read_until(expected='\x00')
    #     self.can.write(b'$$\r')

    #     self.can.close()

    #     data = data.decode('UTF-8')
    #     data = data.split(' ')
    #     return data[0][4:]
