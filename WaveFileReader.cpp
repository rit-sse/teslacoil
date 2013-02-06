#include <stdio.h>
#include <stdlib.h>
#include <sndfile.h>
#include "SoundWave.h"
#include "WaveFileReader.h"

using namespace std;

WaveFileReader::WaveFileReader(){

}

void WaveFileReader::printAll(SoundWave sound){

}

SoundWave WaveFileReader::sqGen(List<Integer> freqs, SoundWave sound, int talkTime, int noteTime){

}

SoundWave WaveFileReader::createSound(int hertz, SoundWave sound, int talkTime, int noteTime){

}

SoundWave WaveFileReader::createSound2(int hertz, int hertz2, SoundWave sound, int talkTime, int noteTime){

}

SoundWave WaveFileReader::convert(SoundWave sound){

}

void WaveFileReader::run(){

}

int main(){

	SNDFILE *sf;
	SF_INFO info;
	int num, num_items;
	int *buf

	/**Open the WAV file*/
	info.format = 0;
	sf = sf_open("Prototype/soundfile.wav",SFM_READ,&info);
	if (sf == NULL){
		printf("Failed to open the file.\n");
		exit(-1);
	}
	num = sf_read_int(sf,buf,num_items);
}
