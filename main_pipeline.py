import sounddevice as sd
import time
import librosa
import tensorflow as tf
from tensorflow import keras
import numpy as np
import soundfile as sf

# LABELDICT:
labeldict={0: 'Sadness',
    1: 'Excited',
    2: 'Happiness',
    3: 'Anger',
    4: 'Frustration',
    5: 'Other'}


def preprocess_input(path): # Returns a list of x (batch_size, timesteps, feature)
    # Preprocess x:
    x = get_mel(path)
    # Reshaping so that the order is not messed up
    x = x.reshape(1, 256, -1)
    # Transposing so that we have timesteps in dim 1
    x = x.transpose((0, 2, 1))
    # Convert to tensor and of type tf.float16 for faster operation
    x = tf.convert_to_tensor(x, dtype=tf.float16)
    return x


# Decode the one hot encoded:
def decode_emotion(one_hot):
    idx_arg_max = np.argmax(one_hot)
    return labeldict[idx_arg_max]


def get_mel(path):
    data, _ = librosa.load(path, sr=44100)
    mels = librosa.feature.melspectrogram(y=data, sr=44100, n_mels=256)
    return mels


def predict_emotion(path):
    data = preprocess_input(path)
    predicted = model(data, training=False)
    result = decode_emotion(predicted)
    print(f"\nThe emotion associated with the file is {result}")
    return result


if __name__ == '__main__':
    input = input("Press Q and Enter to start or E and Enter to Exit: ")
    if input == 'q':  # if key 'q' is pressed
        fs = 44100
        duration = 5  # seconds
        print("Recording begins in 5 seconds, you have 5 seconds to record.")
        time.sleep(5)
        print("Recording Audio")
        myrecording = sd.rec(duration * fs, samplerate=fs, channels=1, dtype='float32')
        sd.wait()
        sf.write('output.wav', myrecording, fs)

        # Load Model
        model = keras.models.load_model('C:/Users/erics/PycharmProjects/INFO442_2/Models/MEL_LSTM.h5')

        predict_emotion('C:/Users/erics/PycharmProjects/INFO442_2/output.wav')

    elif input == 'e':
        print("Exiting")