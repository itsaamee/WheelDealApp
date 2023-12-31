from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.lang import Builder
import sqlite3
from kivy.core.window import Window
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRaisedButton
import bcrypt
from kivymd.uix.pickers import MDDatePicker


Builder.load_file('WheelApp.kv') 

Window.size = (500, 700)

# RTM-002
class ParentScreen(Screen):
    def switch_to_page(self, text):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left', duration = 0.2)
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
        app.root.transition = SlideTransition(direction='right', duration= 0.25)
        app.root.current = 'home'


class HomePage(ParentScreen):

    def go_to_welcome_page(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left', duration= 0.25)
        app.root.current = 'welcome'

    def go_to_register_page(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left', duration= 0.25)
        app.root.current = 'register'

# RTM-010, RTM-006
class RegisterPage(ParentScreen):

    def go_to_password_page(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left', duration= 0.25)
        app.root.current = 'password'

    def submit_to_db(self):
        # create db or connect to it
        conn = sqlite3.connect("database.db")
        
        #create the cursor
        cur = conn.cursor()

        data = {
            'first_name': self.ids.first.text,
            'last_name': self.ids.last.text,
            'email': self.ids.email.text,
            'street': self.ids.street.text,
            'house': self.ids.house.text,
            'city': self.ids.city.text,
            'state': self.ids.state.text,
            'zip': self.ids.zip.text,
            'billing_street': self.ids.billing_street.text,
            'billing_house': self.ids.billing_house.text,
            'billing_city': self.ids.billing_city.text,
            'billing_state': self.ids.billing_state.text,
            'billing_zip': self.ids.billing_zip.text
        }

        # add a record to the database
        cur.execute("""
            INSERT INTO customer_info VALUES (
                :first_name, 
                :last_name, 
                :email, 
                :street, 
                :house, 
                :city, 
                :state, 
                :zip, 
                :billing_street,
                :billing_house,
                :billing_city,
                :billing_state,
                :billing_zip
            )
            """, data)

        conn.commit()

        conn.close()

        # clear all the input fields
        self.ids.first.text = "" 
        self.ids.last.text = ""
        self.ids.email.text= ""
        self.ids.street.text= ""
        self.ids.house.text= ""
        self.ids.city.text= ""
        self.ids.state.text= ""
        self.ids.zip.text= ""
        self.ids.billing_street.text = ""
        self.ids.billing_house.text= ""
        self.ids.billing_city.text= ""
        self.ids.billing_state.text= ""
        self.ids.billing_zip.text= ""

    def same_as_shipping(self):
        self.ids.billing_street.text = self.ids.street.text
        self.ids.billing_house.text = self.ids.house.text
        self.ids.billing_city.text = self.ids.city.text
        self.ids.billing_state.text = self.ids.state.text
        self.ids.billing_zip.text = self.ids.zip.text

    def required_fields(self):
        if (
            self.ids.first.text == "" or
            self.ids.last.text == "" or
            self.ids.email.text == "" or
            self.ids.street.text == "" or
            self.ids.city.text == "" or
            self.ids.state.text == "" or
            self.ids.zip.text == "" or
            self.ids.billing_street.text == "" or
            self.ids.billing_city.text == "" or
            self.ids.billing_state.text == "" or
            self.ids.billing_zip.text == ""
        ):
            self.ids.reg_label.text = "Enter the Required Fields"
        else:
            self.ids.reg_proceed_button.disabled = False
            self.ids.reg_submit_button.disabled = True
            self.ids.reg_label.text = ""


class PasswordPage(ParentScreen):
    def go_to_welcome_page(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left', duration= 0.25)
        app.root.current = 'welcome'
    
    def account_creation_label(self):
        self.ids.success_label.text = "Account Created Successfully"
    
    def submit_creds_to_db(self):
        conn = sqlite3.connect("database.db")
        
        cur = conn.cursor()

        hashed_password = bcrypt.hashpw(self.ids.password.text.encode('utf-8'), bcrypt.gensalt())

        data = {
            'username': self.ids.username.text,
            'password': hashed_password
        }

        cur.execute("""
            INSERT INTO credentials (username, password) VALUES (:username, :password)
            """, data)

        conn.commit()
        conn.close()

        self.ids.username.text = ""
        self.ids.password.text = ""

    def required_fields_password(self):
        if (
            self.ids.password.text == "" or
            self.ids.confirmed_password.text == "" or
            self.ids.username.text == ""  
        ):
            self.ids.success_label.text = "Enter the Required Fields"
        # else:
           # self.ids.proceed_button.disabled = False
            #self.ids.submit_button.disabled = True
            #self.ids.success_label.text = ""
    
    def match_the_password(self):
        if self.ids.username.text != "":
            if self.ids.password.text != "" and self.ids.confirmed_password.text != "":
                if self.ids.password.text == self.ids.confirmed_password.text:
                    self.ids.success_label.text = "account confirmed"
                    self.submit_creds_to_db()
                    self.ids.proceed_button.disabled = False
                    self.ids.submit_button.disabled = True
                else:
                    self.ids.success_label.text = "passwords not a match. Try again."
                    self.ids.password.text = ""
                    self.ids.confirmed_password.text = ""
                    self.ids.proceed_button.disabled = True
            else:
                self.ids.success_label.text = "please enter a password"
        else: 
            self.ids.success_label.text = "please enter username"
        

    


class WelcomePage(ParentScreen):

    def go_to_bike_types(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left', duration= 0.25)
        app.root.current = 'bike_types'

    def go_to_bike_lessons(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left', duration= 0.25)
        app.root.current = 'bike_lessons'

# RTM-003
class BikeTypes(ParentScreen):
    def go_to_bike_size(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left', duration= 0.25)
        app.root.current = 'bike_size'

# RTM-003
class BikeSize(ParentScreen):
    def go_to_bike_tires(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left', duration= 0.25)
        app.root.current = 'bike_tires'

# RTM-003
class Tires(ParentScreen):
    def go_to_options(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left', duration= 0.25)
        app.root.current = 'options'

# RTM-003
class BikeOptions(ParentScreen):
    def go_to_cart(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left', duration= 0.25)
        app.root.current = 'cart'


class PreBuiltBikes(ParentScreen):
    pass

class BikeLessons(ParentScreen):
    
    def show_date_picker(self):
        date_picker = MDDatePicker()
        date_picker.bind(on_save=self.on_save)
        date_picker.open()

    def on_save(self, instance, value, date_range):
        app = App.get_running_app()
        shopping_cart_page = app.root.get_screen('cart') 
        shopping_cart_page.ids.lessons_in_cart.text =f"Lesson on {str(value)}"
        shopping_cart_page.ids.lesson_quantity.text ="   1"
        shopping_cart_page.ids.lesson_price.text ="$40"

    def go_to_cart_page(self):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left', duration= 0.25)
        app.root.current = 'cart'

    

# RTM-004
class ShoppingCart(ParentScreen):
    pass


class MyApp(MDApp):
    def build(self):

        # connect to db
        conn = sqlite3.connect("database.db")
        
        #create the cursor
        cur = conn.cursor()

        # create tables
        cur.execute("""CREATE TABLE if not exists customer_info(
            first_name text,
            last_name text,
            email text,
            street text,
            house_apt text,
            city text,
            state text,
            zip text,
            billing_street text,
            billing_house text,
            billing_city text,
            billing_state text,
            billing_zip text)
            """)
        
        cur.execute("""CREATE TABLE if not exists credentials(
            username text,
            password text
            )""")
        
        conn.commit()

        conn.close()

        sm = ScreenManager()
        sm.add_widget(HomePage(name = "home"))
        sm.add_widget(RegisterPage(name = 'register'))
        sm.add_widget(PasswordPage(name= "password"))
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
