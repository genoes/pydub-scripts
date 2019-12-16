# Segment audio files

## Description

This script uses [pydub](https://github.com/jiaaro/pydub/ "jiaaro - Pydub | Github") to splice a WAVE (.wav) file into multiple segments.

Pydub uses **`make_chunks`**, which allows you to specify segment lengths in milliseconds (ms).
* e.g., **`chunk_length_ms = 10000`** will segment an audio file into 10 second intervals. 
* Note that the duration of the final audio segment will often be less than the specified length.



## Installation
* Python 3.x
* Open Terminal
* Install ffmpeg
	* **`pip install ffmpeg`**
* Install pydub:
	* **`pip install pydub`**

This setup is all you need to segment WAVE files.


## Run
* Run script
	*  **`python audio-segment.py`**
* An output subdirectory **(`./output`)** will be created automatically.
* You will then be prompted to enter the source path to the audio file.
* The script will then populate the output subdirectory with the segmented WAVE files.


## Segment other audio file formats
You can modify the script to use with other audio formats. 

Simply replace `wav` in the script with another audio file extension such as `mp3`, `flac`, `ogg`, etc .

### Installation
This setup requires **[Homebrew](https://brew.sh/ "Homebrew - The missing package manager for macOS or Linux")**
* Open Terminal
* Install Homebrew 
	* **`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`**
* Install ffmpeg:
 	* **`brew install ffmpeg`** 
