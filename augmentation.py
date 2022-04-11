import random
import librosa
import numpy as np
import soundfile as sf
import librosa.display
import matplotlib.pyplot as plt
import os
import os


def add_white_noise(signal, noise_percentage_factor):
    noise = np.random.normal(0, signal.std(), signal.size)
    augmented_signal = signal + noise * noise_percentage_factor
    return augmented_signal


def time_stretch(signal, time_stretch_rate):
    """Time stretching implemented with librosa:
    https://librosa.org/doc/main/generated/librosa.effects.pitch_shift.html?highlight=pitch%20shift#librosa.effects.pitch_shift
    """
    return librosa.effects.time_stretch(signal, time_stretch_rate)


def pitch_scale(signal, sr, num_semitones):
    """Pitch scaling implemented with librosa:
    https://librosa.org/doc/main/generated/librosa.effects.pitch_shift.html?highlight=pitch%20shift#librosa.effects.pitch_shift
    """
    return librosa.effects.pitch_shift(signal, sr, num_semitones)


def random_gain(signal, min_factor=0.5, max_factor=0.5):
    gain_rate = random.uniform(min_factor, max_factor)
    augmented_signal = signal * gain_rate
    return augmented_signal


def invert_polarity(signal):
    return signal * -1


def plot_signal(signal, augmented_signal, sr):
    fig, ax = plt.subplots(nrows=2)
    librosa.display.waveplot(signal, sr=sr, ax=ax[0])
    ax[0].set(title="Original signal")
    librosa.display.waveplot(augmented_signal, sr=sr, ax=ax[1])
    ax[1].set(title="Signal after lowering the gain")
    plt.show()
if __name__ == "__main__":
        i = 0
        # for filename in os.listdir("follow/"):
        #     signal, sr = librosa.load("follow/"+filename)
        #     augmented_signal = random_gain(signal)
        #     cutFilename=filename.replace(".wav","")
        #     sf.write("followa/"+cutFilename+".wav", augmented_signal, sr)#這個是會覆蓋原版的
        signal, sr = librosa.load("augTest/left.2stcbdk6.ingestion-dbd44ffcb-kmfhm.s1.wav")
        augmented_signal = random_gain(signal)
        sf.write("augTest/aug.wav", augmented_signal, sr)
        plot_signal(signal,augmented_signal,sr)

    #Good pitch scale values for male four are -1,1,2
    #Good pitch scale values for female yes are -1,-2