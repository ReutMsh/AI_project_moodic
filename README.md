# AI_project_moodic

# Objective:

Have you ever wished to turn on a song to make yourself feel better?\
so you visited Spotify or YouTube and browsed the song list. 

Yet you were unable to find a single music that suited your mood?

Our system detects your mood, based on your facial expressions using Artificial Intelligence and Computer Vision.\
Then, in your own Spotify player, a playlist matching your mood will be activated.

# How does it work?

As mentioned before, we use CV (Computer Vision) to identify your facial expression and connect it to spotify using a Spotify API.


**The steps:**
1. *Step 1: creating a user interface.* The first thing users see when they start the project, is the GUI.\
We used the kivy library to create the user interface.\
See more about kivy - https://kivy.org/doc/stable/guide/basic.html\

2. *Step 2: facial recognition.*  In order to recognize any emotion, we must first somehow identify a face.\
We used the OpenCV library to get camera access.\
We took frames from the camera feed and identified faces in each frame using a model developed by Intel.\
The faces model is located in the 'emotion' folder in the main directory.\
See more about OpenCV - https://opencv.org/

3. *Step 3: emotion detection.* Once the face has been identified, we now extract out the emotion.\
We used the fer library to find the emotion in the image.\
See more about fer - https://pypi.org/project/fer/

4. *Step 4: connect to Spotify.* The final step is connecting to Spotify and starting a playlist that suits the feeling.\
We used the tekore library to access and manipulate a Spotify user's player.\
The access a user on Spotify require the user's username, passcode and token.\
These details are private and confidential and do not appear in the project.\
You must manually enter them following the instructions at the bottom of this page.\


# Requirements

~ Make sure to install the correct version for each library mentioned in the requirements.txt file.\
~ Make sure your camera is not being used by another process. Else it will not be accessible.\
~ Make sure your Spotify account is active.\
  Open Spotify and activate the player (turn it on and off once) to make sure the user is active.\
~ Make sure your Spotify user's configuration file is in the right format and location according to the attached guide.\
  This information is confidential and will not be stored or used other than what specified above.

# Configuration file instructions:

1. In the '\Spotify' folder, open a new .txt file named "credentials_{yourName}.config" {fill with your name or userName}.
2. The content of the file will be as followed:
   - [DEFAULT]
   - SPOTIFY_CLIENT_ID =
   - SPOTIFY_CLIENT_SECRET =
   - SPOTIFY_REDIRECT_URI = https://example.com/callback
3. Go to https://developer.spotify.com/dashboard/applications
4. Choose 'create an app'. In the 'App name' section enter 'moodic'. Fill the description as you want.
5. In the app you created copy the CLIENT ID to SPOTIFY_CLIENT_SECRET in your config file.
6. Press the 'Show Client Secret'. Your token (CLIENT SECRET) will appear.\
Copy it to SPOTIFY_CLIENT_SECRET in the config file. this token is private, don't send or expose it to anyone.
7. Open the project in your work environment.
8. Open the get_reference_token.py in the \Spotify folder.
9. Change the CONFIG_FILE to equal - "credentials_{yourName}.config" (the name you gave the config file).
10. Run get_reference_token.py file.
11. A web page will open. Sign in, if needed, and scroll down and accept the terms.
13. Another page will open, its title will be 'example domain'. Copy its link to the python terminal.\
This step will add your SPOTIFY_USER_REFRESH token to the configuration file.\
14. Your configuration file is now set and ready to start.
15. The last step is to make the program recognize your config file. To do that:
    1. Go to GUI/home_gui.py
    2. Open the function check_username_sign_in(), assumed to be in line 129.
    3. The if statement has an empty tuple []. Enter your {yourName} from the configuration file name into the tuple, as a string.
    4. Follow steps 2-3 for the check_username_try_again_sign_in function assumed to be in line 181.

Now you are all set to start moodic and listen to music for your mood :)