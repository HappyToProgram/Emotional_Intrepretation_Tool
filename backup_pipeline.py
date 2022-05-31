import sounddevice as sd
import time
import soundfile as sf
import librosa
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras.models import model_from_json
import numpy as np


if __name__ == '__main__':
    input = input("Press Q and Enter to start or E and Enter to Exit: ")
    if input == 'q':  # if key 'q' is pressed

        #recording
        fs = 44100
        duration = 5  # seconds
        print("Recording begins in 5 seconds, you have 2.5 seconds to record.")
        time.sleep(5)
        print("Recording Audio")
        myrecording = sd.rec(duration * fs, samplerate=fs, channels=1, dtype='float32')
        sd.wait()
        sf.write('output.wav', myrecording, fs)

        #model loading
        lb = LabelEncoder()
        json_file = open('C:/Users/erics/PycharmProjects/INFO442_2/Models/sr_model', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new sr_model
        loaded_model.load_weights("C:/Users/erics/PycharmProjects/INFO442_2/Weights/Emotion_Voice_Detection_Model.h5")
        print("Loaded model from disk")
        X, sample_rate = librosa.load('C:/Users/erics/PycharmProjects/INFO442_2/output.wav',
                                      res_type='kaiser_fast', duration=2.5,sr=22050*2,offset=0.5)

        #transforming
        sample_rate = np.array(sample_rate)
        mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13), axis=0)
        featurelive = mfccs
        livedf2 = featurelive
        livedf2 = pd.DataFrame(data=livedf2)
        livedf2 = livedf2.stack().to_frame().T
        twodim = np.expand_dims(livedf2, axis=2)

        #predicting
        livepreds = loaded_model.predict(twodim,
                                         batch_size=32,
                                         verbose=1)
        livepreds1 = livepreds.argmax(axis=1)
        liveabc = livepreds1.astype(int).flatten()


        # Results
        print("\nEmotion:")
        if liveabc == 0:
            print("Female_angry")
        elif liveabc == 1:
            print("Female Calm")
        elif liveabc == 2:
            print("Female Fearful")
        elif liveabc == 3:
            print("Female Happy")
        elif liveabc == 4:
            print("Female Sad")
        elif liveabc == 5:
            print("Male Angry")
        elif liveabc == 6:
            print("Male calm")
        elif liveabc == 7:
            print("Male Fearful")
        elif liveabc == 8:
            print("Male Happy")
        elif liveabc == 9:
            print("Male sad")

    elif input == 'e':
        print('Exiting')