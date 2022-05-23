import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tensorflow as tf

tf.keras.utils.set_random_seed(442)
labeldict = {
    'Sadness': 0,
    'Excited': 1,
    'Happiness': 2,
    'Anger' : 3,
    'Frustration' : 4,
    'Other' : 5
}
while True:
    fs = 44100
    duration = 5  # seconds
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=2, dtype='float32')
    print("Recording Audio")
    sd.wait()
    print("Audio recording complete , Play Audio")
    sd.play(myrecording, fs)
    sd.wait()
    print("Play Audio Complete")
    break