import os
import argparse
from pydub import AudioSegment

formats_to_convert = ['.wav']
mydir = os.getcwd() + "/chunks/wav"
projDir = os.getcwd()

for (dirpath, dirnames, filenames) in os.walk(mydir):
    for filename in filenames:
        if filename.endswith('.wav'):
            fpath = dirpath + '/' + filename
            (fpath, file_extension) = os.path.splitext(fpath)
            ext = file_extension.replace('.', '')
            try:
                track = AudioSegment.from_file(str(fpath+"."+ext))
                flac_filename = filename.replace(ext, 'flac')
                os.chdir(mydir)
                os.system(("ffmpeg -i " + filename+ " -ac 1 " + flac_filename))
                os.chdir(projDir+"//chunks")
                os.remove(mydir+"//"+str(filename))
                os.system(("cp -f "+ mydir+"//"+flac_filename + " " + projDir + "//chunks//flac/"))
            except:
                print("Something went wrong with converting " + str(fpath))
                exit(3)
