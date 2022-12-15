from View.base_screen import BaseScreenView
from View.AboutDeviceScreen.components import AboutDeviceLabel
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class AboutDeviceScreenView(BaseScreenView):
    '''Implements the device info screen in the user application.'''

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.popup = Popup()

    def model_is_changed(self) -> None:

        '''
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        '''
        
        temp_verison, motor_version, optic_version = self.model.firmware_version

        self.ids.fver_temperature.text = f'Температурная прошивка: {temp_verison}'
        self.ids.fver_motor.text = f'Моторная прошивка: {motor_version}'
        self.ids.fver_optical.text = f'Оптическая прошивка: {optic_version}'

        self.ids.serial_number.text = f'Серийный номер: {self.model.serial_number}'
        self.ids.tb_number.text = f'Номер термоблока: {self.model.tb_number}'
        self.ids.tb_type.text = f'Тип термоблока: {self.model.tb_type}'
        self.ids.runtime.text = f'Время наработки: {self.model.runtime} ч.'
        self.popup.dismiss()
        
    def on_enter(self, *args):
        """
        Event called when the screen is displayed: the entering animation is
        complete.
        """ 
        if self.ids.serial_number.text == '':
            self.popup = Popup(title='Загрузка', 
                            content=Label(text='Пожалуйста, подождите.',
                                            color = "white",
                                            font_size = "28sp",
                                            font_name = "assets/fonts/futuralightc.otf"),
                            auto_dismiss=False,
                            pos_hint = {'center_x': 0.5,'center_y': 0.5},
                            size_hint = (0.4, 0.3),
                            background = 'assets/images/bg_3.png',
                            title_color = 'white',
                            title_size = '36sp',
                            title_font = 'assets/fonts/futuralightc.otf',)
            self.popup.open()

            self.controller.get_device_survey()
