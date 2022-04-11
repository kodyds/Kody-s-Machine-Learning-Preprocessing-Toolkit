import pandas as pd
import shutil
data = pd.read_csv("validated.tsv",sep="\t")
labels=data.sentence
names=data.path
downVote=data.down_votes
i=0
for label in labels:
    if (label=="零")and(downVote[i]==0):
        shutil.move(("clips_wav/"+names[i]).replace(".mp3",".wav"),("zeroc/"+"zeroc_"+names[i]).replace(".mp3",".wav"))
    if (label=="一")and(downVote[i]==0):
        shutil.move(("clips_wav/"+names[i]).replace(".mp3",".wav"),("onec/"+"onec_"+names[i]).replace(".mp3",".wav"))
    if (label=="二")and(downVote[i]==0):
        shutil.move(("clips_wav/"+names[i]).replace(".mp3",".wav"),("twoc/"+"twoc_"+names[i]).replace(".mp3",".wav"))
    if (label=="三")and(downVote[i]==0):
        shutil.move(("clips_wav/"+names[i]).replace(".mp3",".wav"),("threec/"+"threec_"+names[i]).replace(".mp3",".wav"))
    if (label=="四")and(downVote[i]==0):
        shutil.move(("clips_wav/"+names[i]).replace(".mp3",".wav"),("fourc/"+"fourc_"+names[i]).replace(".mp3",".wav"))
    if (label=="五")and(downVote[i]==0):
        shutil.move(("clips_wav/"+names[i]).replace(".mp3",".wav"),("fivec/"+"fivec_"+names[i]).replace(".mp3",".wav"))
    if (label=="六")and(downVote[i]==0):
        shutil.move(("clips_wav/"+names[i]).replace(".mp3",".wav"),("sixc/"+"sixc_"+names[i]).replace(".mp3",".wav"))
    if (label=="七")and(downVote[i]==0):
        shutil.move(("clips_wav/"+names[i]).replace(".mp3",".wav"),("sevenc/"+"sevenc_"+names[i]).replace(".mp3",".wav"))
    if (label=="八")and(downVote[i]==0):
        shutil.move(("clips_wav/"+names[i]).replace(".mp3",".wav"),("eightc/"+"eightc_"+names[i]).replace(".mp3",".wav"))
    if (label=="九")and(downVote[i]==0):
        shutil.move(("clips_wav/"+names[i]).replace(".mp3",".wav"),("ninec/"+"ninec_"+names[i]).replace(".mp3",".wav"))
    if (label=="係")and(downVote[i]==0):
        shutil.move(("clips_wav/"+names[i]).replace(".mp3",".wav"),("yesc/"+"yesc_"+names[i]).replace(".mp3",".wav"))
    if (label=="唔係")and(downVote[i]==0):
        shutil.move(("clips_wav/"+names[i]).replace(".mp3",".wav"),("noc/"+"noc_"+names[i]).replace(".mp3",".wav"))
    i=i+1
