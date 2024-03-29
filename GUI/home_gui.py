import sys

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from UserException import OpenCameraException, NoAvailableDevice, NoSpotifyPremium, NoActiveDevice
from emotion.emotion_detector import get_expressed_emotion
from spotify.activate_playlist_in_spotify import activate_emotion_based_playlist_in_spotify

Window.size = (1000 / 3, 1749 / 3)  # defining the size of our application

GUI_PATH = "GUI\\"
BACKGROUND_PATH = GUI_PATH + "background\\"
EMOJY_PATH = GUI_PATH + "emojy\\"
SIGN_IN_NAME = "\nPlease enter your moodic name:"


class HomeApp(App):
    """
    A class that generates and represents the Moodic application
    """

    # region build function
    def build(self):
        self.icon = BACKGROUND_PATH + "green_logo.jpeg"  # define the logo of the application

        # main layout of the application
        main_layout = FloatLayout()

        # region background
        self.background = Image(source=BACKGROUND_PATH + "welcome.jpeg")
        main_layout.add_widget(self.background)
        # endregion

        # region emotion-result label
        self.emotion_result_label = Label(text="",
                                          pos_hint={"center_x": .5, "center_y": .51},
                                          font_size=40,
                                          font_name=GUI_PATH + "Academy Engraved LET Plain")
        main_layout.add_widget(self.emotion_result_label)
        # endregion

        # region button try again
        self.try_again_button = Button(pos_hint={"center_x": .712, "center_y": .203},
                                       size_hint=(0.32, 0.067),
                                       background_color="black",
                                       background_normal='',
                                       opacity=0,
                                       disabled=True)
        self.try_again_button.bind(on_press=self.try_again_to_find_emotion)
        main_layout.add_widget(self.try_again_button)
        # endregion

        # region button transferring to spotify
        self.transferring_button = Button(pos_hint={"center_x": .27, "center_y": .205},
                                          size_hint=(0.32, 0.07),
                                          background_color="black",
                                          background_normal='',
                                          opacity=0,
                                          disabled=True)
        self.transferring_button.bind(on_press=self.transferring_to_spotify_layout,
                                      on_release=self.start_spotify)
        main_layout.add_widget(self.transferring_button)
        # endregion

        # region button switching view and stages in the application
        self.switch_view_button = Button(pos_hint={"center_x": .49, "center_y": .209},
                                         size_hint=(0.5, 0.081),
                                         background_color="black",
                                         background_normal='',
                                         opacity=0)
        self.switch_view_button.bind(on_press=self.sign_in_open_popup)
        main_layout.add_widget(self.switch_view_button)
        # endregion

        # region emotion image
        self.emotion_result_image = Image(source=EMOJY_PATH + "clear.png")
        main_layout.add_widget(self.emotion_result_image)
        # endregion

        return main_layout

    # endregion

    # region login options
    # region sign_in_open_popup
    def sign_in_open_popup(self, instance, message=""):
        """
        Define the sign in popup window and opening it.
        Including input box and 'sign in' button.
        """
        log_in_request = message + SIGN_IN_NAME

        # region popup layout
        popup_layout = BoxLayout(size_hint=(1, 1), orientation="vertical")

        self.exception_label = Label(text=log_in_request)
        popup_layout.add_widget(self.exception_label)

        self.username_input_text = TextInput(multiline=False,
                                             size_hint_y=.3)
        popup_layout.add_widget(self.username_input_text)

        self.exception_button = Button(text="Login",
                                       size_hint_y=.3)
        popup_layout.add_widget(self.exception_button)
        # endregion

        sign_in_popup = Popup(title="Sign In",
                              size_hint=(0.9, 0.5),
                              separator_color="BEFF00",
                              auto_dismiss=False,
                              content=popup_layout)

        sign_in_popup.open()
        self.exception_button.bind(on_press=sign_in_popup.dismiss,
                                   on_release=self.check_username_sign_in)
        return self

    # endregion

    # region check_username_sign_in
    def check_username_sign_in(self, instance):
        """
        Checks if the username has an existing configuration file
        """
        if self.username_input_text.text in []:  # TODO: add your string username
            self.switch_open_Layout_to_scan_Layout(instance)  # move to the next stage
        else:  # try loging in again + a message
            self.sign_in_open_popup(instance, "Invalid user name,"
                                              f"\n{self.username_input_text.text}"
                                              "\ndoesn't exist")
        return self

    # endregion

    # region try_again_non_premium_sign_in_popup
    def try_again_non_premium_sign_in_popup(self, instance, message=""):
        """
        The previous user did not fit the requirements (non-premium user)
        Trying to log in with a different user
        """
        log_in_request = message + SIGN_IN_NAME

        # region popup layout
        popup_layout = BoxLayout(size_hint=(1, 1),
                                 orientation="vertical")

        self.exception_label = Label(text=log_in_request)
        popup_layout.add_widget(self.exception_label)

        self.username_input_text = TextInput(multiline=False,
                                             size_hint_y=.3)
        popup_layout.add_widget(self.username_input_text)

        self.exception_button = Button(text="Login",
                                       size_hint_y=.3)
        popup_layout.add_widget(self.exception_button)
        # endregion

        sign_in_popup = Popup(title="Sign In",
                              size_hint=(0.9, 0.5),
                              separator_color="BEFF00",
                              auto_dismiss=False,
                              content=popup_layout)

        sign_in_popup.open()
        self.exception_button.bind(on_press=self.check_username_try_again_sign_in,
                                   on_release=sign_in_popup.dismiss)
        return self

    # endregion

    # region check_username_try_again_sign_in
    def check_username_try_again_sign_in(self, instance):
        """
        Checks if the username has an existing configuration file
        """
        if self.username_input_text.text in []:  # TODO: add your string username
            self.start_spotify(instance)
        else:
            self.try_again_non_premium_sign_in_popup(instance, f"Invalid user name,"
                                                               f"\n{self.username_input_text.text}"
                                                               f"\ndoesn't exist")
        return self

    # endregion
    # endregion

    # region scanning emotion view
    # region switch_open_Layout_to_scan_Layout
    def switch_open_Layout_to_scan_Layout(self, instance):
        """
        Change the window layout from the opening view to the scanning view
        """
        # change view
        self.background.source = BACKGROUND_PATH + "scan.jpeg"
        # button update settings
        self.switch_view_button.bind(on_press=self.print_scanning,
                                     on_release=self.scan_layout_scan_emotion)
        self.switch_view_button.pos_hint = {"center_x": .5,
                                            "center_y": .47}
        self.switch_view_button.size_hint = (0.5, 0.3)
        return self

    # endregion

    # region scan to emotion
    def print_scanning(self, instance):
        """
        Update the button options to view the 'scanning' sign
        """
        self.switch_view_button.opacity = 1
        self.switch_view_button.size_hint = (0.45, 0.25)
        self.switch_view_button.text = "Scanning..."
        self.switch_view_button.font_color = "white"
        return self

    # endregion
    # endregion

    # region result emotion + result view
    # region switch_scan_layout_to_emotion_layout
    def scan_layout_scan_emotion(self, instance):
        # scan emotion using the user's camera
        try:
            self.emotion = get_expressed_emotion()

        except OpenCameraException as ex:
            camera_error_popup = Popup(title=" ERROR",
                                       size_hint=(0.9, 0.5),
                                       separator_color="BEFF00",
                                       auto_dismiss=False)

            box = BoxLayout(size_hint=(1, 1),
                            orientation="vertical")

            box.add_widget(Label(text=str(ex)))
            box.add_widget(Button(text="okay, I fixed it",
                                  size_hint_y=.3,
                                  on_press=camera_error_popup.dismiss,
                                  on_release=self.try_again_to_find_emotion))

            camera_error_popup.content = box
            camera_error_popup.open()
            return self

        self.continue_switch_scan_layout_to_emotion_layout(instance)
        return self

    # endregion

    # region continue_switch_scan_layout_to_emotion_layout
    def continue_switch_scan_layout_to_emotion_layout(self, instance):
        # print the emotion result of the scan
        self.emotion_result_label.text = self.emotion

        # add emojy
        img = EMOJY_PATH + self.emotion + '.png'
        self.emotion_result_image.source = img
        self.emotion_result_image.pos_hint = {"center_x": .51, "center_y": .360}
        self.emotion_result_image.size_hint = (0.4, 0.4)

        # change view
        self.background.source = BACKGROUND_PATH + "try_again.jpeg"

        # update switch_view button settings
        self.switch_view_button.disabled = True
        self.switch_view_button.opacity = 0

        # update try again button
        self.try_again_button.disabled = False

        # update the spotify button
        self.transferring_button.disabled = False

        return self

    # endregion
    # endregion

    # region try again to scan for emotion
    def try_again_to_find_emotion(self, instance):
        # change background
        self.background.source = BACKGROUND_PATH + "scan.jpeg"

        # update switch_view_button
        self.switch_view_button.opacity = 0
        self.switch_view_button.size_hint = (0.5, 0.3)
        self.switch_view_button.disabled = False

        # update try again button
        self.try_again_button.disabled = True

        # update transferring button
        self.transferring_button.disabled = True

        # delete emojy
        self.emotion_result_image.source = EMOJY_PATH + "clear.png"

        # delete text
        self.emotion_result_label.text = ""
        return self

    # endregion

    # region transferring to spotify
    def transferring_to_spotify_layout(self, instance):
        # clear previous view
        self.emotion_result_label.text = ""
        self.emotion_result_image.source = EMOJY_PATH + "clear.png"

        # update view
        self.background.source = BACKGROUND_PATH + "transferring_to_spotify.jpeg"

        # update try_again button
        self.try_again_button.disabled = True
        self.try_again_button.opacity = 0

        # update spotify button
        self.transferring_button.disabled = True
        self.transferring_button.opacity = 0

        return self

    # endregion

    # region move to spotify
    def start_spotify(self, instance):
        """Play spotify and close the application"""
        try:
            activate_emotion_based_playlist_in_spotify(self.emotion, self.username_input_text.text)

        # region NoAvailableDevice
        except NoAvailableDevice as ex:
            general_exception_popup = Popup(title="ERROR",
                                            size_hint=(0.9, 0.5),
                                            separator_color="BEFF00",
                                            auto_dismiss=False)

            box = BoxLayout(size_hint=(1, 1),
                            orientation="vertical")

            box.add_widget(Label(text=str(ex)))
            box.add_widget(Button(text="okay, I fixed it",
                                  size_hint_y=.3,
                                  on_press=general_exception_popup.dismiss,
                                  on_release=self.continue_switch_scan_layout_to_emotion_layout))

            general_exception_popup.content = box
            general_exception_popup.open()

            return self
        # endregion

        # region NoSpotifyPremium
        except NoSpotifyPremium as ex:
            general_exception_popup = Popup(title="ERROR",
                                            size_hint=(0.9, 0.5),
                                            separator_color="BEFF00",
                                            auto_dismiss=False)

            box = BoxLayout(size_hint=(1, 1),
                            orientation="vertical")

            button_layout = BoxLayout(size_hint=(1, 1),
                                      orientation="horizontal")
            button_layout.add_widget(Button(text="close app",
                                            size_hint_y=.3,
                                            size_hint_x=.3,
                                            on_press=general_exception_popup.dismiss,
                                            on_release=self.stop))

            button_layout.add_widget(Button(text="try another account",
                                            size_hint_y=.3,
                                            size_hint_x=.5,
                                            on_press=general_exception_popup.dismiss,
                                            on_release=self.try_again_non_premium_sign_in_popup))

            box.add_widget(Label(text=str(ex)))
            box.add_widget(button_layout)

            general_exception_popup.content = box
            general_exception_popup.open()

            return self
        # endregion

        # region NoActiveDevice
        except NoActiveDevice as ex:
            no_active_popup = Popup(title="ERROR",
                                    size_hint=(0.9, 0.5),
                                    separator_color="BEFF00",
                                    auto_dismiss=False)

            box = BoxLayout(size_hint=(1, 1),
                            orientation="vertical")

            box.add_widget(Label(text=str(ex)))
            box.add_widget(Button(text="okay, I fixed it",
                                  size_hint_y=.3,
                                  on_press=no_active_popup.dismiss,
                                  on_release=self.continue_switch_scan_layout_to_emotion_layout))

            no_active_popup.content = box
            no_active_popup.open()

            return self
        # endregion

        # region general exception
        except:
            general_exception_popup = Popup(title="UNKNOWN ERROR",
                                            size_hint=(0.9, 0.5),
                                            separator_color="BEFF00",
                                            auto_dismiss=False)

            box = BoxLayout(size_hint=(1, 1),
                            orientation="vertical")

            button_layout = BoxLayout(size_hint=(1, 1),
                                      orientation="horizontal")
            button_layout.add_widget(Button(text="close app",
                                            size_hint_y=.3,
                                            size_hint_x=.3,
                                            on_press=general_exception_popup.dismiss,
                                            on_release=self.stop))

            button_layout.add_widget(Button(text="try again",
                                            size_hint_y=.3,
                                            size_hint_x=.5,
                                            on_press=general_exception_popup.dismiss,
                                            on_release=self.continue_switch_scan_layout_to_emotion_layout))

            box.add_widget(Label(text=f"Sorry, something went wrong\n"
                                      f"Please try again\n\n"
                                      f"The cause might be:\n"
                                      f"~ {sys.exc_info()[1]}."))
            box.add_widget(button_layout)

            general_exception_popup.content = box
            general_exception_popup.open()

            return self
            # endregion
        self.stop()
    # endregion
