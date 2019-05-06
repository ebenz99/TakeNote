from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

# Define a function to normalize a chunk to a target amplitude.
def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)

# Load your audio.
song = AudioSegment.from_file("raw//testaudio.wav")



# Use the loaded audio.
# Specify that a silent chunk must be at least 1 seconds or 1000 ms long.
# Consider a chunk silent if it's quieter than -40 dBFS.
# This will leave 100 ms of silence on either end
chunks = split_on_silence (song, min_silence_len = 1800, silence_thresh = -40, keep_silence=300)

#makes the directory to save the outputs
os.makedirs("chunks", exist_ok=True)

# Process each chunk with your parameters
for i, chunk in enumerate(chunks):
    # Create a silence chunk that's 0.5 seconds (or 500 ms) long for padding.
    silence_chunk = AudioSegment.silent(duration=500)

    # Add the padding chunk to beginning and end of the entire chunk.
    audio_chunk = silence_chunk + chunk + silence_chunk

    # Normalize the entire chunk.
    normalized_chunk = match_target_amplitude(audio_chunk, -20.0)

    # Export the audio chunk
    print("Exporting chunk{0}.wav.".format(i))
    normalized_chunk.export(".//chunks//wav//chunk{0}.wav".format(i),format = "wav")