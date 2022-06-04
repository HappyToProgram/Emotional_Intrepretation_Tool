# Emotion Interpretation Tool:
---
### References: 
1. [Emotion Recognition in Audio and Video Using Deep Neural Networks](https://arxiv.org/pdf/2006.08129.pdf)
2. [MULTI-MODAL EMOTION RECOGNITION ON IEMOCAP WITH NEURAL NETWORKS](https://arxiv.org/pdf/1804.05788.pdf)
3. [IEMOCAP: Interactive emotional dyadic motion capture
database](https://ecs.utdallas.edu/research/researchlabs/msp-lab/publications/Busso_2008_5.pdf)
---
## Directories:
- `Model_Testing`: A directory with the initial model building along with processing notebook and simple data exploration. `train_paths.pkl` and `test_paths.pkl` is a Python list containing the directory path to the train and test data.
- `model` : A directory containing all the models that have been trained on the data(in mel spectrogram or STFT). It also has the notebook that can be used for inference on the model that has been trained.
- `Data_Preprocessing.ipynb`: A Jupyter notebook with an EDA of Audio data in general. It covers the basics of Sampling Rate, Short-time Fourier Transform, and Spectrograms 
- `main_pipeline.py` : Implementation of the model and the preprocessing part. It is the tool that we use to predict.
- `sort_emotion_data.sh` : shell script to sort the files so that each audio file belongs to a directory named with the corresponding emotion.
- `Models` and `Weights` : directories used for loading the models in the pipleline code.
