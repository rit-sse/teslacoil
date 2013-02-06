class WaveFileReader{

	public:
		WaveFileReader();
		void printAll(SoundWave);
		SoundWave sqGen(std::List<Integer>,SoundWave,int,int);
		SoundWave createSound(int,SoundWave,int,int);			SoundWave createSound2(int,int,SoundWave,int,int);
		SoundWave convert(SoundWave);
		void run();
	private:

}
