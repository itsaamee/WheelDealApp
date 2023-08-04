from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.lang import Builder
import sqlite3
from kivy.core.window import Window
from kivy.uix.button import Button

Builder.load_file('WheelApp.kv') 

Window.size = (500, 700)

class ParentScreen(Screen):
    def switch_to_page(self, text):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        if text == "Start":
            app.root.current = "welcome"
        elif text == "Types":
            app.root.current = "bike_types"
        elif text == "Size":
            app.root.current = "bike_size"
        elif text == "Tires":
            app.root.current = "bike_tires"
        elif text == "Lessons":
            app.root.current = "bike_lessons"
        elif text == "Cart":
            app.root.current = "cart"
    
    def go_back(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='right')
        app.root.current = 'home'


class HomePage(ParentScreen):

    def go_to_welcome_page(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'welcome'

    def go_to_register_page(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'register'

class RegisterPage(ParentScreen):

    def go_to_register_page(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'register'

class WelcomePage(ParentScreen):

    def go_to_bike_types(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'bike_types'

    def go_to_bike_lessons(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'bike_lessons'

class CustomBikes(ParentScreen):
    def go_to_bike_types(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'bike_types'

class BikeTypes(ParentScreen):
    def go_to_bike_size(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'bike_size'

class BikeSize(ParentScreen):
    def go_to_bike_tires(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'bike_tires'

class Tires(ParentScreen):
    def go_to_options(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'options'

class BikeOptions(ParentScreen):
    def go_to_cart(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'cart'


class PreBuiltBikes(ParentScreen):
    pass

class BikeLessons(ParentScreen):
    pass

class ShoppingCart(ParentScreen):
    pass


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomePage(name = "home"))
        sm.add_widget(RegisterPage(name = 'register'))
        sm.add_widget(WelcomePage(name='welcome'))
        sm.add_widget(BikeTypes(name='bike_types'))
        sm.add_widget(BikeSize(name='bike_size'))
        sm.add_widget(Tires(name='bike_tires'))
        sm.add_widget(BikeOptions(name = 'options'))
        sm.add_widget(BikeLessons(name='bike_lessons'))
        sm.add_widget(ShoppingCart(name= "cart"))

        sm.current = 'home'
        return sm


if __name__ == "__main__":
    MyApp().run()
