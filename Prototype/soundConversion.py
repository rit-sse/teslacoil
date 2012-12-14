import math
import wave

PI = 3.14159265358979323846264338327950288419716939937510

class SoundWave():
    __slots__ = ('timeStamp','unconverted','switchNotation','converted','amp')

    def __init__(self):
        self.timeStamp = []
        self.unconverted = []
        self.switchNotation = []
        self.converted = []
        self.amp = []

def printAll(sound):
    print(str(sound.timeStamp) + " : " + str(sound.unconverted) + " : " + str(sound.switchNotation) + " : " + str(sound.converted) + " : " + str(sound.amp))
    
        
def sqGen(freqs,sound,talkTime,noteTime):
    waveAdd = 0
    curFreq = len(freqs)
    curSwitch = 0
    print(str(freqs) + " : " + str(curFreq) + " : " + str(sound) + " : " + str(talkTime) + " : " + str(noteTime))
    for i in range(int(talkTime * noteTime)):
        if waveAdd == 0:
            curFreq -= 1
            if curFreq == -1:
                curFreq += len(freqs)
            waveAdd = int(talkTime / freqs[curFreq])
            if curSwitch == 0: #Every other time it does this
                curSwitch = 1
            else:
                curSwitch = 0
        sound.converted.append(curSwitch)
        waveAdd -= 1
    return sound

def createSound(hertz,sound,talkTime,noteTime):
    for i in range(int(noteTime * talkTime)):
        sound.timeStamp.append(float(i/talkTime))
        sound.unconverted.append((math.cos(float(i * 2 * PI * hertz) / talkTime)+2))
    return sound

def createSound2(hertz,hertz2,sound,talkTime,noteTime):
    for i in range(int(noteTime * talkTime)):
        sound.timeStamp.append(float(i/talkTime))
        sound.unconverted.append((math.cos(float(i * 2 * PI * hertz) / talkTime) + math.cos(float(i * 2 * PI * (hertz2)) / talkTime))+2)
    return sound
                                 
def convert(sound):
    cleaned = []
    for i in range(len(sound.unconverted)-1):
        cleaned.append(sound.unconverted[i]+sound.unconverted[i+1]/2)
    direction = 0
    if cleaned[0] >= cleaned[1]:
        direction = 0
    else:
        direction = 1
    holdamp = 0
    for x in range(len(cleaned)-1):
        if direction == 0:
            sound.converted.append(0)
            sound.amp.append(holdamp)
            if cleaned[x] < cleaned[x+1]:
                direction = 1
                holdamp = cleaned[x]
        else:
            sound.converted.append(1)
            sound.amp.append(holdamp)
            if cleaned[x] > cleaned[x+1]:
                direction = 0
                holdamp = 0
    ending = sound.converted[len(sound.converted)-1]
    sound.converted.append(ending)
    sound.converted.append(ending)
    sound.amp.append(0)
    sound.amp.append(0)
    return sound

testSound = SoundWave()

########################################################################################
#EDIT HERE##############################################################################
# sounds = [frequency(s)]
# testSound = sqGen(sounds, testSound, fileReadRate(44100), time)
sounds = [220]
testSound = sqGen(sounds, testSound, 44100, 1)
########################################################################################
#printAll(testSound)
x = wave.open("songfile.wav","w")
x.setparams([1, 1, 44100, 0, 'NONE', 'NONE'])
toFile = []
for i in range(len(testSound.converted)):
    toFile.append(int(testSound.converted[i]*90))
x.writeframes(bytes(toFile))
x.close()
p = open("songfile.csv","w")
for i in range(min(len(testSound.timeStamp),1000)):
    p.write(str(testSound.timeStamp[i]) + "," + str(testSound.unconverted[i]) + "," + str(testSound.converted[i]) + "\n")
p.close()
