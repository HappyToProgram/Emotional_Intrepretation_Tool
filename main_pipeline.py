import sounddevice as sd
import time
import librosa
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2

labeldict = {
    'Sadness': 0,
    'Excited': 1,
    'Happiness': 2,
    'Anger': 3,
    'Frustration': 4,
    'Other': 5
}


def pre_processing(audio_data):
    STFT = np.abs(librosa.stft(audio_data))
    # Zero-padding:
    x = keras.preprocessing.sequence.pad_sequences(STFT, padding="post", maxlen=1489, dtype=np.float32)  # maxlen is after discovering the whole training data
    # Reshaping so that the order is not messed up
    x = x.reshape(-1, 1025, 1489)
    # Transposing so that we have timesteps in dim 1
    x = x.transpose((0, 2, 1))
    return x


while True:
    print("Press Q and Enter to start")
    print("Press E and Enter to exit")
    input = input().lower()
    if input == 'q':  # if key 'q' is pressed
        fs = 44100
        duration = 5  # seconds
        print("Recording begins in 5 seconds, you have 5 seconds to record.")
        time.sleep(5)
        print("Recording Audio")
        myrecording = sd.rec(duration * fs, samplerate=fs, channels=1, dtype='float32')
        sd.wait()

        # TODO
        transformed_data = pre_processing(np.squeeze(myrecording))
        print(transformed_data)

        # TODO
        # Take results from model and match with labels
        # Print result

        break
    elif input == 'e':
        break
