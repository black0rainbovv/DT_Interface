import serial

from serial import SerialException


class Device():
    '''Executes the exchange of commands with the device.'''

    def __init__(self) -> None:
        self._can = serial.Serial()
        self._can.baudrate = 115200
        self._can.timeout = 0.5
        self._can.port = 'COM11'
        self._temperature_controller = '3'
        self._motor_controller = '4'
        self._optical_controller = '2'
        self._display_controller = '5'
        self._motor_cmd = (b'hopen\r', b'hclose\r')
        self._motor_state = 0

    def can_message(self, message, controller):
        controller = str(f'${controller}\r')
        message = str(f'{message}\r')
        try:
            return self._message_to_device(controller, message)
        except SerialException:
            print('Could not open port')
            return ''

    def _message_to_device(self, controller, message):
        self._can.open()
        self._can.write(bytes(controller, 'UTF-8'))
        self._can.write(bytes(message, 'UTF-8'))
        data = self._can.read_until(expected='\x00')
        self._can.write(b'$$\r')
        self._can.close()
        return data.decode('UTF-8')

    def get_serial_number(self):
        serial_number = self.can_message('FSN', self._optical_controller)
        return serial_number[4:10]

    def get_device_status(self):
        device_status = self.can_message('RDEV', self._temperature_controller)
        return device_status[4:6]

    def get_tb_temperature(self):
        data = self.can_message('XM', self._temperature_controller)
        data = data[4:].split(' ')
        xm_answer = []

        if len(data) > 2:
            data[5] = data[5][:4]

            for i in range(6):
                data_slice_1 = data[i][:2]
                data_slice_2 = data[i][2:]
                xm_answer.append(f'{data_slice_1}.{data_slice_2}')

        return xm_answer

    def get_heat_sink_temperature(self):
        data = self.can_message('XTP', self._temperature_controller)
        data = data[4:].split(' ')
        data = data[0]

        if len(data) > 2:
            data_slice_1 = data[:2]
            data_slice_2 = data[2:]
            return f'{data_slice_1}.{data_slice_2}'

    def get_hot_lid_temperature(self):
        data = self.can_message('XTP', self._temperature_controller)
        data = data[4:].split(' ')
        data = data[1]
        if len(data) == 5:
            data_slice_1 = data[:3]
            data_slice_2 = data[3:]
        else:
            data_slice_1 = data[:2]
            data_slice_2 = data[2:]

        return f'{data_slice_1}.{data_slice_2}'

    def get_expositions(self):
        expos_list = []
        for _ in range(6):
            data = self.can_message('FCEXP', self._optical_controller)
            data = data.split(' ')
            data = data[0][4:]
            expos = int(data) * 0.308
            expos_list.append(round(expos))
        return expos_list
    
    def get_tb_number(self):
        data = self.can_message('HRTY', self._temperature_controller)
        return data[4:]

    def get_tb_type(self):
        data = self.can_message('HRID', self._temperature_controller)
        return data[4:]

    def get_time_left(self):
        data = self.can_message('TI', self._temperature_controller)
        data.split(' ')
        return data[0][4:]

    def get_time_passed(self):
        data = self.can_message('TI', self._temperature_controller)
        data.split(' ')
        return data[1]

    def get_firmware_verison(self):
        temp_verison = self.can_message('FVER', self._temperature_controller)
        motor_version = self.can_message('FVER', self._motor_controller)
        optical_version = self.can_message('FVER', self._optical_controller)
        display_version = self.can_message('FVER', self._display_controller)
        return [temp_verison, motor_version, optical_version, display_version]

    def get_device_date(self):
        data = self.can_message('DATE', self._optical_controller)
        return data[4:]

    def get_device_time(self):
        data = self.can_message('TIME', self._optical_controller)
        return data[4:]

    def get_channel_count(self):
        data = self.can_message('FACS', self._optical_controller)
        return data[4:]

    def start_run(self):
        data = self.can_message('RN', self._temperature_controller)
        return data[4:]

    def stop_run(self):
        data = self.can_message('ST', self._temperature_controller)
        return data[4:]

    def open_tb(self):
        data = self.can_message('HOPEN', self._motor_controller)
        return data[4:]

    def close_tb(self):
        data = self.can_message('HCLOSE', self._motor_controller)
        return data[4:]

    def press_tb(self):
        data = self.can_message('HPRESS', self._motor_controller)
        return data[4:]

    def open_close_tb(self):
        self._can.open()
        self._can.write(b'$4\r')
        data = int.from_bytes(self._can.read(1), 'big', signed=True)

        if data != 1:
            self._can.write(b'$$\r')
            data = self._can.read(1)

        self._can.write(self._motor_cmd[self._motor_state])
        self._motor_state = (self._motor_state + 1) % len(self._motor_cmd)
        data = self._can.read_until(expected='\x00')
        self._can.write(b'$$\r')
        data = self._can.read(1)
        self._can.close()
