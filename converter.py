import os
from pydub import AudioSegment

mydir = os.getcwd()

for (dirpath, dirnames, filenames) in os.walk(mydir):
    for filename in filenames:
        if filename.endswith('.m4a'):
            fpath = dirpath + '/' + filename
            (fpath, file_extension) = os.path.splitext(fpath)
            ext = file_extension.replace('.', '')
            try:
                track = AudioSegment.from_file(str(fpath+"."+ext))
                wav_filename = filename.replace(ext, 'wav')
                os.system(("ffmpeg -i " + filename + " -ac 2 -f wav " + wav_filename))
                ext = "wav"
                flac_filename = wav_filename.replace(ext, 'flac')
                os.system(("ffmpeg -i " + wav_filename+ " -ac 1 " + flac_filename))
                wav_path = dirpath + '/' + wav_filename
                os.remove(str(filename))
                os.remove(str(fpath+"wav"))
            except:
                print("Something went wrong with converting " + str(fpath))
                exit(3)