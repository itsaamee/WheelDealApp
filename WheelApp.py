from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.lang import Builder
import sqlite3
from kivy.core.window import Window
from kivy.uix.button import Button

Builder.load_file('WheelApp.kv') 

Window.size = (500, 700)

class HomePage(Screen):

    def switch_to_page(self, text):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        if text == "Custom Bikes":
            app.root.current = "custom_bikes"
        elif text == "Pre-Built Bikes":
            app.root.current = "pre_built_bikes"
        elif text == "Bike Lessons":
            app.root.current = "bike_lessons"
        elif text == "My Cart":
            app.root.current = "cart"

    def go_to_welcome_page(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'welcome'

    def go_to_register_page(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'register'

class RegisterPage(Screen):
    def switch_to_page(self, text):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        if text == "Custom Bikes":
            app.root.current = "custom_bikes"
        elif text == "Pre-Built Bikes":
            app.root.current = "pre_built_bikes"
        elif text == "Bike Lessons":
            app.root.current = "bike_lessons"
        elif text == "My Cart":
            app.root.current = "cart"

    def go_to_register_page(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'register'

    def go_back(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='right')
        app.root.current = 'home'

    
class WelcomePage(Screen):
    def switch_to_page(self, text):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        if text == "Custom Bikes":
            app.root.current = "custom_bikes"
        elif text == "Pre-Built Bikes":
            app.root.current = "pre_built_bikes"
        elif text == "Bike Lessons":
            app.root.current = "bike_lessons"
        elif text == "My Cart":
            app.root.current = "cart"

    def go_to_custom_bikes(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'custom_bikes'

    def go_to_pre_built_bikes(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'pre_built_bikes'

    def go_to_bike_lessons(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'bike_lessons'


class CustomBikes(Screen):
    def switch_to_page(self, text):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        if text == "Custom Bikes":
            app.root.current = "custom_bikes"
        elif text == "Pre-Built Bikes":
            app.root.current = "pre_built_bikes"
        elif text == "Bike Lessons":
            app.root.current = "bike_lessons"
        elif text == "My Cart":
            app.root.current = "cart"

    def go_back(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='right')
        app.root.current = 'welcome'


class PreBuiltBikes(Screen):
    def switch_to_page(self, text):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        if text == "Custom Bikes":
            app.root.current = "custom_bikes"
        elif text == "Pre-Built Bikes":
            app.root.current = "pre_built_bikes"
        elif text == "Bike Lessons":
            app.root.current = "bike_lessons"
        elif text == "My Cart":
            app.root.current = "cart"

    def go_back(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='right')
        app.root.current = 'welcome'


class BikeLessons(Screen):
    def switch_to_page(self, text):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        if text == "Custom Bikes":
            app.root.current = "custom_bikes"
        elif text == "Pre-Built Bikes":
            app.root.current = "pre_built_bikes"
        elif text == "Bike Lessons":
            app.root.current = "bike_lessons"
        elif text == "My Cart":
            app.root.current = "cart"

    def go_back(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='right')
        app.root.current = 'welcome'

class ShoppingCart(Screen):
    def switch_to_page(self, text):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        if text == "Custom Bikes":
            app.root.current = "custom_bikes"
        elif text == "Pre-Built Bikes":
            app.root.current = "pre_built_bikes"
        elif text == "Bike Lessons":
            app.root.current = "bike_lessons"
        elif text == "My Cart":
            app.root.current = "cart"


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomePage(name = "home"))
        sm.add_widget(RegisterPage(name = 'register'))
        sm.add_widget(WelcomePage(name='welcome'))
        sm.add_widget(CustomBikes(name='custom_bikes'))
        sm.add_widget(PreBuiltBikes(name='pre_built_bikes'))
        sm.add_widget(BikeLessons(name='bike_lessons'))
        sm.add_widget(ShoppingCart(name= "cart"))

        sm.current = 'home'
        return sm


if __name__ == "__main__":
    MyApp().run()