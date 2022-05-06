# Created by Wallee#8314/Red-exe-Engineer

# Imports
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

from gtts import gTTS
from playsound import playsound

from os import system
from sys import argv

# Set words to an empty string
words = ""

# Error protection
try:

    # Loop through the argv
    for word in argv[1:]:

        # Add the current argument to words
        words = words + word + " "

    # Create the audio and save it to tts.mp3
    audio = gTTS(text=words, lang="en")
    audio.save("tts.mp3")

    # Play the audio file
    playsound("tts.mp3")

    # Remove the audio file
    system("rm tts.mp3")

# Oops
except:

    # Tell the user the audio could not be played
    mc.postToChat("Something went wrong")
