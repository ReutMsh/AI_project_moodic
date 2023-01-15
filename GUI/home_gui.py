from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from UserException import OpenCameraException, noAvailableDevice, noSpotifyPremium, noActiveDevice
from emotion.find_emotion import scanning_emotion
from spotify.search_in_spotify import search_in_spotify

Window.size = (1000 / 3, 1749 / 3)  # defining the size of our application
GUI_PATH = "GUI\\"

class HomeApp(App):
    """
    A class that generates and represents the Moodic application
    """
    # region build function
    def build(self):
        self.icon = GUI_PATH + "green_logo.jpeg"  # define the logo of the application

        # generating the main layout of the application
        main_layout = FloatLayout()

        # region image for background
        self.background = Image(source= GUI_PATH + "welcome.jpeg")
        main_layout.add_widget(self.background)
        # endregion

        # region text settings for the emotion label
        self.emotion_label = Label(text="",
                                   pos_hint={"center_x": .5, "center_y": .51},
                                   font_size=40, font_name=GUI_PATH + "Academy Engraved LET Plain")
        main_layout.add_widget(self.emotion_label)
        # endregion

        # region button try again
        # primary settings
        self.try_again_button = Button(
            pos_hint={"center_x": .712, "center_y": .203},
            size_hint=(0.32, 0.067),
            background_color="black",
            background_normal='',
            opacity=0,
            disabled=True
        )
        self.try_again_button.bind(on_press =self.try_again_to_find_emotion)
        main_layout.add_widget(self.try_again_button)
        # endregion

        # region button transferring to spotify
        # primary settings
        self.transferring_button = Button(
            pos_hint={"center_x": .27, "center_y": .205},
            size_hint=(0.32, 0.07),
            background_color="black",
            background_normal='',
            opacity=0,
            disabled=True
        )
        self.transferring_button.bind(on_press=self.transferring_view_to_spotify, on_release=self.start_spotify)
        main_layout.add_widget(self.transferring_button)
        # endregion

        # region set a button for switching view and stages in the application
        # primary settings
        self.switch_view_button = Button(
            pos_hint={"center_x": .49, "center_y": .209},
            size_hint=(0.5, 0.081),
            background_color="black",
            background_normal='',
            opacity=0
        )
        self.switch_view_button.bind(on_press=self.sign_in)
        main_layout.add_widget(self.switch_view_button)
        # endregion

        # region emotion image
        self.emotion_image = Image(source=GUI_PATH + "emojy\clear.png")
        main_layout.add_widget(self.emotion_image)
        # endregion

        return main_layout
    # endregion

    # region sign_in
    def sign_in(self, instance):
        textScr = "please enter your moodic name:\n"
        box = BoxLayout()
        self.input_text = TextInput(multiline=False, width=200, height=28, pos=(10, 450))
        box.add_widget(self.input_text, index=1)

        self.myButton = Button(text="OK, start!")
        box.add_widget(self.myButton, index=0)
        popupExc = Popup(title="Sign In\n\n" + textScr + "\n\n\n", size_hint=(0.9, 0.35), size=(250, 250),
                         separator_height=0.05, separator_color="white", auto_dismiss=False)
        popupExc.content = box
        popupExc.open()
        self.myButton.bind(on_press=self.switch_open_win_to_scan_win, on_release=popupExc.dismiss)

        return self
    # endregion


    # region switch_openwin_to_scanwin
    def switch_open_win_to_scan_win(self, instance):
        # change view
        self.background.source =GUI_PATH + "scan.jpeg"
        # button update settings
        self.switch_view_button.bind(on_press =self.print_scanning, on_release=self.switch_scan_win_to_emotion_win)
        self.switch_view_button.pos_hint = {"center_x": .5, "center_y": .47}
        self.switch_view_button.size_hint = (0.5, 0.3)


        return self
    # endregion

    # region scan to emotion
    def print_scanning(self, instance):
        self.switch_view_button.opacity = 1
        self.switch_view_button.size_hint =(0.45, 0.25)
        self.switch_view_button.text = "Scanning..."
        self.switch_view_button.font_color = "white"
        return self
    # endregion

    # region switch_scan_win_to_emotion_win
    def switch_scan_win_to_emotion_win(self, instance):
        # scan emotion using the user's camera
        try:
            self.emotion = scanning_emotion()

        except OpenCameraException as ex:
            print(ex)
            myException = str(ex)
            popupExc = Popup(title="Error\n\n" + myException + "\n\n\n", size_hint=(None, None), size=(250, 250),
                             separator_height=0.05, separator_color="white", auto_dismiss=False)  # , title_align=)
            popupExc.content = Button(text="okay, I fixed it", on_press=popupExc.dismiss,
                                      on_release=self.try_again_to_find_emotion)
            popupExc.open()

            return self
        self.continue_switch_scan_win_to_emotion_win(instance)
    # endregion

    # region continue_switch_scan_win_to_emotion_win
    def continue_switch_scan_win_to_emotion_win(self, instance):
        # print the emotion result of the scan
        self.emotion_label.text = self.emotion

        # add emojy
        img = GUI_PATH + 'emojy\\' + self.emotion + '.png'
        self.emotion_image.source = img
        self.emotion_image.pos_hint = {"center_x": .51, "center_y": .360}
        self.emotion_image.size_hint = (0.4, 0.4)

        # change view
        self.background.source = GUI_PATH + "try_again.jpeg"

        # update switch_view button settings
        self.switch_view_button.disabled = True
        self.switch_view_button.opacity = 0

        # update try again button
        self.try_again_button.disabled = False

        # update the spotify button
        self.transferring_button.disabled = False

        return self
    # endregion

    # region try again
    def try_again_to_find_emotion(self, instance):
        # change background
        self.background.source = GUI_PATH + "scan.jpeg"

        # update switch_view_button
        self.switch_view_button.opacity = 0
        self.switch_view_button.size_hint = (0.5, 0.3)
        self.switch_view_button.disabled = False

        # update try again button
        self.try_again_button.disabled = True

        # update transferring button
        self.transferring_button.opacity = 0  # TODO: delete
        self.transferring_button.disabled = True

        # delete emojy
        self.emotion_image.source = GUI_PATH + "emojy\clear.png"

        # delete text
        self.emotion_label.text = ""
        return self
    # endregion

    # region transferring to spotify
    def transferring_view_to_spotify(self, instance):
        # clear previous view
        self.emotion_label.text = ""
        self.emotion_image.source = GUI_PATH + "emojy\clear.png"

        # update view
        self.background.source = GUI_PATH + "transferring_to_spotify.jpeg"

        # update try_again button
        self.try_again_button.disabled = True
        self.try_again_button.opacity = 0

        # update spotify button
        self.transferring_button.disabled = True
        self.transferring_button.opacity = 0

        return self

    def start_spotify(self, instance):
        """play spotify and close the application"""
        try:
            search_in_spotify(self.emotion, self.input_text.text)
        except noAvailableDevice as ex:
            print(ex)
            myException = str(ex)
            popupExc = Popup(title="Error\n\n" + myException + "\n\n\n", size_hint=(None, None), size=(250, 250),
                             separator_height=0.05, separator_color="white", auto_dismiss=False)
            popupExc.content = Button(text="okay, I fixed it", on_press=popupExc.dismiss,
                                      on_release=self.continue_switch_scan_win_to_emotion_win)
            popupExc.open()
            return self

        except noSpotifyPremium as ex:
            myException = str(ex)
            popupExc = Popup(title="Error\n\n" + myException + "\n\n\n", size_hint=(None, None), size=(250, 250),
                             separator_height=0.05, separator_color="white", auto_dismiss=False)
            popupExc.content = Button(text="okay, close moodic", on_press=popupExc.dismiss,
                                      on_release=self.stop)
            popupExc.open()
            return self


        except noActiveDevice as ex:
            myException = str(ex)
            popupExc = Popup(title="Error\n\n" + myException + "\n\n\n", size_hint=(None, None), size=(250, 250),
                             separator_height=0.05, separator_color="white", auto_dismiss=False)
            popupExc.content = Button(text="okay, I fixed it", on_press=popupExc.dismiss,
                                      on_release=self.continue_switch_scan_win_to_emotion_win)
            popupExc.open()
            return self


        except:
            myException = "Sorry, for unknown reason something went wrong\nPlease try again\n\n"
            popupExc = Popup(title="Error\n\n" + myException + "\n\n\n", size_hint=(None, None), size=(250, 250),
                             separator_height=0.05, separator_color="white", auto_dismiss=False)
            popupExc.content = Button(text="okay, I fixed it", on_press=popupExc.dismiss,
                                      on_release=self.continue_switch_scan_win_to_emotion_win)
            popupExc.open()
            return self

        self.stop()
    # endregion

'''
app = HomeApp()
app.run()'''

