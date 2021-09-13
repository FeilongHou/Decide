from kivy.app import App
from kivy.config import Config
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, ColorProperty, Clock
import random


Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '812')

class Menu(BoxLayout):
    choice1 = StringProperty("")
    choice2 = StringProperty("")
    choice3 = StringProperty("")
    choice4 = StringProperty("")
    choice5 = StringProperty("")
    choice6 = StringProperty("")
    choice7 = StringProperty("")
    choice8 = StringProperty("")

    color = [True, False, False, False, False, False, False, False,]

    dark_red = (127/255, 30/255, 4/255, 1)
    light_red = (.957, .267, .18, 1)
    dark_yellow = (251/255, 123/255, 0, 1)
    light_yellow = (253/255, 241/255, 41/255, 1)
    
    b1 = ColorProperty(dark_red)
    b2 = ColorProperty(dark_yellow)
    b3 = ColorProperty(dark_red)
    b4 = ColorProperty(dark_yellow)
    b5 = ColorProperty(dark_yellow)
    b6 = ColorProperty(dark_red)
    b7 = ColorProperty(dark_yellow)
    b8 = ColorProperty(dark_red)

    run_speed = 0.15
    accelerate = True
    max_iter = random.randrange(20,60)
    iteration = 0

    select = SoundLoader.load("sound/select.mp3")
    spin = SoundLoader.load("sound/spin.mp3")
    spin.volume = 0.3
    result = SoundLoader.load("sound/result.mp3")

    def rotate(self):
        self.spin.play()

        def change_color(dt):
            if self.color[0]:
                self.color[0] = False
                self.color[1] = True
                self.ids.c4.color = self.dark_red
                self.ids.c1.color = self.light_yellow
                self.b1 = self.light_red
                self.b4 = self.dark_yellow

            elif self.color[1]:
                self.color[1] = False
                self.color[2] = True
                self.ids.c1.color = self.dark_yellow
                self.ids.c2.color = self.light_red
                self.b1 = self.dark_red
                self.b2 = self.light_yellow

            elif self.color[2]:
                self.color[2] = False
                self.color[4] = True
                self.ids.c2.color = self.dark_red
                self.ids.c3.color = self.light_yellow
                self.b2 = self.dark_yellow
                self.b3 = self.light_red


            elif self.color[3]:
                self.color[3] = False
                self.color[0] = True
                self.ids.c6.color = self.dark_yellow
                self.ids.c4.color = self.light_red
                self.b6 = self.dark_red
                self.b4 = self.light_yellow


            elif self.color[4]:
                self.color[4] = False
                self.color[7] = True
                self.ids.c3.color = self.dark_yellow
                self.ids.c5.color = self.light_red
                self.b3 = self.dark_red
                self.b5 = self.light_yellow


            elif self.color[5]:
                self.color[5] = False
                self.color[3] = True
                self.ids.c7.color = self.dark_red
                self.ids.c6.color = self.light_yellow
                self.b7 = self.dark_yellow
                self.b6 = self.light_red


            elif self.color[6]:
                self.color[6] = False
                self.color[5] = True
                self.ids.c8.color = self.dark_yellow
                self.ids.c7.color = self.light_red
                self.b8 = self.dark_red
                self.b7 = self.light_yellow


            elif self.color[7]:
                self.color[7] = False
                self.color[6] = True
                self.ids.c5.color = self.dark_red
                self.ids.c8.color = self.light_yellow
                self.b5 = self.dark_yellow
                self.b8 = self.light_red

            self.iteration += 1
            if self.iteration >= self.max_iter:
                Clock.unschedule(change_color)
                self.iteration = 0
                self.result.play()
                if Menu.color[0]:
                    show_result(self.ids.c4.text) 
                    
                elif Menu.color[1]:
                    show_result(self.ids.c1.text)

                elif Menu.color[2]:
                    show_result(self.ids.c2.text)

                elif Menu.color[3]:
                    show_result(self.ids.c6.text)

                elif Menu.color[4]:
                    show_result(self.ids.c3.text)

                elif Menu.color[5]:
                    show_result(self.ids.c7.text)

                elif Menu.color[6]:
                    show_result(self.ids.c8.text)

                else:
                    show_result(self.ids.c5.text)
    

        Clock.schedule_interval(change_color, self.run_speed)

    def clear_all(self):
        self.choice1 = ""
        self.choice2 = ""
        self.choice3 = ""
        self.choice4 = ""
        self.choice5 = ""
        self.choice6 = ""
        self.choice7 = ""
        self.choice8 = ""
        self.b1 = self.dark_red
        self.b2 = self.dark_yellow
        self.b3 = self.dark_red
        self.b4 = self.dark_yellow
        self.b5 = self.dark_yellow
        self.b6 = self.dark_red
        self.b7 = self.dark_yellow
        self.b8 = self.dark_red
        self.select.play()

    def on_food_press(self, food):
        self.select.play()     
        if not self.choice1:
            self.choice1 = food.text
        elif not self.choice2:
            self.choice2 = food.text
        elif not self.choice3:
            self.choice3 = food.text
        elif not self.choice4:
            self.choice4 = food.text
        elif not self.choice5:
            self.choice5 = food.text
        elif not self.choice6:
            self.choice6 = food.text
        elif not self.choice7:
            self.choice7 = food.text
        elif not self.choice8:
            self.choice8 = food.text

class Choices(StackLayout):
    def __init__(self, **kwargs):
        super(Choices, self).__init__(**kwargs)



def show_result(food):
    class result(FloatLayout):
        choice = StringProperty(food)
    
    show = result()
    popupWindow = Popup(title="Bon Appétit", title_size = 20, content = show, size_hint = (0.8, 0.6))
    popupWindow.open()
    


class DecideApp(App):
    def build(self):
        return Menu()

if __name__ == "__main__":
    DecideApp().run()