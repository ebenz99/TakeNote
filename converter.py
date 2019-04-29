import os
import argparse
from pydub import AudioSegment

formats_to_convert = ['.m4a']
mydir = os.getcwd()

for (dirpath, dirnames, filenames) in os.walk(mydir):
    for filename in filenames:
        if filename.endswith('.m4a'):
            fpath = dirpath + '/' + filename
            (fpath, file_extension) = os.path.splitext(fpath)
            ext = file_extension.replace('.', '')
            try:
                track = AudioSegment.from_file(filepath,ext)
                wav_filename = filename.replace(ext, 'wav')
                wav_path = dirpath + '/' + wav_filename
                file_handle = track.export(wav_path, format='wav')
                os.remove(filepath)
            except:
                print("Something went wrong " + str(filepath))
                exit(3)