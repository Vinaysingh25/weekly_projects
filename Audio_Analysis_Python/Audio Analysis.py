import os
import librosa as li
import librosa.display
import pandas as pd

data, sampling = li.load('sample.wav')
print (data, sampling)
plt.figure(figsize=(12, 4))
librosa.display.waveplot(data, sr=sampling)