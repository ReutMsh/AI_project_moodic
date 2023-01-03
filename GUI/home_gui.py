from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window

from emotion.find_emotion import scanning_emotion

Window.size = (1000 / 3, 1749 / 3)  # defining the size of our application


class HomeApp(App):
    """
    A class that generates and represents the Moodic application
    """

    # region build function
    def build(self):
        self.icon = "green_logo.jpeg"  # define the logo of the application

        # generating the main layout of the application
        main_layout = FloatLayout()

        # region image for background
        self.background = Image(source="welcome.jpeg")
        main_layout.add_widget(self.background)
        # endregion

        # region text settings for the emotion label
        self.emotion_label = Label(text="",
                                   pos_hint={"center_x": .5, "center_y": .51},
                                   font_size=40, font_name="Academy Engraved LET Plain")
        main_layout.add_widget(self.emotion_label)
        # endregion

        # region set a button for switching view and stages in the application
        # primary settings
        self.switch_view_button = Button(
            pos_hint={"center_x": .49, "center_y": .209},
            size_hint=(0.5, 0.081),
            background_color="black",
            background_normal='',
            opacity=0.2,
        )
        self.switch_view_button.bind(on_press=self.switch_open_win_to_scan_win)
        main_layout.add_widget(self.switch_view_button)
        # endregion

        return main_layout
    # endregion

    # region switch_openwin_to_scanwin
    def switch_open_win_to_scan_win(self, instance):
        # change view
        self.background.source = "scan.jpeg"

        # button update settings
        self.switch_view_button.bind(on_press=self.switch_scan_win_to_emotion_win)
        self.switch_view_button.pos_hint = {"center_x": .5, "center_y": .47}
        self.switch_view_button.size_hint = (0.5, 0.3)

        return self
    # endregion

    # region switch_scan_win_to_emotion_win
    def switch_scan_win_to_emotion_win(self, instance):
        # scan emotion using the user's camera
        self.emotion = scanning_emotion()

        # update button settings
        self.switch_view_button.bind(on_press=self.switch_scan_win_to_emotion_win)
        self.switch_view_button.pos_hint = {"center_x": .51, "center_y": .196}
        self.switch_view_button.size_hint = (0.49, 0.0775)
        self.switch_view_button.opacity = 0.2
        # change view
        self.background.source = "try_again.jpeg"

        # print the emotion result of the scan
        self.emotion_label.text = self.emotion

        return self
    # endregion


HomeApp().run()
