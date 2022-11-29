from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import CardTransition

from kivymd.uix.boxlayout import MDBoxLayout


class LoginHero(ButtonBehavior, MDBoxLayout):
    """Класс реализует виджет героя."""

    manager = ObjectProperty()  # объект менеджера экранов

    def animation_bg_out(self, *args):

        p = self.parent
        while p:
            if 'bg' in p.ids:
                break
            p = p.parent

        bg = p.ids.bg

        animation = Animation(
            height=bg.height - p.SHIFT_Y, d=2, t="in_out_quart"
        )
        animation.bind(on_complete=self.change_screen)
        animation.start(bg)

    def switch_screen(self):
        """Метод, который вызывается при тапе по виджету героя."""

        #self.animation_bg_out()
        #self.parent.on_pre_leave(self, *args)
        #self.change_screen()
        #self.manager.transition = CardTransition()
        #self.manager.current = "login screen"

        # Устанавливает имя текущего героя для экранного менеджера.
        # self.manager.current_hero = self.ids.hero.tag
        # Переключаем экран.
        # self.manager.current = "login screen"

    def change_screen(self, animation, animated_instance):
        # Устанавливает имя текущего героя для экранного менеджера.
        #self.manager.current_hero = self.ids.hero_from.tag
        # Переключаем экран.
        self.manager.transition = CardTransition()
        self.manager.current = "login screen"
        #self.manager.transition.direction = 'right'
