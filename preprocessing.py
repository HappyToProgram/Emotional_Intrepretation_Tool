import glob
import re

audio_directory = 'C:/Users/Owner/PycharmProjects/INFO442Proj/IEMOCAP_full_release'
label_directory = 'C:/Users/Owner/PycharmProjects/INFO442Proj/Dialog_Dir/dialog_sess*/EmoEvaluation/Categorical/*.txt'
for file in glob.glob(label_directory):
    f = open(file, "r")
    for line in f.readlines():
        line = re.sub('[:;]', '', line)
        line = line.split()
        del line[2:]
        print(line)