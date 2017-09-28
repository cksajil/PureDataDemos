import pyaudio
import numpy as np

RATE    = 44100
CHUNK   = 128

p               =   pyaudio.PyAudio()

player = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, output=True, 
frames_per_buffer=CHUNK)
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)

for i in range(int(20*RATE/CHUNK)): #do this for 10 seconds
    player.write(np.fromstring(stream.read(CHUNK),dtype=np.int16),CHUNK)

stream.stop_stream()
stream.close()
p.terminate()