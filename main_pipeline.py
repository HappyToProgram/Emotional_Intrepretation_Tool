import sounddevice as sd
import time
import tensorflow as tf
labeldict = {
    'Sadness': 0,
    'Excited': 1,
    'Happiness': 2,
    'Anger' : 3,
    'Frustration' : 4,
    'Other' : 5
}
while True:
    print("Press Q and Enter to start")
    print("Press E and Enter to exit")
    input = input().lower()
    if input == 'q':  # if key 'q' is pressed
        fs = 44100
        duration = 5  # seconds
        print("Recording begins in 5 seconds, you have # seconds to record.")
        time.sleep(5)
        print("Recording Audio")
        myrecording = sd.rec(duration * fs, samplerate=fs, channels=2, dtype='float32')
        #TODO
            #Transform through instructions from Hajun on how to do it properly
            #Load audio data correctly into model for fitting

        #TODO
            #Take results from model and match with labels
            #Print result

        #print("Audio recording complete , Play Audio")
        #sd.play(myrecording, fs)
        #sd.wait()
        #print("Play Audio Complete")
        break
    elif input == 'e':
        break