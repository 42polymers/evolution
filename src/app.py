from kivy.app import App
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.stacklayout import StackLayout

from settings import SC_PATH
from src.create_db import create_db
from src.helpers import switch_page
from src.turn import TurnManager


# TODO: dev settings. delete before compiling
Config.set('graphics', 'width', '720')
Config.set('graphics', 'height', '1280')


class CustomScreen(Screen):
    """Screen with custom abilities"""

    def __lt__(self, other):
        return self.name < other.name


class CustomInnerGrid(ButtonBehavior, GridLayout):

    grid_id = ObjectProperty('grid_id')
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
        creatures_screen = CustomScreen(name='main')
        biomes_screen = CustomScreen(name='biom')
        supply_screen = CustomScreen(name='supply')
        self.biomes_grid = GridLayout(cols=2)
        self.creatures_grid = GridLayout(cols=2)
        biomes_screen.add_widget(self.biomes_grid)
        creatures_screen.add_widget(self.creatures_grid)
        self.unremovable_screens = sorted([
            creatures_screen, biomes_screen, supply_screen
        ])

        popup = Popup(title='Test popup',
                      content=Label(text='Hello world'),
                      size_hint=(None, None))
        supply_screen.add_widget(Button(text='supply', on_press=popup.open))
        self.sm.add_widget(creatures_screen)
        self.sm.add_widget(biomes_screen)
        self.sm.add_widget(supply_screen)

        to_biom = Button(text='to biom',
                         on_press=lambda *args: switch_page(self.sm, biomes_screen.name))

        to_creatures = Button(text='to_creatures',
                              on_press=lambda *args: switch_page(self.sm, creatures_screen.name))

        to_supply = Button(text='to supply',
                           on_press=lambda *args: switch_page(self.sm, supply_screen.name))
        make_turn_btn = Button(text='make_turn',
                               on_press=lambda *args: self.make_turn(*args))

        button_box.add_widget(make_turn_btn)
        button_box.add_widget(to_biom)
        button_box.add_widget(to_creatures)
        button_box.add_widget(to_supply)

        bl.add_widget(statistic_box)
        bl.add_widget(self.sm)
        bl.add_widget(button_box)
        return bl

    def make_turn(self, button):
        turn_data = TurnManager.make_turn()
        self.general_preparations()
        self.prepare_biomes(turn_data['biomes_data'])
        self.prepare_creatures(turn_data['creatures_data'])

    def general_preparations(self):
        # clearing updating widgets
        if sorted(self.sm.screens) != self.unremovable_screens:
            self.sm.clear_widgets(
                screens=[sc for sc in self.sm.screens if sc not in self.unremovable_screens]
            )
        self.biomes_grid.clear_widgets()
        self.creatures_grid.clear_widgets()

    def prepare_biomes(self, data):
        for item in data:
            self.biomes_grid.add_widget(
                self.create_inner_grid(item, 'b')
            )

    def prepare_creatures(self, data):
        for item in data:
            self.creatures_grid.add_widget(
                self.create_creature_grid(item, 'c')
            )

    def create_inner_grid(self, item, prefix):
        grid_id = item.pop('id')
        inner_grid = CustomInnerGrid(
            rows=2, padding=5, grid_id=grid_id, sm=self.sm,
            on_press=lambda obj: switch_page(self.sm, f'{prefix}{obj.grid_id}')
        )
        screen = CustomScreen(name=f'{prefix}{grid_id}')
        screen.add_widget(Button(text=f'{prefix}{grid_id}'))
        self.sm.add_widget(screen)

        for data_item in item:
            bl = BoxLayout()
            bl.add_widget(Image(source=f'{SC_PATH}/{data_item}.png', size_hint=(1, 1), ))
            bl.add_widget(Label(text=str(item[data_item])))
            inner_grid.add_widget(bl)
        return inner_grid

    def create_creature_grid(self, item, prefix):
        grid_id = item.pop('id')
        flag = item.pop('flag')
        inner_grid = CustomInnerGrid(
            rows=2, padding=5, grid_id=grid_id, sm=self.sm,
            on_press=lambda obj: switch_page(self.sm, f'{prefix}{obj.grid_id}')
        )
        screen = CustomScreen(name=f'{prefix}{grid_id}')
        bl = BoxLayout()
        left_part = BoxLayout()
        right_part = GridLayout(cols=3, padding=5)
        for i in range(30):
            right_part.add_widget(Button(
                text=f'{i}',
                size_hint_y=None,
            ))
        bl.add_widget(left_part)
        bl.add_widget(right_part)
        screen.add_widget(bl)
        self.sm.add_widget(screen)

        for data_item in item:
            bl = BoxLayout()
            bl.add_widget(Image(source=f'{SC_PATH}/mock.png', size_hint=(1, 1), ))
            bl.add_widget(Label(text=str(item[data_item])))
            inner_grid.add_widget(bl)
        return inner_grid