#include "SoundWave.h"

using namespace std;

SoundWave::SoundWave(){

}

list<int> SoundWave::getTimeStamp(){
	return _TimeStamp;
}

void SoundWave::setTimeStamp(list<int> timeStamp){
	_TimeStamp = timeStamp;
}

list<int> SoundWave::getUnconverted(){
	return _Unconverted;
}

void SoundWave::setUnconverted(list<int> unconverted){
	_Unconverted = unconverted;
}

list<int> SoundWave::getSwitchNotation(){
	return _SwitchNotation;
}

void SoundWave::setSwitchNotation(list<int> switchNotation){
	_SwitchNotation = switchNotation;
}

list<int> SoundWave::getConverted(){
	return _Converted;
}

void SoundWave::setConverted(list<int> converted){
	_Converted = converted;
}

list<int> SoundWave::getAmp(){
	return _Amp;
}

void SoundWave::setAmp(list<int> amp){
	_Amp = amp;
}
