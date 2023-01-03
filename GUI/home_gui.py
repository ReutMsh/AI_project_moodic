from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label

from emotion.find_emotion import scanning_emotion

from kivy.core.window import Window

Window.size = (1000/3, 1749/3)

class homeApp(App):
    def build(self):
        self.icon = "green_logo.jpeg"

        main_layout = FloatLayout()



        self.background = Image(source = "welcome.jpeg")
        main_layout.add_widget(self.background)

        self.emotion_label = Label(text="",
                                   pos_hint={"center_x": .5, "center_y": .51},
                                   font_size = 40, font_name = "Academy Engraved LET Plain")
        main_layout.add_widget(self.emotion_label)

        self.button = Button(
            pos_hint={"center_x": .49, "center_y": .209},
            size_hint =(0.5, 0.081),
            background_color="grey",
            opacity = 1,
        )

        self.button.bind(on_press=self.start)
        #self.button.bind(on_press=self.next_func)

        main_layout.add_widget(self.button)
        '''

        self.button = Button(
            pos_hint= {"center_x": .5, "center_y": .5},
            background_color="red"
        )

        self.button.bind(on_press= self.func())  # TODO: build func

        main_layout.add_widget(self.button)

        self.background = Image(source = "logo.jpg")#TODO: put the real image

        main_layout.add_widget(self.background)
'''
        return main_layout

    def start(self, instance):
        self.background.source = "scan.jpeg"
        self.button.bind(on_press=self.next_func)
        self.button.pos_hint = {"center_x": .5, "center_y": .47}
        self.button.size_hint = (0.5,0.3)

        return self

    def next_func(self, instance):
        self.emotion = scanning_emotion()

        self.button.bind(on_press=self.next_func)
        self.button.pos_hint = {"center_x": .51, "center_y": .196}
        self.button.size_hint = (0.49, 0.0775)

        self.background.source = "try_again.jpeg"
        self.emotion_label.text= self.emotion

        return self

if __name__ == "__main__":
    app = homeApp()
    app.run()
