from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView


from src.create_db import create_db
from src.turn import TurnManager

import sqlite3


conn = sqlite3.connect("evo.db")
cursor = conn.cursor()


class MainApp(App):

    def build(self):

        bl = BoxLayout(orientation='vertical')
        statistic_box = BoxLayout(size_hint=(1, .05))
        statistic_stack = StackLayout()
        for i in range(5):
            statistic_stack.add_widget(Button(text=str(i), size_hint=(.1, 1)))
        statistic_box.add_widget(statistic_stack)
        button_box = BoxLayout(size_hint=(1, .1))
        self.sm = ScreenManager(size_hint=(1, .85))
        main_screen = Screen(name='main')
        biom_screen = Screen(name='biom')
        supply_screen = Screen(name='supply')
        self.biom_grid = GridLayout(cols=2)
        # for i in range(10):
        #     biom_grid.add_widget(Button(text='hue'))
        main_screen.add_widget(Button(text='main'))
        # biom_screen.add_widget(Button(text='biom'))
        biom_screen.add_widget(self.biom_grid)
        # supply_screen.add_widget(Button(text='supply'))
        popup = Popup(title='Test popup',
                      content=Label(text='Hello world'),
                      size_hint=(None, None))
        supply_screen.add_widget(Button(text='supply', on_press=popup.open))
        self.sm.add_widget(main_screen)
        self.sm.add_widget(biom_screen)
        self.sm.add_widget(supply_screen)

        to_biom = Button(text='to biom',
                         on_press=lambda *args: self.switching_page(biom_screen.name))

        to_main = Button(text='to main',
                         on_press=lambda *args: self.switching_page(main_screen.name))

        to_supply = Button(text='to supply',
                           on_press=lambda *args: self.switching_page(supply_screen.name))
        make_turn = Button(text='make_turn',
                           on_press=self.make_turn)

        button_box.add_widget(make_turn)
        button_box.add_widget(to_biom)
        button_box.add_widget(to_main)
        button_box.add_widget(to_supply)

        bl.add_widget(statistic_box)
        bl.add_widget(self.sm)
        bl.add_widget(button_box)
        return bl

    def switching_page(self, destination):
        self.sm.current = destination

    def make_turn(self, button):
        data = TurnManager.make_turn()
        self.biom_grid.clear_widgets()
        for item in data:
            self.biom_grid.add_widget(Button(text=str(item)))


if __name__ == "__main__":
    MainApp().run()
