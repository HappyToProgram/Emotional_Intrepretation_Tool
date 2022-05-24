import glob
import re
import librosa  # Audio processing library
import numpy as np
import librosa.display  # For displaying spectrograms

label_directory = 'C:/Users/erics/PycharmProjects/INFO442_2/IEMOCAP_full_release/Session*/dialog/EmoEvaluation/Categorical/*.txt'
audio_directory = 'C:/Users/erics/PycharmProjects/INFO442_2/IEMOCAP_full_release/AudioFiles'


def transform(audio_file):
    y, sr = librosa.load(audio_file, sr=44100)

    # Apply Short-Time Fourier Transform
    D = librosa.stft(y)

    # Separate the magnitude and phase
    S, phase = librosa.magphase(D)

    # Decompose by nmf
    components, activations = librosa.decompose.decompose(S, n_components=8, sort=True)

    # Spectrogram: Discrete Fourier Transform where each data point (cut by sampling rate)  frequency is binned.
    S = np.abs(librosa.stft(y))


for file in glob.glob(label_directory):
    f = open(file, "r")
    for line in f.readlines():
        line = re.sub('[:;]', '', line)
        line = line.split()
        del line[2:]
        text_type = line[0][7:12]
        if text_type == 'impro':
            wav_dir = '/' + line[0][:14] + '/'
            audio_file = audio_directory + wav_dir + line[0] + '.wav'
            transform(audio_file)
        else:
            wav_dir = '/' + line[0][:14] + '/'
            audio_file = audio_directory + wav_dir + line[0] + '.wav'
            transform(audio_file)
