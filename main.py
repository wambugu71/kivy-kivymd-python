from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import phonenumbers 
from kivy.uix.label import Label
from kivymd.toast import toast
from kivy.uix.screenmanager import Screen
from phonenumbers import geocoder, carrier, timezone
from kivy.config import Config
#Config.set("graphics", "fullscreen", 0)
Builder.load_string('''                   
<inputme>:
    txtinput: txtinput
    mypast: mypast
    country: country
    carrier: carrier
    timezone: timezone
    info: info
    MDBoxLayout:
        orientation: 'vertical'
       # adaptive_size: True
        MDTopAppBar:
            title: "Phone number info"
            elevation: 4
            left_action_items: [["menu", lambda x: my_drawer.set_state("open")]]
            type: "top"
        MDNavigationLayout:
            ScreenManager:
                id: wambugu
                MDScreen:
                    name: "main"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTextField:
                            id: txtinput
                            hint_text: "Paste your number with country code here:"
                            mode: "rectangle"
                            icon_left: "account-search"
                            max_length: 13
                            pos_hint: {'center_x': 0.5,'center_y': 0.5}
                            multiline: False
                            mode: "round"
                            size_hint_x: .9
                        MDRectangleFlatIconButton:
                            hint_animation: True
                            icon:"cellphone-check"
                            text:"check info"
                            on_release: root.mypaste()
                            md_bg_color: "white"
                            pos_hint: {'center_x': 0.5,'center_y': 0.5}
                        MDCard:
                            size_hint: .8,.2
                            orientation: 'vertical'
                            padding: ('5dp', '5dp', '5dp', '5dp')
                            shadow_radius: 1
                            md_bg_color: "white"
                            adaptive_size: True
                            pos_hint: {'center_x': 0.5,'center_y': 0.5}
                            adaptive_size: True
                            MDTextField:
                                id: mypast
                                hint_text: "PHONE NUMBER INFO"
                                font_size: 18
                                icon_left: "account-check"
                                keyboard_mode: "managed"
                            MDTextField: 
                                id: country
                                hint_text: "COUNTRY"
                                font_size:18
                                icon_left: "home-map-marker"
                                keyboard_mode: "managed"
                            MDTextField:
                                id: carrier 
                                hint_text: "SERVICE PROVIDER"
                                font_size: 18
                                icon_left: "sim"
                                keyboard_mode: "managed"
                            MDTextField:
                                id: timezone
                                font_size: 18
                                icon_left: "timer-settings-outline"
                                hint_text: "TIME ZONE"
                                keyboard_mode: "managed"
                               # MDLabel:
                          #        text: "widh you good"
                       #           halign: "center"
                              
                          
                                
                MDScreen:
                    name: "information"
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDCard:
                            size_hint_x: .6
                            orientation: 'vertical'
                            padding: ('20dp', '20dp', '20dp', '20dp')
                            shadow_radius: 3
                            shadow_offset:0, 2
                            md_bg_color: "white"
                            pos_hint: {'center_x': 0.5,'center_y': 0.5}
                            MDLabel:
                                id: info
                                text: "info"
                                halign: "center"
                                
            MDNavigationDrawer: 
                id: my_drawer
                MDList:
                    TwoLineListItem:
                        text: "Main screen"
                        secondary_text: "Goto the main screen"
                        on_release: 
                            wambugu.current = "main"
                            my_drawer.set_state("close")
                    TwoLineListItem:
                        text: "Phone numbers info"
                        secondary_text: "informatin about phone numbers library"
                        on_release:
                            wambugu.current = "information"
                            my_drawer.set_state("close")
                            root.myinfo()
     ''') 

  
class inputme(Screen):
    dia = None
    def __init__(self):
        super(inputme, self).__init__()
    def mypaste(self):
        self.myphone = self.ids.txtinput.text
        if self.myphone=="":
            toast("Enter the phone number with the country code!")
        else: 
            try:
                phone_no_info= phonenumbers.parse(self.myphone)
                self.ids.mypast.text = str(phone_no_info)
                country_zone = geocoder.description_for_number(phone_no_info, "en")
                self.ids.country.text =f"{country_zone}"
                carrier_comp = carrier.name_for_number(phone_no_info, "en")
                self.ids.carrier.text = f"{carrier_comp}"
                time_zone = timezone.time_zones_for_number(phone_no_info)
                self.ids.timezone.text = f"{time_zone}"
            
            except:
                toast("Error")
                self.ids.mypast.text = "Error"
            
            
    def myinfo(self):
        self.ids.info.text = "Name: Wambugu kinyua\nContact: kenliz1738@gmail.com"
class MainActicityApp(MDApp):
    def build(self):
        toast("Made by ken")
        return inputme()

MainActicityApp().run()
