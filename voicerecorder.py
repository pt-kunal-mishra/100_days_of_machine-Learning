import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

frequency = 48000

duration = 5

recording=sd.rec(int(duration*frequency),samplerate=frequency,channels=2)

sd.wait()

write("record.wav",frequency,recording)