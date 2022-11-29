import serial

class Device():

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

    def can_message(self, message, controller):
        controller = str(f'${controller}\r')
        message = str(f'{message}\r')
        self.can.open()
        self.can.write(bytes(controller, 'UTF-8'))
        self.can.write(bytes(message, 'UTF-8'))
        data = self.can.read_until(expected='\x00')
        self.can.write(b'$$\r')
        self.can.close()
        return data.decode('UTF-8')

    def get_device_number(self):
        serial_number = self.can_message('FSN', self.optical_controller)
        return serial_number[4:10]

    def get_device_starus(self):
        device_status = self.can_message('RDEV', self.temperature_controller)
        return device_status[4:6]

    def get_tb_temperature(self):
        data = self.can_message('XM', self.temperature_controller)
        data = data[4:].split(' ')
        xm_answer = []

        for i in range(6):
            data_slice_1 = data[i][:2]
            data_slice_2 = data[i][2:]
            xm_answer.append(f'{data_slice_1}.{data_slice_2}')
        return xm_answer

    def get_heat_sink_temperature(self):
        data = self.can_message('XTP', self.temperature_controller)
        data = data[4:].split(' ')
        data = data[0]
        data_slice_1 = data[:2]
        data_slice_2 = data[2:]
        return f'{data_slice_1}.{data_slice_2}'

    def get_hot_lid_temperature(self):
        data = self.can_message('XTP', self.temperature_controller)
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
            data = self.can_message('FCEXP', self.optical_controller)
            data = data.split(' ')
            data = data[0][4:]
            expos = int(data) * 0.308
            expos_list.append(round(expos))
        return expos_list
    
    def get_tb_number(self):
        data = self.can_message('HRTY', self.temperature_controller)
        return data[4:]

    def get_tb_type(self):
        data = self.can_message('HRID', self.temperature_controller)
        return data[4:]

    def get_time_left(self):
        data = self.can_message('TI', self.temperature_controller)
        data.split(' ')
        return data[0][4:]

    def get_time_passed(self):
        data = self.can_message('TI', self.temperature_controller)
        data.split(' ')
        return data[1]

    def get_firmware_verison(self):
        temp_verison = self.can_message('FVER', self.temperature_controller)
        motor_version = self.can_message('FVER', self.motor_controller)
        optical_version = self.can_message('FVER', self.optical_controller)
        display_version = self.can_message('FVER', self.display_controller)
        return [temp_verison, motor_version, optical_version, display_version]

    def get_device_date(self):
        data = self.can_message('DATE', self.optical_controller)
        return data[4:]

    def get_device_time(self):
        data = self.can_message('TIME', self.optical_controller)
        return data[4:]

    def get_channel_count(self):
        data = self.can_message('FACS', self.optical_controller)
        return data[4:]

    def start_run(self):
        data = self.can_message('RN', self.temperature_controller)
        return data[4:]

    def stop_run(self):
        data = self.can_message('ST', self.temperature_controller)
        return data[4:]

    def open_tb(self):
        data = self.can_message('HOPEN', self.motor_controller)
        return data[4:]

    def close_tb(self):
        data = self.can_message('HCLOSE', self.motor_controller)
        return data[4:]

    def press_tb(self):
        data = self.can_message('HPRESS', self.motor_controller)
        return data[4:]

    def open_close_tb(self):
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
