from pydub import AudioSegment
import os
# files
for filename in os.listdir("clips/"):
    sound = AudioSegment.from_mp3("clips/"+filename)
    newFilename=filename.replace(".mp3",".wav")
    sound.export("clips_wav/"+newFilename, format="wav")