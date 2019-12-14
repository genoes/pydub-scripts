#Segment audio files

##Description

This script uses [Pydub](https://github.com/jiaaro/pydub/ "jiaaro - Pydub | Github") to splice a WAVE (.wav) file into multiple segments.

Pydub uses **`make_chunks`**, which allows you to specify segment lengths in milliseconds (ms).
* e.g., **`chunk_length_ms = 10000`** will segment an audio file into 10 second intervals. 
* Note that the duration of the final audio segment will often be less than the specified length.

------------


##Installation
Open Terminal
* Install ffmpeg
	* **`pip install ffmpeg`**
* Install pydub:
	* **`pip install pydub`**

This setup is all you need to segment WAVE files.


------------
##Segment other audio file formats
You can modify the script to use with other audio formats.
* Use an editor to replace `wav` in the script with another file format such as `mp3`, `flac`, `ogg`, etc .

###Installation
This setup requires **[Homebrew](https://brew.sh/ "Homebrew - The missing package manager for macOS or Linux")**
* Open Terminal
* Install Homebrew 
	* **`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`**
* Install ffmpeg:
 	* **`brew install ffmpeg`**

------------
##Run
* Open Terminal
* Run script
	*  **`python audio-segment.py`**
* A subdirectory **(`./output`)** will automatically be created.
* You will then be prompted to **`Enter the path to the source file`**.
* The script will then populate the output directory with the segments.
