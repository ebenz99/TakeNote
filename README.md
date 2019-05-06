# TakeNote

Do you frequently read PDFs and take notes? Do you prefer to take those notes on your computer? If so, say goodbye to the `alt-tab` nightmares of your past!

TakeNote is an application that I use for note-taking in most of my humanities classes. As a broke college student, I prefer the PDF versions of textbooks to the hardcopies from my campus's bookstore. But, when I'm reading these books, I run into a problem. I find myself constantly having to read a couple sentences, `alt-tab` to my notes window, click into my notes window to get a cursor, type in some notes, `alt-tab` back to my textbook window, and find my place in the page to begin reading again and restart this tedious cycle.

With TakeNote, I just open the GUI from this repo and hit "Record". This starts a note-taking session in the background. If I'm reading my textbook and want to take a note, all I have to do now is say "Take Note" followed by whatever key point I'd like to have jotted down. I can do this over and over again, and at the end of my chapter of reading, I simply navigate back to the "Stop Recording" button and click it. The program then takes the audio file of whatever I've said since I started reading, cuts out all the unecessary silence from the file, and ships it to GCP for speech processing. When GCP sends back the speech data, that data is parsed with looking for instances of the phrase "Take Note", and notes immediately following that phrase are transcribed into a text file and opened onto your screen for easy `cop-paste` access into whatever note-organization software your prefer.

## Requirements

### Brew
Some parts of this application require software not default on MacOS. The following should be installed with the command `brew install <library>`
1. `portaudio` - A cross-platform library for doing I/O with your machine's microphone. Necessary for python's access as an audio controller.
2. `ffmpeg` - A file conversion library for sound files. Will be used to modify channels and the frame rate on recorded audio.

### Pip/Conda
The other requirements for this application are modules available to Python 3.x. These can be installed with `pip install <module>` or `conda install <module>`
1. `pydub` - A module for manipulating audio files
2. `google-cloud` - Google's API for speech-to-text conversion in python

### GCP
The perfect version of this project uses Pocketsphinx's offline audio recognition library. That version doesn't exist, however, because pocketsphinx really hates usability. In lieu of using their tools for this project, I turned to GCP, which means there's an extra step. In order to run this application, you must have/create a Google Cloud Platform account and set up a key for their `speech-to-text` API. The file with this key should be saved in your main project directory.

