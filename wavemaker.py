from pocketsphinx import LiveSpeech
for phrase in LiveSpeech(audio_device="MacBook Pro Microphone"): print(phrase)