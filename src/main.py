from kivy.app import App
from kivy.properties import StringProperty
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
from kivy.uix.image import Image
from kivy.uix.behaviors.button import ButtonBehavior


from src.create_db import create_db
from src.helpers import switch_page
from src.turn import TurnManager
from settings import SC_PATH

import sqlite3


conn = sqlite3.connect("evo.db")
cursor = conn.cursor()


class CustomScreen(Screen):
    """Screen with custom abilities"""

    def __lt__(self, other):
        return self.name < other.name


class InnerBiomeGrid(ButtonBehavior, GridLayout):
    """Custom grid for biomes"""

    biome_id = ObjectProperty('biom_id')
    sm = ObjectProperty('sm')


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
        main_screen = CustomScreen(name='main')
        biom_screen = CustomScreen(name='biom')
        supply_screen = CustomScreen(name='supply')
        self.biom_grid = GridLayout(cols=2)
        self.unremovable_screens = sorted([
            main_screen, biom_screen, supply_screen
        ])
        main_screen.add_widget(Button(text='main'))
        biom_screen.add_widget(self.biom_grid)
        popup = Popup(title='Test popup',
                      content=Label(text='Hello world'),
                      size_hint=(None, None))
        supply_screen.add_widget(Button(text='supply', on_press=popup.open))
        self.sm.add_widget(main_screen)
        self.sm.add_widget(biom_screen)
        self.sm.add_widget(supply_screen)

        to_biom = Button(text='to biom',
                         on_press=lambda *args: switch_page(self.sm, biom_screen.name))

        to_main = Button(text='to main',
                         on_press=lambda *args: switch_page(self.sm, main_screen.name))

        to_supply = Button(text='to supply',
                           on_press=lambda *args: switch_page(self.sm, supply_screen.name))
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

    def make_turn(self, button):
        data = TurnManager.make_turn()
        self.biom_grid.clear_widgets()
        if sorted(self.sm.screens) != self.unremovable_screens:
            self.sm.clear_widgets(
                screens=[sc for sc in self.sm.screens if sc not in self.unremovable_screens]
            )
        for item in data:
            biome_id = item.pop('biome_id')
            inner_grid = InnerBiomeGrid(
                rows=2, padding=5, biome_id=biome_id, sm=self.sm,
                on_press=lambda obj: switch_page(self.sm, f'b{obj.biome_id}')
            )
            biome_screen = CustomScreen(name=f'b{biome_id}')
            biome_screen.add_widget(Button(text=f'b{biome_id}'))
            self.sm.add_widget(biome_screen)

            for data_item in item:
                bl = BoxLayout()
                bl.add_widget(Image(source=f'{SC_PATH}/{data_item}.png', size_hint=(1, 1),))
                bl.add_widget(Label(text=str(item[data_item])))
                inner_grid.add_widget(bl)
            self.biom_grid.add_widget(inner_grid)


if __name__ == "__main__":
    MainApp().run()
