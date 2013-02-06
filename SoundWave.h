#include <list>

class SoundWave{

	public:
		SoundWave();
		std::list<int> getTimeStamp();
		void setTimeStamp(std::list<int>);
		std::list<int> getUnconverted();
		void setUnconverted(std::list<int>);
		std::list<int> getSwitchNotation();
		void setSwitchNotation(std::list<int>);
		std::list<int> getConverted();
		void setConverted(std::list<int>);
		std::list<int> getAmp();
		void setAmp(std::list<int>);
	private:
		std::list<int> _TimeStamp;
		std::list<int> _Unconverted;
		std::list<int> _SwitchNotation;
		std::list<int> _Converted;
		std::list<int> _Amp;

};
